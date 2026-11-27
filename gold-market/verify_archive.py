#!/usr/bin/env python3
"""Verify imported Gold Lab artifacts against Git blob identities.
Run with python3 -I verify_archive.py. Standard library only; no network access.
This checks archive integrity, not market claims, old forecasts, or model skill.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def git_blob_sha1(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def main():
    manifest = json.loads((ROOT / "source_manifest.json").read_text(encoding="utf-8"))
    entries = manifest["artifacts"]
    for entry in entries:
        path = ROOT / entry["path"]
        if not path.is_file():
            raise SystemExit("MISSING: " + entry["path"])
        if git_blob_sha1(path.read_bytes()) != entry["expected_git_blob_sha1"]:
            raise SystemExit("BLOB_MISMATCH: " + entry["path"])
    print("verified_artifacts=" + str(len(entries)))
    print("copied_source_blobs=" + str(manifest["counts"]["copied_source_blobs"]))
    print("verbatim_issue_records=" + str(manifest["counts"]["verbatim_issue_records"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
