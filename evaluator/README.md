# Coding-agent review and full-stack fixture

Run from the repository root: `python scripts/career_verify.py`. Run the local web app with `python evaluator/server.py --port 8080`, then open http://127.0.0.1:8080. No model key or dependencies are required.

The task board implements title validation, creation and completion across domain logic, HTTP routes and browser UI. Twelve unit/integration checks cover malformed input, unknown IDs and the create/complete/list roundtrip. The evaluation harness applies three broken patches and one correct refactor to isolated temporary copies, executes the same suite and records the diff, output, exit code and rubric decision. A fifth case abstains because the specification is incomplete. Fixtures are generated from the exact source in `evaluate.py`; their patch bytes and digest are in the generated receipt.

Review the exact diff and failing assertion, explain the root cause, propose the smallest fix, rerun the same test, and state remaining uncertainty. Tests score contract compliance; human review covers maintainability and ambiguity. This is AI-assisted synthetic portfolio work, not historical employer work or a live model benchmark.

See [architecture](docs/ARCHITECTURE.md), [limitations](docs/LIMITATIONS.md), [scenarios](docs/INTERVIEW_SCENARIOS.md), and [review receipt](docs/REVIEW_RECEIPT.md).
