# Engineering assessment and limitations

**Dondi · Arif Anıl Dondurmacı**  
**Review date:** 8 October 2026  
**Method:** owner-requested, AI-assisted documentation/source inspection and GitHub CI readback. This is not an independent security audit, certification, hiring decision or live coding assessment.

[Portfolio](README.md) · [Pinned evidence](PORTFOLIO_INDEX.md) · [Machine-readable assessment](EVALUATION.json)

## Assessment in brief

The portfolio contains implemented engineering work, not just architecture proposals. The strongest demonstrated thread is controlled execution: explicit state transitions, conservative recovery, scoped invocation, testable constraints and evidence-bound outputs. Product UI and local EVM security projects add breadth, with their own narrower evidence boundaries.

The appropriate conclusion is **implemented, inspectable proof of work with recorded cross-platform test evidence**. It is neither “only an idea” nor proof of production scale, audit accreditation or universal reliability. The private New4 product's readiness is a separate question and was not used to downgrade or upgrade the public labs.

## 1. What was actually reviewed

The profile and portfolio landing pages, the pinned index, all eight lab READMEs, the evaluator README and `scripts/validate.py` were read. Implementation inspection covered `app.py` in recovery, retrieval evaluation, scoped gateway and transactional backend; `main.go`, `runtime.go` and `runtime_test.go` in the Go workflow lab were also read.

GitHub returned four successful test jobs for each of the eight selected lab runs: **32 in total**. The product's separate deployment run returned two successful jobs and is not included in that total. The product test/deployment metadata was inspected to establish that both refer to the same recorded commit.

A local clone was attempted but the review container could not resolve `github.com`. Repository test suites were therefore **not rerun locally**. Readback of existing CI results is not a new execution. Full CI logs, all archived artifacts, every source file, the evaluator's CI, and current native-machine behavior were not reviewed. For seven labs, source/run pairing comes from the existing portfolio index rather than a fresh checkout-log audit.

## 2. Evaluation rubric

This review uses evidence categories, not a numerical grade for the person.

| Dimension | Evidence that supports a claim | What is insufficient |
|---|---|---|
| Implementation | Inspectable code that expresses the mechanism | A README, diagram or tool list alone |
| Behavioral validation | Assertions and recorded execution of relevant tests | A green badge without knowing the tested scope |
| Reproducibility | Pinned source, commands, fixtures and environment information | A screenshot or an unversioned success statement |
| Operational maturity | Deployment, monitoring, recovery and load evidence for the target | Extrapolating a local fixture to production |
| Claim discipline | Mechanism, observation and limitation kept together | Treating one lab's limits as the author's global limits |

`SOURCE_INSPECTED` means the named files were read, not exhaustively audited. `CI_JOBS_RECHECKED` means GitHub's job/step conclusions were observed. `DOCUMENTED` means a repository claim was read without independently reproducing it. `NOT_ESTABLISHED` means this review lacks evidence; it does not mean incapability or nonexistence.

## 3. Per-project findings

### 1. Agent runtime recovery

