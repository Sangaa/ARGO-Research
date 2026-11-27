"""Bounded R02 arithmetic and issuance-shape verifier.

Run with Python 3.12+ and the standard library: python r02_verifier.py

This does not establish that a source was public at cutoff, validate the supplied
calendar's authority, verify snapshot bytes, or prove forecast immutability.
"""
import hashlib
import json
import os
from datetime import date, datetime, timezone
from math import exp, floor, isclose, isfinite, log, sqrt
import random
import re
import unittest
import tempfile
from pathlib import Path

WEIGHTS = {"DXY": 0.30, "REAL": 0.35, "MOM": 0.20, "ETF": 0.15}
FEATURE_RULES = {
    "DXY": ("decimal_return", -1.0, 0.015),
    "REAL": ("bp", -1.0, 20.0),
    "MOM": ("decimal_return", 1.0, 0.04),
    "ETF": ("tonnes", 1.0, 40.0),
}
AMPLITUDE = 0.013
SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


def clip(value, low=-1.0, high=1.0):
    return max(low, min(high, value))


def feature_score(name, value, unit):
    if name not in FEATURE_RULES:
        raise ValueError("unknown feature")
    expected_unit, sign, scale = FEATURE_RULES[name]
    if unit != expected_unit:
        raise ValueError("wrong unit for " + name)
    if not isfinite(value):
        raise ValueError("non-finite feature")
    return clip(sign * value / scale)


def weighted_score(inputs):
    if set(inputs) != set(WEIGHTS):
        raise ValueError("feature set mismatch")
    scores = {}
    contributions = {}
    coverage = 0.0
    for name, raw in inputs.items():
        if raw is None:
            scores[name] = None
            contributions[name] = 0.0
            continue
        score = feature_score(name, raw["value"], raw["unit"])
        scores[name] = score
        contributions[name] = WEIGHTS[name] * score
        coverage += WEIGHTS[name]
    total = sum(contributions.values())
    return {
        "scores": scores,
        "contributions": contributions,
        "coverage": coverage,
        "S": total,
        "official_eligible": all(value is not None for value in scores.values()),
        "shadow_only": any(value is None for value in scores.values()),
    }


def forecast_xau(spot, horizon, score):
    if not isfinite(spot) or spot <= 0:
        raise ValueError("spot must be positive")
    if horizon not in (3, 10):
        raise ValueError("unsupported horizon")
    if not isfinite(score) or score < -1.0 or score > 1.0:
        raise ValueError("score must be finite and clipped")
    return spot * exp(AMPLITUDE * sqrt(horizon / 3.0) * score)


