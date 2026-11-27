#!/usr/bin/env python3
"""Two-vessel illustration of berth release versus outbound channel slots."""
from math import inf


def simulate(blocked_at_berth):
    arrivals = [0, 0]
    handling = [1, 1]
    earliest_channel_slot = [10, 0]
    channel_headway = 1
    gaps = [0, 0]

    starts = []
    completions = []
    berth_releases = []
    channel_entries = []

    for i in range(2):
        if i == 0:
            start = arrivals[i]
            previous_channel_entry = -inf
        else:
            start = max(arrivals[i], berth_releases[i - 1] + gaps[i])
            previous_channel_entry = channel_entries[i - 1]

        completion = start + handling[i]
        channel_entry = max(
            completion,
            earliest_channel_slot[i],
            previous_channel_entry + channel_headway,
        )
        berth_release = channel_entry if blocked_at_berth else completion

        starts.append(start)
        completions.append(completion)
        berth_releases.append(berth_release)
        channel_entries.append(channel_entry)

    return starts, completions, berth_releases, channel_entries


for label, blocked in (
    ("clear_then_wait_elsewhere", False),
    ("remain_on_berth_until_slot", True),
):
    starts, completions, releases, entries = simulate(blocked)
    print(
        label
        + ": starts=" + str(starts)
        + "; handling_complete=" + str(completions)
        + "; berth_release=" + str(releases)
        + "; channel_entry=" + str(entries)
        + "; C2_le_3=" + str(completions[1] <= 3)
    )
print("scenarios=2; vessels=2; deterministic_integer_times=1")
