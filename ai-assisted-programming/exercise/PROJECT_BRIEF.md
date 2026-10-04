# Project brief: CSV data-quality checker

We are building a very small Python program. The learner has no prior programming experience. Keep the code simple and explain each change.

## Requirements
- REQ-1: Read `stations_workshop.csv` from the same project folder.
- REQ-2: Report the number of data rows. The header does not count.
- REQ-3: Report missing cells, including CSV row number and column name.
- REQ-4: Report exact duplicate rows.
- REQ-5: For non-missing `year_opened` values, flag values that are not integers from 1900 through 2026.
- REQ-6: For non-missing `daily_passengers` values, flag values that are not numeric or are less than or equal to zero.

## Constraints
- Use only Python's standard library. Do not install external packages.
- Work incrementally.
- Implement only the requirement(s) requested in the current step.
- Preserve behaviour that already passed its tests.
- Explain the plan before editing code.
