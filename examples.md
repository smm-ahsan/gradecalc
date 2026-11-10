# GradeCalc — Examples

Real runs, copied from actual output.

## Example 1: What do I need on the rest of the course?

```bash
python3 gradecalc.py --item "Midterm:70:40" --item "Assignment:90:20" --target 80
```

Output:

```
Midterm: 70 (weight 40%)
Assignment: 90 (weight 20%)
Completed weight: 60%
Points banked: 46.0
Current average on completed work: 76.7
To finish at 80, you need an average of 85.0 on the remaining 40%.
```

The midterm (70 at 40% weight) and assignment (90 at 20% weight) bank
46.0 points between them. To finish at the target of 80, the remaining
40% of the course has to average 85.0.

## Example 2: When a target is out of reach

```bash
python3 gradecalc.py --item "Quiz:50:10" --target 100
```

Output:

```
Quiz: 50 (weight 10%)
Completed weight: 10%
Points banked: 5.0
Current average on completed work: 50.0
Target 100 is no longer reachable - you would need 105.6 on the remaining 90%.
```

Scoring 50 on a quiz worth 10% banks only 5.0 points, so a perfect 100
overall would need an impossible 105.6 average on everything left.
GradeCalc says so plainly instead of letting you hope.
