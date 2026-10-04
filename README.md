# AI, Programming, and OCR — Instructional Materials

Teaching materials for introductory, hands-on work with AI-assisted programming, OCR, and local/OpenAI-compatible model infrastructure. The repository is designed for students who may have little or no prior programming experience.

## Repository overview

| Module | Focus | Main materials |
|---|---|---|
| `ai-assisted-programming/` | Programming with AI for complete beginners | Workshop slides, project brief, prompts, tests, CSV exercise |
| `ocr-fundamentals/` | OCR as a small machine-learning workflow | OCR slides, PaddleOCR examples, synthetic image, large-document tiling example |
| `htw-llm-infrastructure/` | Minimal API and vision examples | OpenAI-compatible API scripts and a sample image |

## Core teaching idea

The materials use a common control principle: **specify → build → run → test → diagnose → iterate**. AI can draft code or suggest changes, but requirements, expected results, testing, and judgement remain with the learner.

### 1. AI-assisted programming

The workshop introduces VS Code and GitHub Copilot through one deliberately small CSV data-quality project. Learners first turn an idea into explicit requirements, then ask the AI for one bounded implementation step at a time. The supplied acceptance tests make expected behaviour explicit before code is changed.

Key concepts:
- explicit requirements as the source of truth;
- one functional change at a time;
- expected vs. actual results;
- regression testing after every change;
- diagnosis before repair;
- recognising when the learner no longer understands the system.

Start with [`ai-assisted-programming/exercise/README_SETUP.md`](ai-assisted-programming/exercise/README_SETUP.md).

### 2. OCR fundamentals

The OCR module treats optical character recognition as an auditable machine-learning workflow rather than a single function call. Students work from image input through OCR evidence, preprocessing/postprocessing, ground truth, and evaluation.

Key concepts:
- text detection and recognition with PaddleOCR;
- virtual environments and reproducible setup;
- raw OCR evidence: text, position, confidence, and source;
- preprocessing risks and controlled comparison;
- ground truth and repeatable evaluation;
- precision, recall, and F1;
- orientation correction and overlapping tiles for large document images.

Start with [`ocr-fundamentals/README.md`](ocr-fundamentals/README.md).

### 3. HTW / local model infrastructure

The infrastructure examples show the minimum mechanics of calling an OpenAI-compatible endpoint for text and vision. Credentials are intentionally **not** stored in the repository; they must be supplied through environment variables.

Start with [`htw-llm-infrastructure/README.md`](htw-llm-infrastructure/README.md).

## Suggested teaching sequence

1. Begin with the AI-assisted programming workshop to establish specification, incremental development, testing, and debugging habits.
2. Move to OCR to apply those habits to a concrete AI/ML pipeline with measurable outputs and ground truth.
3. Use the infrastructure examples when students need to understand how local or institutional models are accessed programmatically.

## Notes

- Generated OCR outputs are ignored by Git so that raw teaching inputs remain separate from derived evidence.
- No software license has been added. Add one before publishing if reuse beyond the course should be permitted.
- Do not commit API keys, tokens, passwords, or other credentials.
