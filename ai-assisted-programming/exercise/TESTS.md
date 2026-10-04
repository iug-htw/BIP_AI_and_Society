# Acceptance tests

The expected results below are derived from PROJECT_BRIEF.md and from manually inspecting `stations_workshop.csv` before running the program.

| Test | Requirement | Expected result |
|---|---|---|
| T1 | REQ-1 | `stations_workshop.csv` can be read without an error. |
| T2 | REQ-2 | 8 data rows are reported. |
| T3 | REQ-3 | 2 missing cells are reported: Wittenau / `daily_passengers`, and the blank `station` cell. |
| T4 | REQ-4 | 1 exact duplicate row is reported: the second Alexanderplatz/U5/1930/85000 row. |
| T5 | REQ-5 | 1 invalid non-missing year is reported: 2035. |
| T6 | REQ-6 | 2 invalid non-missing passenger values are reported: -500 and `eight thousand`. |

## Regression rule
After every change, rerun all tests for requirements that were already implemented. Do not change an expected result merely because the program produces a different result.
