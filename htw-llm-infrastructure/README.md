# OpenAI-Compatible HTW / Local Model Examples

Small teaching examples for calling an OpenAI-compatible model endpoint from Python.

## Security first

Do not place an API key directly in Python source code. The examples read configuration from environment variables:

### Windows (PowerShell)

```powershell
$env:HTW_API_KEY="your-key"
$env:HTW_BASE_URL="https://your-endpoint.example/v1"
$env:HTW_TEXT_MODEL="your-text-model-id"
$env:HTW_VISION_MODEL="your-vision-model-id"
```

### macOS and Linux (Bash/Zsh)

```bash
export HTW_API_KEY="your-key"
export HTW_BASE_URL="https://your-endpoint.example/v1"
export HTW_TEXT_MODEL="your-text-model-id"
export HTW_VISION_MODEL="your-vision-model-id"
```

Use the endpoint URL, API key and model IDs provided by your instructor.

HTW_TEXT_MODEL is optional. If not set, the text example uses the first model returned by the server.

HTW_VISION_MODEL must identify a vision-capable model.

Run the Python scripts in the same terminal in which
you set the environment variables.

## Installation

Make sure Python 3.10 or newer is installed.

Open a terminal in the htw-llm-infrastructure directory.

Install the required Python package:

```bash
python -m pip install -r requirements.txt
```


## Examples

- `examples/test_htw_api.py` — lists available models, sends a basic chat request, and demonstrates streaming.
- `examples/test_htw_vision.py` — base64-encodes a local image and sends it to a vision-capable model.
- `examples/test_bvg.jpg` — sample image for the vision example.

The exact endpoint URL, key, and available model IDs depend on the infrastructure used in class.

## Running the examples

### Text generation

```bash
python examples/test_htw_api.py
```

The script demonstrates:

- Listing available models
- Selecting a model
- Sending a chat completion request
- Measuring response time
- Inspecting token usage
- Streaming generated text
- Measuring time to first text

### Image understanding

```bash
python examples/test_htw_vision.py
```

Press Enter to use the provided sample image or enter
the path to another local image.

The script demonstrates:

- Encoding an image in Base64
- Sending a multimodal request
- Generating an image description
- Measuring response time and token usage
