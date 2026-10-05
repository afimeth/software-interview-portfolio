# Career Evidence Ledger

Each substantive CV bullet maps to an immutable source ref. MEASURED means recorded test/CI evidence, not production acceptance.

## POW-001 — agent-runtime-recovery-lab (MEASURED)

Implemented a SQLite-backed agent execution fixture with durable dispatch markers, conservative crash recovery, and replay suppression tests.

Source: [b3b2287093ac](https://github.com/afimeth/agent-runtime-recovery-lab/tree/b3b2287093acfc4cefb3e3796f4696d81d78f7e5) · [CI](https://github.com/afimeth/agent-runtime-recovery-lab/actions/runs/37134986507)

Limitations: Synthetic standalone lab; no live model, production scale or independently audited system. See README boundaries.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-001: checkout https://github.com/afimeth/agent-runtime-recovery-lab at b3b2287093acfc4cefb3e3796f4696d81d78f7e5; follow README test/demo commands, inspect CI https://github.com/afimeth/agent-runtime-recovery-lab/actions/runs/37134986507, and compare the safe wording with documented limitations.

## POW-002 — evidence-rag-eval-lab (MEASURED)

Built a deterministic retrieval evaluation harness with extractive citations, source digest verification, abstention fixtures, and adversarial citation tests.

Source: [35920533825b](https://github.com/afimeth/evidence-rag-eval-lab/tree/35920533825bd9f899ce3d25191d2bd9b1fc694d) · [CI](https://github.com/afimeth/evidence-rag-eval-lab/actions/runs/37134994525)

Limitations: Synthetic standalone lab; no live model, production scale or independently audited system. See README boundaries.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-002: checkout https://github.com/afimeth/evidence-rag-eval-lab at 35920533825bd9f899ce3d25191d2bd9b1fc694d; follow README test/demo commands, inspect CI https://github.com/afimeth/evidence-rag-eval-lab/actions/runs/37134994525, and compare the safe wording with documented limitations.

## POW-003 — scoped-tool-gateway-lab (MEASURED)

Implemented a local capability-scoped tool gateway with expiry, atomic usage budgets, denial audit events, and concurrent replay tests.

Source: [3b6e627aa044](https://github.com/afimeth/scoped-tool-gateway-lab/tree/3b6e627aa044e2e0261389da901e43d4f6d71d12) · [CI](https://github.com/afimeth/scoped-tool-gateway-lab/actions/runs/37135003386)

Limitations: Synthetic standalone lab; no live model, production scale or independently audited system. See README boundaries.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-003: checkout https://github.com/afimeth/scoped-tool-gateway-lab at 3b6e627aa044e2e0261389da901e43d4f6d71d12; follow README test/demo commands, inspect CI https://github.com/afimeth/scoped-tool-gateway-lab/actions/runs/37135003386, and compare the safe wording with documented limitations.

## POW-004 — durable-backend-systems-lab (MEASURED)

Built a SQLite transfer API with transactional idempotency, atomic outbox jobs, concurrent overdraft/replay tests, and process-crash rollback verification.

Source: [f015aa654c3a](https://github.com/afimeth/durable-backend-systems-lab/tree/f015aa654c3a216a79a2483aed52073b0fb5fb8d) · [CI](https://github.com/afimeth/durable-backend-systems-lab/actions/runs/37137575754)

Limitations: SQLite single-host writer locking; no PostgreSQL, ORM, migrations beyond initial schema, auth, TLS, tenant isolation, cloud deployment, currency conversion, real accounting compliance, external sink exactly-once guarantee, sustained load, or production operations.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-004: checkout https://github.com/afimeth/durable-backend-systems-lab at f015aa654c3a216a79a2483aed52073b0fb5fb8d; follow README test/demo commands, inspect CI https://github.com/afimeth/durable-backend-systems-lab/actions/runs/37137575754, and compare the safe wording with documented limitations.

## POW-005 — realtime-product-systems-lab (MEASURED)

Built and tested a local async state feed with cursor replay, snapshot recovery, bounded slow-consumer queues, and observable CLI metrics.

Source: [ee0314e2aa27](https://github.com/afimeth/realtime-product-systems-lab/tree/ee0314e2aa275ac5d29a93a61494b9304a8554cd) · [CI](https://github.com/afimeth/realtime-product-systems-lab/actions/runs/37137915377)

Limitations: No WebSocket, ASGI, WebRTC, media transport, browser subscription UI, durable restart state, multi-process fanout, auth/TLS, distributed ordering, or internet deployment. StreamWriter/OS buffering is separate from application queue bounds. Active pre-subscription sockets have a two-second timeout but no global connection cap. Core event objects are trusted in-process data.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-005: checkout https://github.com/afimeth/realtime-product-systems-lab at ee0314e2aa275ac5d29a93a61494b9304a8554cd; follow README test/demo commands, inspect CI https://github.com/afimeth/realtime-product-systems-lab/actions/runs/37137915377, and compare the safe wording with documented limitations.

## POW-006 — workflow-runtime-oss-lab (MEASURED)

Built a Go DAG execution lab with bounded concurrency, adapter contracts, explicit safe retries, cancellation, and conservative journal recovery.

Source: [33df6e7f4e4d](https://github.com/afimeth/workflow-runtime-oss-lab/tree/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6) · [CI](https://github.com/afimeth/workflow-runtime-oss-lab/actions/runs/37137592153)

Limitations: One scheduler owns one journal; no multi-process lock, distributed scheduler, Kubernetes/Argo integration, containers, durable directory fsync on all platforms, leases, remote plugins, untrusted-code isolation, backoff timing, upstream OSS contribution, or production on-call history. Adapters must honor cancellation; a noncooperative adapter can prevent completion. Cancellation does not roll back completed effects. Direct Run callers must bind the workflow spec as the CLI does.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-006: checkout https://github.com/afimeth/workflow-runtime-oss-lab at 33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6; follow README test/demo commands, inspect CI https://github.com/afimeth/workflow-runtime-oss-lab/actions/runs/37137592153, and compare the safe wording with documented limitations.

## POW-007 — solidity-multichain-security-lab (MEASURED)

Built a local Foundry routing-security lab with access-control, replay-domain, slippage and reentrancy tests, fuzz cases, conservation invariants, and gas measurements.

Source: [31f25a16bba6](https://github.com/afimeth/solidity-multichain-security-lab/tree/31f25a16bba671f6bb5347d90e797c0f3a24e92b) · [CI](https://github.com/afimeth/solidity-multichain-security-lab/actions/runs/37137599899)

Limitations: Native-asset local fixture only: no ERC20 quirks, oracle, MEV mitigation, bridge messaging/finality/relayer verification, Yul/assembly, upgrade safety, mainnet/testnet operations, real multi-network deployment, or independent audit. Owner can allow a malicious adapter; user must trust the allowlist policy. Forced donations may remain stuck. Public receive accepts donations. Gas depends on compiler/profile and fixture. The two invariant predicates are grouped by Foundry 1.8.4 into one reported campaign.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-007: checkout https://github.com/afimeth/solidity-multichain-security-lab at 31f25a16bba671f6bb5347d90e797c0f3a24e92b; follow README test/demo commands, inspect CI https://github.com/afimeth/solidity-multichain-security-lab/actions/runs/37137599899, and compare the safe wording with documented limitations.

## POW-008 — design-engineering-product-lab (MEASURED)

Built a responsive React/TypeScript session journal with stateful review/filtering, validated persisted settings, keyboard/modal checks, automated accessibility checks, and a measured asset-size budget.

Source: [4a64601086b2](https://github.com/afimeth/design-engineering-product-lab/tree/4a64601086b2b673031fdc59dd673accdcde45a3) · [CI](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137671237)

Limitations: Synthetic local journal; no brokerage, trading enforcement, backend, auth, financial advice, analytics/conversion uplift, live market data, professional design-tool history, broad browser matrix, manual screen-reader audit or complete WCAG certification. Axe checks cover exercised desktop/modal/mobile states only. Gzip budget is not Core Web Vitals. Unit tests use storage/dialog fixtures; Chromium tests use real browser APIs.

Avoid: Production experience, Independent audit, Years of experience, Employer affiliation, Mainnet ownership.

One-prompt recall: Verify POW-008: checkout https://github.com/afimeth/design-engineering-product-lab at 4a64601086b2b673031fdc59dd673accdcde45a3; follow README test/demo commands, inspect CI https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137671237, and compare the safe wording with documented limitations.

## POW-009 — coding-agent evaluator fixture (MEASURED)

Built an AI-assisted, provider-free full-stack task fixture and deterministic patch-review harness with domain/HTTP regression tests, three rejected mutations, a passing refactor and explicit specification abstention.

Source: [9c21a7afa059](https://github.com/afimeth/software-interview-portfolio/tree/9c21a7afa059a1fe475e94b74f98724366e22827/evaluator) · [CI](https://github.com/afimeth/software-interview-portfolio/actions/runs/37152878281)

Limitations: Fixed synthetic code patches only; no hostile-code sandbox, live model benchmark, browser E2E, production deployment or independent review.

Avoid: Evaluated production coding agents, Measured model quality, Independent reviewer approval.

One-prompt recall: Verify POW-009: checkout https://github.com/afimeth/software-interview-portfolio at 9c21a7afa059a1fe475e94b74f98724366e22827; run python evaluator/evaluate.py and python -m unittest discover -s evaluator/tests (set PYTHONPATH=evaluator); inspect evaluator/docs/REVIEW_RECEIPT.md and explain FAIL versus ABSTAIN.