def parse_utc(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must include a timezone")
    return parsed.astimezone(timezone.utc)


def _valid_date(value):
    return date.fromisoformat(value)


def snapshot_bytes_match(snapshot_bytes, declared_sha256):
    if not isinstance(snapshot_bytes, (bytes, bytearray)):
        return False
    if not SHA256_RE.fullmatch(declared_sha256 or ""):
        return False
    return hashlib.sha256(bytes(snapshot_bytes)).hexdigest() == declared_sha256.lower()


def validate_issue(cutoff_utc, issued_at_utc, inputs, source_meta,
                   target_sessions, approved_xau_sessions, base_session_date):
    failures = []
    cutoff = parse_utc(cutoff_utc)
    issued = parse_utc(issued_at_utc)
    base_date = _valid_date(base_session_date)
    result = weighted_score(inputs)
    if issued < cutoff:
        failures.append("issued_before_cutoff")
    if base_date > cutoff.date():
        failures.append("base_session_after_cutoff")
    if not result["official_eligible"]:
        failures.append("required_feature_missing")

    for name in WEIGHTS:
        meta = source_meta.get(name, {})
        if not snapshot_bytes_match(meta.get("snapshot_bytes"), meta.get("snapshot_sha", "")):
            failures.append("snapshot_sha256_unbound:" + name)
        for field in ("source_url", "series_id", "observation_date",
                      "release_utc", "fetched_utc"):
            if not meta.get(field):
                failures.append("source_metadata_missing:" + name + ":" + field)
        if meta.get("observation_date"):
            obs_date = _valid_date(meta["observation_date"])
            if obs_date > cutoff.date():
                failures.append("observation_after_cutoff:" + name)
            if obs_date > base_date:
                failures.append("observation_after_base:" + name)
            if name == "ETF" and (cutoff.date() - obs_date).days > 14:
                failures.append("etf_observation_stale")
        released = parse_utc(meta["release_utc"]) if meta.get("release_utc") else None
        fetched = parse_utc(meta["fetched_utc"]) if meta.get("fetched_utc") else None
        if released and released > cutoff:
            failures.append("post_cutoff_release:" + name)
        if released and fetched and fetched < released:
            failures.append("source_fetched_before_release:" + name)
        if fetched and fetched > cutoff:
            failures.append("source_fetched_after_cutoff:" + name)
        if fetched and fetched > issued:
            failures.append("source_fetched_after_issue:" + name)
        if not (released and fetched and released <= fetched <= cutoff <= issued):
            failures.append("source_chronology_invalid:" + name)

    calendar = [_valid_date(item) for item in (approved_xau_sessions or [])]
    if not calendar:
        failures.append("approved_session_calendar_missing")
    if calendar != sorted(calendar) or len(set(calendar)) != len(calendar):
        failures.append("approved_session_calendar_invalid")
    for horizon in (3, 10):
        sessions = target_sessions.get(horizon, [])
        if len(sessions) != horizon or len(set(sessions)) != horizon:
            failures.append("target_session_map_invalid:" + str(horizon))
            continue
        parsed = [_valid_date(item) for item in sessions]
        if parsed != sorted(parsed) or len(set(parsed)) != len(parsed):
            failures.append("target_session_order_invalid:" + str(horizon))
        next_sessions = [item for item in calendar if item > base_date][:horizon]
        if parsed != next_sessions:
            failures.append("target_not_next_calendar_sessions:" + str(horizon))
        if parsed and parsed[0] <= cutoff.date():
            failures.append("target_not_after_cutoff:" + str(horizon))
    return {"eligible": not failures, "failures": failures}


def paired_moving_block_interval(paired_differences):
    """Return the preregistered 95% percentile interval for exactly 20 paired losses.

    Candidate method only: the independent protocol review may reject it before
    any official R02 issue. Three adjacent paired differences form each block.
    """
    values = list(paired_differences)
    if len(values) != 20:
        raise ValueError("primary interval requires exactly 20 paired differences")
    if not all(isfinite(value) for value in values):
        raise ValueError("paired differences must be finite")

    block_length = 3
    replicates = 20000
    seed = 20261123
    rng = random.Random(seed)
    blocks_per_sample = (len(values) + block_length - 1) // block_length
    means = []
    for _ in range(replicates):
        sample = []
        for _ in range(blocks_per_sample):
            start = rng.randrange(0, len(values) - block_length + 1)
            sample.extend(values[start:start + block_length])
        sample = sample[:len(values)]
        means.append(sum(sample) / len(values))
    means.sort()

    def quantile(probability):
        position = probability * (len(means) - 1)
        lower = floor(position)
        upper = min(lower + 1, len(means) - 1)
        fraction = position - lower
        return means[lower] + fraction * (means[upper] - means[lower])

    return {
        "n": len(values),
        "estimate": sum(values) / len(values),
        "lower_95": quantile(0.025),
        "upper_95": quantile(0.975),
        "method": "moving_block_percentile",
        "block_length": block_length,
        "replicates": replicates,
        "seed": seed,
    }


def paired_absolute_error(model_target_key, benchmark_target_key,
                          actual, prediction, benchmark):
    if model_target_key != benchmark_target_key:
        raise ValueError("model and B0 target mismatch")
    if not all(isfinite(value) for value in (actual, prediction, benchmark)):
        raise ValueError("non-finite price")
    return abs(actual - prediction), abs(actual - benchmark)


def local_log_error_parts(actual, predicted):
    xau_a, fx_a, q_a = actual
    xau_p, fx_p, q_p = predicted
    if min(xau_a, fx_a, xau_p, fx_p, 1 + q_a, 1 + q_p) <= 0:
        raise ValueError("prices, FX and 1+q must be positive")
    parts = (
        log(xau_a / xau_p),
        log(fx_a / fx_p),
        log((1 + q_a) / (1 + q_p)),
    )
    total = log((xau_a * fx_a * (1 + q_a)) /
                (xau_p * fx_p * (1 + q_p)))
    return parts, total


def _canonical_payload_bytes(payload):
    if not isinstance(payload, dict):
        raise ValueError("record payload must be an object")
    try:
        return json.dumps(payload, ensure_ascii=False, sort_keys=True,
                          separators=(",", ":"), allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("record payload is not canonical JSON data") from exc


def _valid_record_id(record_id):
    return (isinstance(record_id, str) and
            re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}", record_id) is not None)


def write_immutable_record(directory, payload):
    """Create a content-hashed, write-once record; this detects tampering but cannot prevent it."""
    if not _valid_record_id(payload.get("record_id") if isinstance(payload, dict) else None):
        raise ValueError("record_id must be a safe 1-128 character identifier")
    payload_bytes = _canonical_payload_bytes(payload)
    digest = hashlib.sha256(payload_bytes).hexdigest()
    encoded = json.dumps(
        {"payload": payload, "sha256": digest},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8") + b"\n"
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    target = root / (payload["record_id"] + ".json")
    try:
        descriptor = os.open(str(target), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
    except FileExistsError:
        if target.read_bytes() != encoded:
            raise ValueError("record_id already exists with different bytes")
        return digest
    with os.fdopen(descriptor, "wb") as output:
        output.write(encoded)
        output.flush()
        os.fsync(output.fileno())
    if target.read_bytes() != encoded:
        raise OSError("record readback differs from written bytes")
    read_immutable_record(root, payload["record_id"])
    return digest


def read_immutable_record(directory, record_id):
    if not _valid_record_id(record_id):
        raise ValueError("invalid record_id")
    path = Path(directory) / (record_id + ".json")
    encoded = path.read_bytes()
    try:
        envelope = json.loads(encoded.decode("utf-8"))
        payload = envelope["payload"]
        declared = envelope["sha256"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise ValueError("record envelope is invalid") from exc
    if not isinstance(payload, dict) or payload.get("record_id") != record_id:
        raise ValueError("record identity mismatch")
    actual = hashlib.sha256(_canonical_payload_bytes(payload)).hexdigest()
    if declared != actual:
        raise ValueError("record digest mismatch")
    expected = json.dumps(
        {"payload": payload, "sha256": actual},
        ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False,
    ).encode("utf-8") + b"\n"
    if encoded != expected:
        raise ValueError("record serialization mismatch")
    return payload


def replay_archived_pair(directory, model_record_id, benchmark_record_id, outcome_record_id):
    """Replay one archived M1/B0 pair after verifying immutable record hashes and joins."""
    model = read_immutable_record(directory, model_record_id)
    benchmark = read_immutable_record(directory, benchmark_record_id)
    outcome = read_immutable_record(directory, outcome_record_id)
    if model.get("record_type") != "forecast" or benchmark.get("record_type") != "forecast":
        raise ValueError("model and benchmark records must be forecasts")
    if outcome.get("record_type") != "outcome":
        raise ValueError("joined record must be an outcome")
    if outcome.get("model_record_id") != model_record_id:
        raise ValueError("outcome model reference mismatch")
    if outcome.get("benchmark_record_id") != benchmark_record_id:
        raise ValueError("outcome benchmark reference mismatch")
    join_fields = ("cohort_id", "issue_slot_id", "base_session_id", "target_key")
    for field in join_fields:
        if not model.get(field) or model.get(field) != benchmark.get(field):
            raise ValueError("forecast pair join mismatch:" + field)
    if outcome.get("target_key") != model["target_key"]:
        raise ValueError("outcome target mismatch")
    model_error, benchmark_error = paired_absolute_error(
        model["target_key"], benchmark["target_key"], outcome["actual"],
        model["prediction"], benchmark["prediction"])
    return {
        "cohort_id": model["cohort_id"],
        "issue_slot_id": model["issue_slot_id"],
        "target_key": model["target_key"],
        "model_record_id": model_record_id,
        "benchmark_record_id": benchmark_record_id,
        "outcome_record_id": outcome_record_id,
        "model_absolute_error": model_error,
        "benchmark_absolute_error": benchmark_error,
        "paired_difference": model_error - benchmark_error,
    }


def sample_inputs():
    return {
        "DXY": {"value": 0.0, "unit": "decimal_return"},
        "REAL": {"value": 0.0, "unit": "bp"},
        "MOM": {"value": 0.0, "unit": "decimal_return"},
        "ETF": {"value": 0.0, "unit": "tonnes"},
    }


def sample_meta():
    return {
        name: {
            "snapshot_bytes": ("synthetic-fixture:" + name).encode("ascii"),
            "snapshot_sha": hashlib.sha256(("synthetic-fixture:" + name).encode("ascii")).hexdigest(),
            "source_url": "https://example.invalid/source",
            "series_id": name,
            "observation_date": "2026-11-20",
            "release_utc": "2026-11-20T20:00:00Z",
            "fetched_utc": "2026-11-22T13:59:30Z",
        }
        for name in WEIGHTS
    }


def sample_calendar():
    return ["2026-11-23", "2026-11-24", "2026-11-25", "2026-11-27",
            "2026-11-30", "2026-12-01", "2026-12-02", "2026-12-03",
            "2026-12-04", "2026-12-07"]


class R02VerifierTests(unittest.TestCase):
    def test_weights_sum_to_one(self):
        self.assertTrue(isclose(sum(WEIGHTS.values()), 1.0, abs_tol=1e-12))

    def test_frozen_weight_map_and_feature_contributions(self):
        expected = {"DXY": 0.30, "REAL": 0.35, "MOM": 0.20, "ETF": 0.15}
        self.assertEqual(WEIGHTS, expected)
        result = weighted_score({
            "DXY": {"value": 0.0075, "unit": "decimal_return"},
            "REAL": {"value": 10.0, "unit": "bp"},
            "MOM": {"value": 0.02, "unit": "decimal_return"},
            "ETF": {"value": 20.0, "unit": "tonnes"},
        })
        self.assertEqual(result["contributions"], {
            "DXY": -0.15, "REAL": -0.175, "MOM": 0.10, "ETF": 0.075,
        })

    def test_feature_units_signs_and_clipping(self):
        self.assertEqual(feature_score("DXY", 0.0075, "decimal_return"), -0.5)
        self.assertEqual(feature_score("REAL", 10.0, "bp"), -0.5)
        self.assertEqual(feature_score("MOM", 0.02, "decimal_return"), 0.5)
        self.assertEqual(feature_score("ETF", 20.0, "tonnes"), 0.5)
        self.assertEqual(feature_score("MOM", -0.20, "decimal_return"), -1.0)
        with self.assertRaises(ValueError):
            feature_score("REAL", 0.10, "decimal_return")
        with self.assertRaises(ValueError):
            feature_score("ETF", float("nan"), "tonnes")

    def test_synthetic_full_vector(self):
        raw = {
            "DXY": {"value": 0.0075, "unit": "decimal_return"},
            "REAL": {"value": 10.0, "unit": "bp"},
            "MOM": {"value": 0.02, "unit": "decimal_return"},
            "ETF": {"value": 20.0, "unit": "tonnes"},
        }
        result = weighted_score(raw)
        self.assertAlmostEqual(result["S"], -0.15)
        self.assertAlmostEqual(forecast_xau(2000.0, 3, result["S"]), 1996.103800, places=5)
        self.assertAlmostEqual(forecast_xau(2000.0, 10, result["S"]), 1992.892267, places=5)
        self.assertTrue(result["official_eligible"])

    def test_missing_feature_is_zero_weight_shadow_without_renormalizing(self):
        raw = {
            "DXY": {"value": 0.0075, "unit": "decimal_return"},
            "REAL": None,
            "MOM": None,
            "ETF": None,
        }
        result = weighted_score(raw)
        self.assertAlmostEqual(result["S"], -0.15)
        self.assertAlmostEqual(result["coverage"], 0.30)
        self.assertFalse(result["official_eligible"])
        self.assertTrue(result["shadow_only"])
        mutant_renormalized = result["S"] / result["coverage"]
        self.assertNotAlmostEqual(result["S"], mutant_renormalized)

    def test_issue_accepts_clean_eligible_fixture(self):
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), sample_meta(), targets,
                                sample_calendar(), "2026-11-20")
        self.assertTrue(result["eligible"], result["failures"])
        self.assertEqual(result["failures"], [])

    def test_issue_rejects_unbound_snapshot_bytes(self):
        meta = sample_meta()
        meta["MOM"]["snapshot_bytes"] += b"-mutated"
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), meta, targets,
                                sample_calendar(), "2026-11-20")
        self.assertIn("snapshot_sha256_unbound:MOM", result["failures"])

    def test_issue_rejects_cutoff_chronology_and_future_dates(self):
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        cases = [
            ("fetch_after_cutoff", "ETF", "fetched_utc", "2026-11-22T14:00:30Z", "source_fetched_after_cutoff:ETF"),
            ("fetch_before_release", "DXY", "fetched_utc", "2026-11-20T19:59:59Z", "source_fetched_before_release:DXY"),
            ("observation_after_cutoff", "REAL", "observation_date", "2026-11-23", "observation_after_cutoff:REAL"),
        ]
        for _, feature, field, value, expected in cases:
            with self.subTest(feature=feature, field=field):
                meta = sample_meta()
                meta[feature][field] = value
                result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                        sample_inputs(), meta, targets,
                                        sample_calendar(), "2026-11-20")
                self.assertIn(expected, result["failures"])
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), sample_meta(), targets,
                                sample_calendar(), "2026-11-23")
        self.assertIn("base_session_after_cutoff", result["failures"])

    def test_issue_rejects_observation_after_base(self):
        meta = sample_meta()
        meta["DXY"]["observation_date"] = "2026-11-21"
        meta["DXY"]["release_utc"] = "2026-11-21T20:00:00Z"
        meta["DXY"]["fetched_utc"] = "2026-11-22T13:59:30Z"
        for name in ("REAL", "MOM", "ETF"):
            meta[name]["observation_date"] = "2026-11-20"
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), meta, targets,
                                sample_calendar(), "2026-11-20")
        self.assertEqual(result["failures"], ["observation_after_base:DXY"])

    def test_issue_rejects_stale_etf_observation(self):
        meta = sample_meta()
        for name in WEIGHTS:
            meta[name]["observation_date"] = "2026-11-02"
            meta[name]["release_utc"] = "2026-11-02T20:00:00Z"
            meta[name]["fetched_utc"] = "2026-11-22T13:59:30Z"
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), meta, targets,
                                sample_calendar(), "2026-11-02")
        self.assertEqual(result["failures"], ["etf_observation_stale"])

    def test_issue_rejects_missing_snapshot_and_future_release(self):
        meta = sample_meta()
        meta["ETF"]["release_utc"] = "2026-11-24T00:00:00Z"
        meta["MOM"]["snapshot_sha"] = ""
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), meta, targets,
                                sample_calendar(), "2026-11-20")
        self.assertFalse(result["eligible"])
        self.assertIn("post_cutoff_release:ETF", result["failures"])
        self.assertIn("snapshot_sha256_unbound:MOM", result["failures"])

    def test_issue_rejects_missing_features(self):
        missing = sample_inputs()
        missing["ETF"] = None
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                missing, sample_meta(), targets,
                                sample_calendar(), "2026-11-20")
        self.assertIn("required_feature_missing", result["failures"])

    def test_issue_rejects_bad_target_mapping(self):
        calendar = sample_calendar()
        targets = {3: calendar[1:4], 10: calendar}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), sample_meta(), targets,
                                calendar, "2026-11-20")
        self.assertIn("target_not_next_calendar_sessions:3", result["failures"])

    def test_issue_requires_calendar_and_timezone_aware_timestamps(self):
        with self.assertRaises(ValueError):
            validate_issue("2026-11-22T14:00:00", "2026-11-22T14:01:00Z",
                           sample_inputs(), sample_meta(), {}, None, "2026-11-20")
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), sample_meta(), {}, None, "2026-11-20")
        self.assertIn("approved_session_calendar_missing", result["failures"])

    def test_issue_rejects_fetch_after_issue_and_before_cutoff_issue(self):
        meta = sample_meta()
        meta["ETF"]["fetched_utc"] = "2026-11-22T14:02:00Z"
        targets = {3: sample_calendar()[:3], 10: sample_calendar()}
        result = validate_issue("2026-11-22T14:00:00Z", "2026-11-22T14:01:00Z",
                                sample_inputs(), meta, targets, sample_calendar(), "2026-11-20")
        self.assertIn("source_fetched_after_issue:ETF", result["failures"])
        early = validate_issue("2026-11-22T14:02:00Z", "2026-11-22T14:01:00Z",
                               sample_inputs(), sample_meta(), targets,
                               sample_calendar(), "2026-11-20")
        self.assertIn("issued_before_cutoff", early["failures"])

    def test_archived_pair_replay_joins_and_scores_exact_target(self):
        model = {"record_id": "M1-ISSUE-001", "record_type": "forecast",
                 "cohort_id": "R02-P0", "issue_slot_id": "SLOT-001",
                 "base_session_id": "XAU:2026-11-20",
                 "target_key": "XAU:h3:2026-11-25", "prediction": 100.0}
        benchmark = {**model, "record_id": "B0-ISSUE-001",
                     "prediction": 99.0}
        outcome = {"record_id": "OUT-001", "record_type": "outcome",
                   "model_record_id": "M1-ISSUE-001",
                   "benchmark_record_id": "B0-ISSUE-001",
                   "target_key": "XAU:h3:2026-11-25", "actual": 101.0}
        with tempfile.TemporaryDirectory() as directory:
            for record in (model, benchmark, outcome):
                write_immutable_record(directory, record)
            replay = replay_archived_pair(directory, model["record_id"],
                                          benchmark["record_id"], outcome["record_id"])
            self.assertEqual(replay["model_absolute_error"], 1.0)
            self.assertEqual(replay["benchmark_absolute_error"], 2.0)
            self.assertEqual(replay["paired_difference"], -1.0)

    def test_archived_pair_replay_rejects_mismatched_issue_or_target(self):
        model = {"record_id": "M1-ISSUE-002", "record_type": "forecast",
                 "cohort_id": "R02-P0", "issue_slot_id": "SLOT-002",
                 "base_session_id": "XAU:2026-11-20",
                 "target_key": "XAU:h3:2026-11-25", "prediction": 100.0}
        benchmark = {**model, "record_id": "B0-ISSUE-002",
                     "issue_slot_id": "SLOT-OLD", "prediction": 99.0}
        outcome = {"record_id": "OUT-002", "record_type": "outcome",
                   "model_record_id": "M1-ISSUE-002",
                   "benchmark_record_id": "B0-ISSUE-002",
                   "target_key": "XAU:h3:2026-11-25", "actual": 101.0}
        with tempfile.TemporaryDirectory() as directory:
            for record in (model, benchmark, outcome):
                write_immutable_record(directory, record)
            with self.assertRaisesRegex(ValueError, "issue_slot_id"):
                replay_archived_pair(directory, model["record_id"],
                                     benchmark["record_id"], outcome["record_id"])

    def test_immutable_record_roundtrip_and_duplicate_write(self):
        payload = {"record_id": "R02-M1-ISSUE-001", "kind": "forecast",
                   "target_key": "XAU:h3:2026-12-01", "value": 100.0}
        with tempfile.TemporaryDirectory() as directory:
            first_digest = write_immutable_record(directory, payload)
            second_digest = write_immutable_record(directory, payload)
            self.assertEqual(first_digest, second_digest)
            self.assertEqual(read_immutable_record(directory, payload["record_id"]), payload)
            with self.assertRaises(ValueError):
                write_immutable_record(directory, {**payload, "value": 101.0})

    def test_immutable_record_readback_detects_tampering(self):
        payload = {"record_id": "R02-B0-ISSUE-001", "kind": "benchmark",
                   "target_key": "XAU:h3:2026-12-01", "value": 100.0}
        with tempfile.TemporaryDirectory() as directory:
            write_immutable_record(directory, payload)
            path = Path(directory) / (payload["record_id"] + ".json")
            path.chmod(0o666)
            path.write_bytes(path.read_bytes().replace(b"100.0", b"101.0"))
            with self.assertRaises(ValueError):
                read_immutable_record(directory, payload["record_id"])

    def test_immutable_record_rejects_unsafe_ids_and_nonfinite_json(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                write_immutable_record(directory, {"record_id": "../escape"})
            with self.assertRaises(ValueError):
                write_immutable_record(directory, {"record_id": "bad-nan",
                                                   "value": float("nan")})

    def test_primary_uncertainty_interval_is_reproducible(self):
        differences = [float((index % 5) - 2) for index in range(20)]
        first = paired_moving_block_interval(differences)
        second = paired_moving_block_interval(differences)
        self.assertEqual(first, second)
        self.assertEqual(first["n"], 20)
        self.assertEqual(first["method"], "moving_block_percentile")
        self.assertEqual(first["block_length"], 3)
        self.assertEqual(first["replicates"], 20000)
        self.assertEqual(first["seed"], 20261123)
        self.assertAlmostEqual(first["estimate"], sum(differences) / 20)
        self.assertLessEqual(first["lower_95"], first["upper_95"])

    def test_primary_uncertainty_interval_rejects_bad_cohort(self):
        with self.assertRaises(ValueError):
            paired_moving_block_interval([0.0] * 19)
        with self.assertRaises(ValueError):
            paired_moving_block_interval([0.0] * 19 + [float("nan")])

    def test_paired_score_requires_same_target(self):
        with self.assertRaises(ValueError):
            paired_absolute_error("XAU:h3:2026-11-25", "XAU:h3:2026-11-26", 10, 9, 11)
        self.assertEqual(paired_absolute_error("XAU:h3:2026-11-25",
                                               "XAU:h3:2026-11-25", 10, 9, 11),
                         (1, 1))

    def test_egypt_log_error_decomposition_is_exact(self):
        parts, total = local_log_error_parts(
            (3530.0, 53.8, 0.03), (3500.0, 53.5, 0.02))
        self.assertAlmostEqual(sum(parts), total, places=12)


if __name__ == "__main__":
    unittest.main(verbosity=2)
