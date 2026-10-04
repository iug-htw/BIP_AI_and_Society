# Security notes

- Never commit API keys, access tokens, passwords, or cookies.
- Keep real values in environment variables or a local `.env` file that is ignored by Git.
- If a credential has ever been placed in a file that may have been shared or committed, revoke/rotate it rather than merely deleting it from the latest version.
- Before pushing, search the repository for likely secrets, e.g. `sk-`, `api_key=`, `token=`, and `password=`.
