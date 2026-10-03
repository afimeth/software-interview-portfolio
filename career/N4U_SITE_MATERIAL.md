# Website-ready proof cards

Prepared for n4u.tech; not deployed. Public product demo remains on GitHub Pages.

## POW-001

**Problem:** Ambiguous crash outcomes cause unsafe replay.

**Built:** Implemented a SQLite-backed agent execution fixture with durable dispatch markers, conservative crash recovery, and replay suppression tests.

[Repo](https://github.com/afimeth/agent-runtime-recovery-lab) Â· [Source](https://github.com/afimeth/agent-runtime-recovery-lab/tree/b3b2287093acfc4cefb3e3796f4696d81d78f7e5) Â· [Tests/CI](https://github.com/afimeth/agent-runtime-recovery-lab/actions/runs/37134986507) Â· [Demo/run](https://github.com/afimeth/agent-runtime-recovery-lab/blob/b3b2287093acfc4cefb3e3796f4696d81d78f7e5/README.md)

**Limitations:** Synthetic standalone lab; no live model, production scale or independently audited system. See README boundaries.

## POW-002

**Problem:** Retrieval answers need inspectable citation evidence.

**Built:** Built a deterministic retrieval evaluation harness with extractive citations, source digest verification, abstention fixtures, and adversarial citation tests.

[Repo](https://github.com/afimeth/evidence-rag-eval-lab) Â· [Source](https://github.com/afimeth/evidence-rag-eval-lab/tree/35920533825bd9f899ce3d25191d2bd9b1fc694d) Â· [Tests/CI](https://github.com/afimeth/evidence-rag-eval-lab/actions/runs/37134994525) Â· [Demo/run](https://github.com/afimeth/evidence-rag-eval-lab/blob/35920533825bd9f899ce3d25191d2bd9b1fc694d/README.md)

**Limitations:** Synthetic standalone lab; no live model, production scale or independently audited system. See README boundaries.

## POW-003

**Problem:** Tools need bounded capabilities and denial evidence.

**Built:** Implemented a local capability-scoped tool gateway with expiry, atomic usage budgets, denial audit events, and concurrent replay tests.

[Repo](https://github.com/afimeth/scoped-tool-gateway-lab) Â· [Source](https://github.com/afimeth/scoped-tool-gateway-lab/tree/3b6e627aa044e2e0261389da901e43d4f6d71d12) Â· [Tests/CI](https://github.com/afimeth/scoped-tool-gateway-lab/actions/runs/37135003386) Â· [Demo/run](https://github.com/afimeth/scoped-tool-gateway-lab/blob/3b6e627aa044e2e0261389da901e43d4f6d71d12/README.md)

**Limitations:** Synthetic standalone lab; no live model, production scale or independently audited system. See README boundaries.

## POW-004

**Problem:** Duplicate requests must not cause partial transfers.

**Built:** Built a SQLite transfer API with transactional idempotency, atomic outbox jobs, concurrent overdraft/replay tests, and process-crash rollback verification.

[Repo](https://github.com/afimeth/durable-backend-systems-lab) Â· [Source](https://github.com/afimeth/durable-backend-systems-lab/tree/f015aa654c3a216a79a2483aed52073b0fb5fb8d) Â· [Tests/CI](https://github.com/afimeth/durable-backend-systems-lab/actions/runs/37137575754) Â· [Demo/run](https://github.com/afimeth/durable-backend-systems-lab/blob/f015aa654c3a216a79a2483aed52073b0fb5fb8d/README.md)

**Limitations:** SQLite single-host writer locking; no PostgreSQL, ORM, migrations beyond initial schema, auth, TLS, tenant isolation, cloud deployment, currency conversion, real accounting compliance, external sink exactly-once guarantee, sustained load, or production operations.

## POW-005

**Problem:** Slow consumers and missed state need bounded recovery.

**Built:** Built and tested a local async state feed with cursor replay, snapshot recovery, bounded slow-consumer queues, and observable CLI metrics.

[Repo](https://github.com/afimeth/realtime-product-systems-lab) Â· [Source](https://github.com/afimeth/realtime-product-systems-lab/tree/ee0314e2aa275ac5d29a93a61494b9304a8554cd) Â· [Tests/CI](https://github.com/afimeth/realtime-product-systems-lab/actions/runs/37137915377) Â· [Demo/run](https://github.com/afimeth/realtime-product-systems-lab/blob/ee0314e2aa275ac5d29a93a61494b9304a8554cd/README.md)

**Limitations:** No WebSocket, ASGI, WebRTC, media transport, browser subscription UI, durable restart state, multi-process fanout, auth/TLS, distributed ordering, or internet deployment. StreamWriter/OS buffering is separate from application queue bounds. Active pre-subscription sockets have a two-second timeout but no global connection cap. Core event objects are trusted in-process data.

## POW-006

**Problem:** Workflow failures require safe retry and cancellation.

**Built:** Built a Go DAG execution lab with bounded concurrency, adapter contracts, explicit safe retries, cancellation, and conservative journal recovery.

[Repo](https://github.com/afimeth/workflow-runtime-oss-lab) Â· [Source](https://github.com/afimeth/workflow-runtime-oss-lab/tree/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6) Â· [Tests/CI](https://github.com/afimeth/workflow-runtime-oss-lab/actions/runs/37137592153) Â· [Demo/run](https://github.com/afimeth/workflow-runtime-oss-lab/blob/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6/README.md)

**Limitations:** One scheduler owns one journal; no multi-process lock, distributed scheduler, Kubernetes/Argo integration, containers, durable directory fsync on all platforms, leases, remote plugins, untrusted-code isolation, backoff timing, upstream OSS contribution, or production on-call history. Adapters must honor cancellation; a noncooperative adapter can prevent completion. Cancellation does not roll back completed effects. Direct Run callers must bind the workflow spec as the CLI does.

## POW-007

**Problem:** Route adapters can violate asset and replay boundaries.

**Built:** Built a local Foundry routing-security lab with access-control, replay-domain, slippage and reentrancy tests, fuzz cases, conservation invariants, and gas measurements.

[Repo](https://github.com/afimeth/solidity-multichain-security-lab) Â· [Source](https://github.com/afimeth/solidity-multichain-security-lab/tree/31f25a16bba671f6bb5347d90e797c0f3a24e92b) Â· [Tests/CI](https://github.com/afimeth/solidity-multichain-security-lab/actions/runs/37137599899) Â· [Demo/run](https://github.com/afimeth/solidity-multichain-security-lab/blob/31f25a16bba671f6bb5347d90e797c0f3a24e92b/README.md)

**Limitations:** Native-asset local fixture only: no ERC20 quirks, oracle, MEV mitigation, bridge messaging/finality/relayer verification, Yul/assembly, upgrade safety, mainnet/testnet operations, real multi-network deployment, or independent audit. Owner can allow a malicious adapter; user must trust the allowlist policy. Forced donations may remain stuck. Public receive accepts donations. Gas depends on compiler/profile and fixture. The two invariant predicates are grouped by Foundry 1.8.4 into one reported campaign.

## POW-008

**Problem:** A review journal needs usable persistent state.

**Built:** Built a responsive React/TypeScript session journal with stateful review/filtering, validated persisted settings, keyboard/modal checks, automated accessibility checks, and a measured asset-size budget.

[Repo](https://github.com/afimeth/design-engineering-product-lab) Â· [Source](https://github.com/afimeth/design-engineering-product-lab/tree/4a64601086b2b673031fdc59dd673accdcde45a3) Â· [Tests/CI](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137671237) Â· [Demo/run](https://afimeth.github.io/design-engineering-product-lab/)

**Limitations:** Synthetic local journal; no brokerage, trading enforcement, backend, auth, financial advice, analytics/conversion uplift, live market data, professional design-tool history, broad browser matrix, manual screen-reader audit or complete WCAG certification. Axe checks cover exercised desktop/modal/mobile states only. Gzip budget is not Core Web Vitals. Unit tests use storage/dialog fixtures; Chromium tests use real browser APIs.

## POW-009

**Problem:** Patches can pass a happy path while silently breaking a contract.

**Built:** Built an AI-assisted, provider-free full-stack task fixture and deterministic patch-review harness with domain/HTTP regression tests, three rejected mutations, a passing refactor and explicit specification abstention.

[Repo](https://github.com/afimeth/software-interview-portfolio) Â· [Source](https://github.com/afimeth/software-interview-portfolio/tree/9c21a7afa059a1fe475e94b74f98724366e22827/evaluator) Â· [Tests/CI](https://github.com/afimeth/software-interview-portfolio/actions/runs/37152878281) Â· [Demo/run](https://github.com/afimeth/software-interview-portfolio/tree/9c21a7afa059a1fe475e94b74f98724366e22827/evaluator)

**Limitations:** Fixed synthetic code patches only; no hostile-code sandbox, live model benchmark, browser E2E, production deployment or independent review.