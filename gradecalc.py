#!/usr/bin/env python3
"""GradeCalc - weighted grade calculator.

Enter the work you have already completed (its score and how much of
the final grade it is worth) and GradeCalc tells you your current
standing and, if you give it a target grade, what average you need on
the work that is still left.

Standard library only.
"""

import argparse
import sys


def fmt(value):
    """Print whole numbers without a decimal point, others as given."""
    if float(value).is_integer():
        return str(int(value))
    return str(value)


def parse_item(raw, parser):
    parts = raw.split(":")
    if len(parts) != 3:
        parser.error(
            "bad --item format: %r (expected 'name:score:weight')" % raw
        )
    name = parts[0].strip()
    if not name:
        parser.error("bad --item format: %r (name is empty)" % raw)
    try:
        score = float(parts[1])
        weight = float(parts[2])
    except ValueError:
        parser.error(
            "bad --item format: %r (score and weight must be numbers)" % raw
        )
    if not 0 <= score <= 100:
        parser.error(
            "score for %r must be between 0 and 100 (got %s)"
            % (name, fmt(score))
        )
    if weight < 0:
        parser.error(
            "weight for %r cannot be negative (got %s)" % (name, fmt(weight))
        )
    return name, score, weight


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="gradecalc.py",
        description="Weighted grade calculator: see your current standing "
                    "and what you still need to hit your target grade.",
    )
    parser.add_argument(
        "--item",
        action="append",
        default=[],
        metavar="NAME:SCORE:WEIGHT",
        help="a completed piece of work, e.g. --item \"Midterm:70:40\" "
             "(score 0-100, weight = percent of the final grade). "
             "Repeatable.",
    )
    parser.add_argument(
        "--target",
        type=float,
        default=None,
        help="the overall grade you want to finish with, e.g. --target 80",
    )
    args = parser.parse_args(argv)

    items = [parse_item(raw, parser) for raw in args.item]

    total_weight = sum(w for _, _, w in items)
    if total_weight > 100 + 1e-9:
        parser.error(
            "total weight is %s%% - weights cannot add up to more than 100%%"
            % fmt(total_weight)
        )

    banked = sum(s * w / 100 for _, s, w in items)

    for name, score, weight in items:
        print("%s: %s (weight %s%%)" % (name, fmt(score), fmt(weight)))
    print("Completed weight: %s%%" % fmt(total_weight))
    print("Points banked: %.1f" % banked)

    if total_weight == 0:
        print("No completed work yet - add items with scores to see "
              "where you stand.")
        return 0

    average = banked / total_weight * 100
    print("Current average on completed work: %.1f" % average)

    if args.target is None:
        return 0

    target = args.target
    remaining = 100 - total_weight
    if remaining <= 0:
        met = banked >= target
        print(
            "Final grade: %.1f - target %s %s."
            % (banked, fmt(target), "met" if met else "not met")
        )
        return 0

    needed = (target - banked) / remaining * 100
    if needed <= 0:
        print("Target already secured on completed work.")
    elif needed > 100:
        print(
            "Target %s is no longer reachable - you would need %.1f "
            "on the remaining %s%%."
            % (fmt(target), needed, fmt(remaining))
        )
    else:
        print(
            "To finish at %s, you need an average of %.1f "
            "on the remaining %s%%."
            % (fmt(target), needed, fmt(remaining))
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
