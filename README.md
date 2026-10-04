# Engineering Evidence Index

Small, runnable public engineering fixtures covering durable backend behavior, async product systems, workflow runtimes, Solidity security, product implementation, and applied-AI failure boundaries.

This repository is an evidence/navigation layer, not a product showcase. The useful unit is a reproducible claim bound to code, fixtures, tests, receipts, provenance, and explicit limitations.

[Full coverage matrix](PORTFOLIO_COVERAGE.md) · [Exact evidence receipt](PORTFOLIO_RECEIPT.json) · [Application-ready project bullets](APPLICATION_READY.md) · [Live product demo](https://afimeth.github.io/design-engineering-product-lab/)

All eight lab heads have successful Linux/Windows CI matrices (32 jobs). The five newly built labs contribute 75 reported checks; the three existing labs contribute 30. Foundry groups two invariant predicates into one campaign, and fuzz iterations are not inflated into separate tests.

## Evidence contract

- **Engineer-readable first.** A reviewer should be able to identify the mechanism, inputs, outputs, tests, evidence, and limitations without relying on marketing prose.
- **Machine-readable where useful.** Receipts, fixtures, measurements, and stable identifiers should prefer structured data.
- **Meaning before encoding.** Human input may originate in any language or compressed form. Preserve source input; represent canonical semantics structurally; project to English, Go-like syntax, CJK/other compact relay forms, or model-specific encodings only as needed.
- **Headless runtime first.** Click-to-run means a stable runtime entrypoint, not a required UI. Interfaces are optional projections over the same runtime contract.
- **Claims follow evidence.** Passing tests prove only the tested behavior. Producer-run measurements, CI, independent review, and production evidence remain distinct.
- **No public secrets.** Use synthetic fixtures, mock providers, schemas, and environment placeholders rather than credentials or private data.

See [EVIDENCE_CONTRACT.md](EVIDENCE_CONTRACT.md) for the compact repository contract.

## Start here

- Backend: [transactional transfer API](https://github.com/afimeth/durable-backend-systems-lab).
- Product systems: [async state feed](https://github.com/afimeth/realtime-product-systems-lab) and [responsive React journal](https://github.com/afimeth/design-engineering-product-lab).
- Workflow/runtime: [Go DAG execution](https://github.com/afimeth/workflow-runtime-oss-lab).
- EVM security: [Foundry router fixture](https://github.com/afimeth/solidity-multichain-security-lab).
- Applied AI: [crash recovery](https://github.com/afimeth/agent-runtime-recovery-lab), [citation evaluation](https://github.com/afimeth/evidence-rag-eval-lab), [scoped tools](https://github.com/afimeth/scoped-tool-gateway-lab).

Each lab provides English architecture/run/test material for engineer review while allowing its machine-facing representation to remain implementation-specific. This index is not a ninth implementation lab. Validate evidence consistency with `python scripts/validate.py`.

Fresh AI-assisted work with synthetic data. Public role-family requirements inform practice scenarios; no employer endorsement or actual take-home question is claimed. Projects demonstrate local capability and do not establish historical experience, production adoption, mainnet ownership or independent audit credentials.

## Role-specific career evidence

[Public portfolio index](PORTFOLIO_INDEX.md) · [Coding-agent/full-stack fixture](evaluator/README.md) · [Claim registry](career/CLAIM_REGISTRY.md) · [Application packs](career/APPLICATION_PACKS.md) · [CV A](career/CV_A.md) · [CV B](career/CV_B.md) · [CV C](career/CV_C.md) · [n4u.tech-ready cards](career/N4U_SITE_MATERIAL.md).

Run `python scripts/career_verify.py` for 12 additional unit/integration checks and five deterministic patch/spec cases. The original eight labs remain unchanged.
