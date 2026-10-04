# OpenAI-Compatible HTW / Local Model Examples

Small teaching examples for calling an OpenAI-compatible model endpoint from Python.

## Security first

Do not place an API key directly in Python source code. The examples read configuration from environment variables:

```powershell
$env:HTW_API_KEY="your-key"
$env:HTW_BASE_URL="https://your-endpoint.example/v1"
$env:HTW_VISION_MODEL="your-vision-model-id"
```

## Examples

- `examples/test_htw_api.py` — lists available models, sends a basic chat request, and demonstrates streaming.
- `examples/test_htw_vision.py` — base64-encodes a local image and sends it to a vision-capable model.
- `examples/test_bvg.jpg` — sample image for the vision example.

The exact endpoint URL, key, and available model IDs depend on the infrastructure used in class.
