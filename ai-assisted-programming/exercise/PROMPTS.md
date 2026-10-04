# Workshop prompts

## 0. Check context
Read PROJECT_BRIEF.md. Do not edit any files. List the six requirement IDs and explain REQ-2 in one sentence.

## 1. Build v0.1
Read PROJECT_BRIEF.md first.
Implement only REQ-1 and REQ-2 in main.py.
Use Python's standard library only.
Read stations_workshop.csv from the same folder and print the number of data rows.
Do not implement REQ-3 to REQ-6 yet.
Keep the code beginner-readable.
Before editing, tell me in 3 bullets what you plan to change.

## 2. Add missing-value detection
The current program satisfies REQ-1 and REQ-2.
Read PROJECT_BRIEF.md and TESTS.md again.
Implement ONLY REQ-3 in main.py.
Report the total number of missing cells and list the CSV row number and column name for each missing cell.
Do not implement duplicate, year or passenger validation yet.
Preserve REQ-1 and REQ-2.
Before changing code, state the expected result for our supplied CSV.

## 3. Add duplicate detection
Read PROJECT_BRIEF.md and TESTS.md.
Implement ONLY REQ-4.
Detect exact duplicate rows, report how many duplicate rows exist and identify them.
Preserve REQ-1 to REQ-3.
Before editing, state the expected result for T4.

## 4. Add validation
Read PROJECT_BRIEF.md and TESTS.md.
Implement REQ-5 and REQ-6 only.
Validate only non-missing values.
Preserve REQ-1 to REQ-4.
Before editing, state the expected results for T5 and T6.

## 5. Diagnose before fixing
The program has produced the following error or wrong result:
[PASTE THE EXACT ERROR OR OUTPUT]
Do not change any code yet.
Explain:
1. what happened,
2. which requirement is affected,
3. the most likely cause,
4. the smallest possible fix,
5. which existing tests must be rerun afterwards.

## 6. Additional tests
Read PROJECT_BRIEF.md and TESTS.md.
Our supplied CSV already gives one acceptance test for each requirement.
Propose up to five ADDITIONAL edge cases that could expose bugs.
For each case state: the requirement, input condition, expected result, and why the existing dataset would not catch the bug.
Do not modify main.py yet.
