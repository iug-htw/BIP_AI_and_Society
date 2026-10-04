"""Send one local image to an OpenAI-compatible vision model.

Set HTW_API_KEY, HTW_BASE_URL and optionally HTW_VISION_MODEL.
Never commit real credentials to GitHub.
"""

import base64
import mimetypes
import os
from openai import OpenAI

API_KEY = os.environ.get("HTW_API_KEY")
BASE_URL = os.environ.get("HTW_BASE_URL")
MODEL = os.environ.get("HTW_VISION_MODEL", "qwen3.8-27b")

if not API_KEY or not BASE_URL:
    raise RuntimeError("Set HTW_API_KEY and HTW_BASE_URL before running this script.")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
image_path = input("Enter the path to your image: ").strip()
mime_type, _ = mimetypes.guess_type(image_path)
mime_type = mime_type or "image/jpeg"

with open(image_path, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Describe this image in detail. Mention the main objects, people, text, and other visually relevant information.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:{mime_type};base64,{image_base64}"},
                },
            ],
        }
    ],
)
print(response.choices[0].message.content)
