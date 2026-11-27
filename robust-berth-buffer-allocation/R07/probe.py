#!/usr/bin/env python3
"""Three-vessel deterministic probe for finite off-berth holding capacity."""
from collections import deque


def simulate(capacity):
    count = 3
    arrivals = [0, 0, 0]
    handling = [1, 1, 1]
    first_channel_entry = 10
    channel_headway = 1

    starts = []
    completions = []
    releases = []
    entries = []
    holding_departures = deque()

    for i in range(count):
        start = arrivals[i] if i == 0 else max(arrivals[i], releases[i - 1])
        completion = start + handling[i]
        previous_entry = entries[i - 1] if i else -10**9
        entry = max(completion, first_channel_entry, previous_entry + channel_headway)

        while holding_departures and holding_departures[0] <= completion:
            holding_departures.popleft()

        if capacity == 0:
            release = entry
        elif len(holding_departures) < capacity:
            release = completion
            holding_departures.append(entry)
        else:
            next_space = holding_departures[0]
            if entry <= next_space:
                release = entry
            else:
                release = next_space
                holding_departures.popleft()
                holding_departures.append(entry)

        starts.append(start)
        completions.append(completion)
        releases.append(release)
        entries.append(entry)

    return starts, completions, releases, entries


for capacity in range(4):
    starts, completions, releases, entries = simulate(capacity)
    print(
        "K=" + str(capacity)
        + ": starts=" + str(starts)
        + "; handling_complete=" + str(completions)
        + "; berth_release=" + str(releases)
        + "; channel_entry=" + str(entries)
        + "; C3_le_3=" + str(completions[2] <= 3)
    )
print("capacities=4; vessels=3; deterministic_integer_times=1")
