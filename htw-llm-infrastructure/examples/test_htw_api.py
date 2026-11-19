"""Minimal test of an OpenAI-compatible HTW-hosted language-model endpoint.

Set HTW_API_KEY and HTW_BASE_URL in the environment before running.
Never commit real credentials to GitHub.
"""

import os
import time
from openai import (
    OpenAI,
    APIConnectionError,
    AuthenticationError,
    RateLimitError,
    APITimeoutError,
    APIStatusError,
)

API_KEY = os.environ.get("HTW_API_KEY")
BASE_URL = os.environ.get("HTW_BASE_URL")
model = "MODELNAME"

if not API_KEY or not BASE_URL:
    raise RuntimeError("Set HTW_API_KEY and HTW_BASE_URL before running this script.")

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
    timeout=120.0,
    max_retries=0,
)


def main() -> None:
    print("=" * 60)
    print("HTW OPENAI-COMPATIBLE API TEST")
    print("=" * 60)

    print(f"\nUsing model: {model}")

    print("\n[2] Chat completion...")
    start = time.time()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for HTW Berlin students."},
            {"role": "user", "content": "Explain what generative AI is in three short sentences."},
        ],
        temperature=0.2,
    )
    print(response.choices[0].message.content)
    print(f"Response time: {time.time() - start:.2f} seconds")
    if response.usage:
    print("\nToken usage:")
    print(f"Input tokens:  {response.usage.prompt_tokens}")
    print(f"Output tokens: {response.usage.completion_tokens}")
    print(f"Total tokens:  {response.usage.total_tokens}")

    print("\n[3] Streaming...")
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Write a short two-sentence description of Berlin."}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
