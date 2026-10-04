# AI-Assisted Programming Workshop

A beginner workshop built around a small Python data-quality checker. The emphasis is not on generating as much code as possible, but on maintaining control over what the program should do and how correctness is demonstrated.

## Learning outcomes

Students should be able to:
1. translate an idea into explicit, observable requirements;
2. ask an AI coding assistant for one small implementation step;
3. run code and inspect actual behaviour;
4. derive tests from requirements rather than from existing output;
5. debug by separating diagnosis from repair;
6. stop, simplify, revert, or ask for explanation when they no longer understand the system.

## Exercise structure

The exercise uses one CSV file and six requirements: read the file, count rows, detect missing values, detect exact duplicates, validate opening years, and validate passenger values. `PROJECT_BRIEF.md` is the source of truth; `TESTS.md` defines expected results; `PROMPTS.md` contains bounded prompts for the incremental build.

The workshop rule is: **one functional change → run → test → only then continue**.

## Files

- `slides/AI_Assisted_Programming_Workshop_VSCode.pdf` — complete workshop slides.
- `exercise/README_SETUP.md` — pre-workshop setup.
- `exercise/PROJECT_BRIEF.md` — project requirements and constraints.
- `exercise/TESTS.md` — acceptance tests and regression rule.
- `exercise/PROMPTS.md` — staged Copilot prompts.
- `exercise/stations_workshop.csv` — intentionally imperfect dataset.
- `exercise/main.py` — intentionally minimal starting file.
