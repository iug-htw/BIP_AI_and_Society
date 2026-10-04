# OCR Fundamentals

A practical introduction to OCR with PaddleOCR. The module frames OCR as a small machine-learning workflow: collect/prepare input, run inference, preserve evidence, compare against ground truth, analyse errors, and iterate.

## Main concepts

- PaddleOCR combines pretrained models for text detection and recognition, with optional orientation and document preprocessing.
- Raw OCR output should be preserved as evidence. Useful evidence includes recognized text, polygon coordinates, confidence, source, and engine.
- Preprocessing can improve or damage recognition. Variants should therefore be evaluated against the same ground truth instead of being assumed to help.
- Postprocessing should remain traceable and reversible rather than silently overwriting raw OCR output.
- Ground truth provides the reference for repeatable evaluation.
- Precision, recall, and F1 make detection quality measurable once the matching rule and positive class are defined.
- Large document images may need orientation correction and overlapping tiling so small text is not lost through downscaling.

## Setup

The examples use Python 3.11 and a dedicated virtual environment on Windows:

```powershell
python -m venv C:\venvs\paddleocr
C:\venvs\paddleocr\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r examples\requirements.txt
```

Run the examples in order:

```powershell
python examples\01_paddleocr_basic.py
python examples\02_paddleocr_export.py
python examples\03_paddleocr_evidence.py
python examples\04_paddleocr_tile.py
```

## Example progression

1. `01_paddleocr_basic.py` — smallest working OCR call and raw printed result.
2. `02_paddleocr_export.py` — exports PaddleOCR JSON and visualization.
3. `03_paddleocr_evidence.py` — creates a reduced evidence representation with text, confidence, and coordinates.
4. `04_paddleocr_tile.py` — handles a larger TIFF: classify page orientation once, rotate the complete image, choose an overlapping tile layout, run OCR per tile, translate coordinates back to page space, and merge overlapping duplicate detections.

## Inputs

- `example.png` — small synthetic OCR example.
- `00000018.TIF` — larger document example used by the tiling workflow.
- `slides/OCR_Fundamentals_EN_v7.pptx` — full instructional slide deck.
