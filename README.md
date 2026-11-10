# GradeCalc

A tiny command-line tool that works out your weighted grade so far and tells you exactly what average you still need to finish at your target.

## How it works

Every piece of coursework is worth a slice of your final grade. GradeCalc adds up the points you have already banked from finished work, shows your current average on that work, and then works backwards from a target grade to tell you what you need on everything that is left.

A mini example: your midterm is worth 40% of the final grade and you scored 70, and an assignment worth 20% scored 90. That banks 46.0 points (28 from the midterm, 18 from the assignment) out of the 60% of the course you have completed, a current average of 76.7. If you want to finish at 80 overall, you need an average of 85.0 on the remaining 40% of the course. GradeCalc prints exactly that, and it also tells you honestly when a target is already secured or no longer reachable.

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

```bash
python3 gradecalc.py --item "Midterm:70:40" --item "Assignment:90:20" --target 80
python3 gradecalc.py --item "Quiz:50:10" --target 100
```

Each `--item` is `name:score:weight` — the name of the work, your score out of 100, and how many percent of the final grade it is worth. Repeat `--item` as many times as you need. `--target` is optional; leave it off to just see your current standing.

Scores must be between 0 and 100 and the weights cannot add up to more than 100. Bad input exits with a clear error message and code 2.

## License

MIT — see [LICENSE](LICENSE).
