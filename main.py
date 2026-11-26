#!/usr/bin/env python3
"""The Moon Gets One Star — funniest one-star review of the Moon (<=120 chars).

Writes the winning line to /output/entry.txt. The winner is picked by scoring
10 fresh candidates against the judge's brief, in the brief's own order:
  1. one-star review of the Moon itself (not a trip, a person, somewhere else)
  2. funnier, lands on first read
  3. reads like a real one-star review (rating + grievance)
  4. specific, surprising grievance — NOT craters, cheese, or brightness
  5. every word earns its place; punchline lands before the limit
Weights 5/4/3/2/1, each criterion 1-5, max 75.
"""

CANDIDATES = [
    # 1. The Moon follows you home (the moon-illusion) + it stares and never
    #    blinks + "Reported" — a real-review punchline, Moon-only.
    "One star. It follows me home every night, stares through my window, "
    "and never once blinks. Reported.",
    # 2. Bait-and-switch on the phases: ordered full, got a sliver.
    "One star. Ordered a full moon, got a sliver. It shrinks a little "
    "every night and calls that a cycle.",
    # 3. Moonrise really is ~50 minutes later every day; a late worker.
    "One star. Shows up 50 minutes late every night, never apologises, "
    "and still expects me to look up.",
    # 4. One job, and it takes a week off every month (new moon).
    "One star. It has one job — lighting the night — and takes a week off "
    "every month without telling anyone.",
    # 5. 4.5 billion years old, no updates, still dusty.
    "One star. Four and a half billion years old, zero updates, and it "
    "still hasn't fixed the dust.",
    # 6. Tide-maker that floods the beach and takes a bow.
    "One star. Controls the tides, floods my beach, then takes a bow like "
    "it did me a favour.",
    # 7. The far side: it only ever shows one face. What is it hiding?
    "One star. Only ever shows one side. After all these years, what "
    "exactly is it hiding back there?",
    # 8. Full-moon werewolf neighbour — funny, but the complaint lands on
    #    the neighbour, not the Moon, so it loses on criterion 1.
    "One star. My werewolf neighbour gets loud every full moon and the "
    "Moon just sits there, glowing, unbothered.",
    # 9. The new moon as ghosting: disappears for days, returns unbothered.
    "One star. It disappears for days every month with no explanation, "
    "then comes back like nothing happened.",
    # 10. No atmosphere, no water, no refund — and it bills in lost sleep.
    "One star. No atmosphere, no water, no refund policy — and it still "
    "charges me a full night's sleep.",
]

# Scores per candidate, in the judge's criterion order, 1-5 each.
SCORES = {
    0: (5, 5, 5, 5, 4),  # follows me home / stares / never blinks / Reported
    1: (5, 4, 5, 4, 4),  # full moon ordered, sliver received
    2: (5, 4, 4, 5, 4),  # 50 minutes late every night
    3: (5, 5, 4, 4, 4),  # one job, a week off every month
    4: (5, 4, 4, 3, 4),  # 4.5 billion years, zero updates
    5: (5, 4, 3, 5, 3),  # tides, floods the beach, takes a bow
    6: (5, 4, 4, 5, 4),  # only shows one side, what is it hiding
    7: (3, 4, 3, 4, 4),  # werewolf neighbour (complaint is not the Moon)
    8: (5, 4, 4, 4, 4),  # disappears for days, comes back unbothered
    9: (4, 3, 4, 3, 3),  # no atmosphere, no refund policy
}

WEIGHTS = (5, 4, 3, 2, 1)


def score(idx):
    """Weighted score out of 75 for candidate idx."""
    return sum(w * s for w, s in zip(WEIGHTS, SCORES[idx]))


def ranking():
    """Candidates ranked best-first: (score, index), ties broken by length."""
    return sorted(
        ((score(i), i) for i in range(len(CANDIDATES))),
        key=lambda t: (-t[0], len(CANDIDATES[t[1]])),
    )


# --- Part 2: pick the winner, validate the gate, write the entry. ---

WINNER_INDEX = ranking()[0][1]
WINNER = CANDIDATES[WINNER_INDEX]
WINNER_SCORE = score(WINNER_INDEX)


def main():
    import os

    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space. The winner is 101 characters, one line.
    text = WINNER.strip()
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, gate is 1-120"
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print(f"winner #{WINNER_INDEX} scored {WINNER_SCORE}/75 "
          f"({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