**Evidence status:** `SOURCE_INSPECTED + CI_JOBS_RECHECKED`. [agent-runtime-recovery-lab](https://github.com/afimeth/agent-runtime-recovery-lab/tree/b3b2287093acfc4cefb3e3796f4696d81d78f7e5)

**Supported mechanism:** Durable dispatch markers, conservative recovery and replay suppression.

**Evaluation:** [app.py](https://github.com/afimeth/agent-runtime-recovery-lab/blob/b3b2287093acfc4cefb3e3796f4696d81d78f7e5/app.py) · [Recorded test run](https://github.com/afimeth/agent-runtime-recovery-lab/actions/runs/37134986507). The index reports 10 checks; four CI job conclusions were rechecked.

**Boundary:** Local fixture adapters; injected exceptions, not a measured power-loss or distributed exactly-once guarantee.

**Useful next evaluation:** Exercise a real subprocess interruption and reconcile an adapter outcome without blindly retrying. This is a proposed extension, not a newly executed test or a confirmed defect.

### 2. Retrieval evaluation

**Evidence status:** `SOURCE_INSPECTED + CI_JOBS_RECHECKED`. [evidence-rag-eval-lab](https://github.com/afimeth/evidence-rag-eval-lab/tree/35920533825bd9f899ce3d25191d2bd9b1fc694d)

**Supported mechanism:** Deterministic lexical retrieval, citation binding, abstention and adversarial fixtures.

**Evaluation:** [app.py](https://github.com/afimeth/evidence-rag-eval-lab/blob/35920533825bd9f899ce3d25191d2bd9b1fc694d/app.py) · [Recorded test run](https://github.com/afimeth/evidence-rag-eval-lab/actions/runs/37134994525). The index reports 11 checks; four CI job conclusions were rechecked.

**Boundary:** No embeddings, reranker or live LLM; fixture scores do not estimate real-world answer accuracy.

**Useful next evaluation:** Add held-out queries with irrelevant-but-valid citations and report precision separately from source binding. This is a proposed extension, not a newly executed test or a confirmed defect.

### 3. Scoped tool gateway

**Evidence status:** `SOURCE_INSPECTED + CI_JOBS_RECHECKED`. [scoped-tool-gateway-lab](https://github.com/afimeth/scoped-tool-gateway-lab/tree/3b6e627aa044e2e0261389da901e43d4f6d71d12)

**Supported mechanism:** Tool scope, expiry and atomic usage reservation with explicit denial and outcome audit.

**Evaluation:** [app.py](https://github.com/afimeth/scoped-tool-gateway-lab/blob/3b6e627aa044e2e0261389da901e43d4f6d71d12/app.py) · [Recorded test run](https://github.com/afimeth/scoped-tool-gateway-lab/actions/runs/37135003386). The index reports 9 checks; four CI job conclusions were rechecked.

**Boundary:** Trusted in-process callers; not an authenticated network service, MCP server or OS sandbox.

**Useful next evaluation:** Add an authenticated broker boundary and verify expiry, revocation and concurrent budget consumption there. This is a proposed extension, not a newly executed test or a confirmed defect.

### 4. Go workflow runtime

**Evidence status:** `SOURCE_INSPECTED + CI_JOBS_RECHECKED`. [workflow-runtime-oss-lab](https://github.com/afimeth/workflow-runtime-oss-lab/tree/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6)

**Supported mechanism:** DAG validation, bounded concurrency, explicit safe retries, cancellation and journal recovery.

**Evaluation:** [main.go](https://github.com/afimeth/workflow-runtime-oss-lab/blob/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6/main.go) · [runtime.go](https://github.com/afimeth/workflow-runtime-oss-lab/blob/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6/runtime.go) · [runtime_test.go](https://github.com/afimeth/workflow-runtime-oss-lab/blob/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6/runtime_test.go) · [Recorded test run](https://github.com/afimeth/workflow-runtime-oss-lab/actions/runs/37137592153). The index reports 17 checks; four CI job conclusions were rechecked.

**Boundary:** Single scheduler/journal; adapters must cooperate with cancellation; no distributed scheduling or universal power-loss guarantee.

**Useful next evaluation:** Inject journal-write failures during concurrent execution and check worker joining and persisted/in-memory state agreement. This is a proposed extension, not a newly executed test or a confirmed defect.

### 5. Transactional backend

**Evidence status:** `SOURCE_INSPECTED + CI_JOBS_RECHECKED`. [durable-backend-systems-lab](https://github.com/afimeth/durable-backend-systems-lab/tree/f015aa654c3a216a79a2483aed52073b0fb5fb8d)

**Supported mechanism:** Payload-bound idempotency, atomic debit/credit/outbox and exclusive job claims.

**Evaluation:** [app.py](https://github.com/afimeth/durable-backend-systems-lab/blob/f015aa654c3a216a79a2483aed52073b0fb5fb8d/app.py) · [Recorded test run](https://github.com/afimeth/durable-backend-systems-lab/actions/runs/37137575754). The index reports 16 checks; four CI job conclusions were rechecked.

**Boundary:** Single-host SQLite; the demonstration sink shares the transaction. No external-sink exactly-once, tenant auth or accounting certification.

**Useful next evaluation:** Move the sink outside the transaction and test lost acknowledgement, deduplication retention and reconciliation. This is a proposed extension, not a newly executed test or a confirmed defect.

### 6. Realtime product state

**Evidence status:** `DOCUMENTED + CI_JOBS_RECHECKED`. [realtime-product-systems-lab](https://github.com/afimeth/realtime-product-systems-lab/tree/ee0314e2aa275ac5d29a93a61494b9304a8554cd)

**Supported mechanism:** Sequence-numbered state feed, cursor replay, snapshot fallback and slow-consumer eviction.

**Evaluation:** [README](https://github.com/afimeth/realtime-product-systems-lab/blob/ee0314e2aa275ac5d29a93a61494b9304a8554cd/README.md) · [Recorded test run](https://github.com/afimeth/realtime-product-systems-lab/actions/runs/37137915377). The index reports 15 checks; four CI job conclusions were rechecked.

**Boundary:** Loopback TCP JSON-lines, not WebSockets; state is not durable across restart and transport buffering is outside the application queue bound.

**Useful next evaluation:** Add restart persistence and an explicit total-connection limit; measure slow-consumer behavior end to end. This is a proposed extension, not a newly executed test or a confirmed defect.

### 7. EVM security mechanisms

**Evidence status:** `DOCUMENTED + CI_JOBS_RECHECKED`. [solidity-multichain-security-lab](https://github.com/afimeth/solidity-multichain-security-lab/tree/31f25a16bba671f6bb5347d90e797c0f3a24e92b)

**Supported mechanism:** Local routing-security tests for allowlists, replay domains, slippage, reentrancy and invariants.

**Evaluation:** [README](https://github.com/afimeth/solidity-multichain-security-lab/blob/31f25a16bba671f6bb5347d90e797c0f3a24e92b/README.md) · [Recorded test run](https://github.com/afimeth/solidity-multichain-security-lab/actions/runs/37137599899). The index reports 16 checks; four CI job conclusions were rechecked.

**Boundary:** Native-asset fixture, not a deployed multichain bridge or independent security audit. The allowlist owner remains trusted.

**Useful next evaluation:** Extend adversarial adapter cases and obtain an independent review before any deployment claim. This is a proposed extension, not a newly executed test or a confirmed defect.

### 8. Product interface

**Evidence status:** `DOCUMENTED + CI_JOBS_RECHECKED`. [design-engineering-product-lab](https://github.com/afimeth/design-engineering-product-lab/tree/4a64601086b2b673031fdc59dd673accdcde45a3)

**Supported mechanism:** Responsive session journal with persisted settings, interaction tests, axe checks and an asset-size budget.

**Evaluation:** [README](https://github.com/afimeth/design-engineering-product-lab/blob/4a64601086b2b673031fdc59dd673accdcde45a3/README.md) · [Recorded test run](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137669803). The index reports 11 checks; four CI job conclusions were rechecked.

**Boundary:** Synthetic local data; exercised Chromium/axe checks are not complete accessibility certification, broad browser coverage or live financial integration.

**Useful next evaluation:** Add manual keyboard/screen-reader review and a second browser engine; measure field performance separately from bundle size. This is a proposed extension, not a newly executed test or a confirmed defect.

## 4. What the inspected mechanisms show

**Recovery:** dispatch state is persisted before entering the adapter, and a compare-and-set prevents two contenders from taking that path. A failure can deliberately leave the outcome uncertain rather than pretending no effect occurred. The ID is derived from the task payload: identical payloads are treated as the same intent. Supporting two intentionally distinct identical requests would need an explicit identity contract.

**Retrieval:** `app.py` ranks by lexical token overlap and verifies exact citation text and digest. Its fixture evaluation uses recall at two and an abstention case. Citation binding is not semantic entailment; the check does not establish that a source is true or that every included citation is relevant. A future eval should keep precision, recall, answer quality and source binding separate.

**Scoped tools:** the gateway checks scope, expiry, arguments and remaining budget under a lock, reserving usage before dispatch. This is substantive boundary logic, while fixture admission and mutable in-process grant storage deliberately stop short of an authenticated service or security sandbox.

**Go workflows:** the inspected tests include graph rejection, bounded concurrency, safe-retry behavior, ambiguous-failure HOLD, completed-work suppression, cancellation, corrupt/null journal rejection and specification mismatch. These are relevant failure-oriented tests. They do not exhaust all schedules, storage failures or noncooperative adapters.

**Backend:** idempotency is bound to the payload and transaction; debit, credit and outbox creation commit together. Completion in the demo also writes to a sink in the same database transaction. That is a valid local atomicity demonstration, not a guarantee for an independent external service.

## 5. Traceability correction

The original `PORTFOLIO_INDEX.md` linked product run **37137671237** under test CI. It is the successful static deployment (build/deploy), not the test matrix. The actual four-job test run for the same commit is **37137669803**. The revised index separates them. This is an evidence-label/link correction; no test failure was inferred, and no historical receipt was overwritten.

## 6. Limits of the overall evaluation

The work is disclosed as AI-assisted. Repository artifacts alone cannot separate every human-authored line from generated code or measure unaided live coding ability. The useful follow-up is a technical walkthrough, a bounded change and a failure diagnosis—not guessing competence from authorship assumptions.

Synthetic fixtures are controlled and reproducible, but their selection is not an independent test set. Thirty-two successful matrix jobs represent repeated test execution across environments, not 32 independent audits. The reported 105 checks are a suite inventory, not coverage or a probability of correctness. The additional evaluator has five controlled cases, not a model leaderboard.

Production traffic, sustained load, multi-tenant operation, incident response, independent security review, broad accessibility conformance and live external integrations are not established by this inspection. Those are scope limits on these artifacts. The review does not infer employment tenure, degree, seniority, salary, hiring probability or general intelligence from repository counts.

## 7. How to evaluate Dondi further

For AI systems and developer tools, start with recovery, gateway and retrieval evaluation; ask for a real-adapter extension with a lost-acknowledgement case. For backend/workflow work, use the Go runtime and transactional outbox; ask for a concurrent persistence-failure diagnosis. For product engineering, review the journal and reconnecting state feed together. Web3 review should remain scoped to the local contract and its adversarial assumptions.

These are evidence-led review paths, not endorsements or claims that every adjacent production requirement is already met. A reviewer can inspect a mechanism, change a constraint, run the suite and discuss the residual gap.

---

This document evaluates the public artifacts at the listed snapshots. It does not publish private New4 source or establish private-product acceptance. Historical evidence remains available in [PORTFOLIO_RECEIPT.json](PORTFOLIO_RECEIPT.json); this review is an additional, explicitly bounded interpretation.
