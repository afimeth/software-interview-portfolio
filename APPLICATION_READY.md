# Application-ready project material

Use these under Projects in a truthful CV. Keep actual employment, education and years unchanged. Review applicant-only declarations yourself. No application was submitted by this work.

## Safe English CV bullets

- Built a SQLite transfer API with transactional idempotency, atomic outbox jobs, concurrent overdraft/replay tests, and process-crash rollback verification. [Repository](https://github.com/afimeth/durable-backend-systems-lab) · [CI](https://github.com/afimeth/durable-backend-systems-lab/actions/runs/37137575754).
- Built and tested a local async state feed with cursor replay, snapshot recovery, bounded slow-consumer queues, and observable CLI metrics. [Repository](https://github.com/afimeth/realtime-product-systems-lab) · [CI](https://github.com/afimeth/realtime-product-systems-lab/actions/runs/37137915377).
- Built a Go DAG execution lab with bounded concurrency, adapter contracts, explicit safe retries, cancellation, and conservative journal recovery. [Repository](https://github.com/afimeth/workflow-runtime-oss-lab) · [CI](https://github.com/afimeth/workflow-runtime-oss-lab/actions/runs/37137592153).
- Built a local Foundry routing-security lab with access-control, replay-domain, slippage and reentrancy tests, fuzz cases, conservation invariants, and gas measurements. [Repository](https://github.com/afimeth/solidity-multichain-security-lab) · [CI](https://github.com/afimeth/solidity-multichain-security-lab/actions/runs/37137599899).
- Built a responsive React/TypeScript session journal with stateful review/filtering, validated persisted settings, keyboard/modal checks, automated accessibility checks, and a measured asset-size budget. [Repository](https://github.com/afimeth/design-engineering-product-lab) · [CI](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137669803).

## Role-specific introduction snippets

### DualEntry backend

I built a local transfer API to make transactional failure boundaries inspectable: idempotency keys bind to request payloads, debit/credit/outbox records commit atomically, concurrent tests prevent overdraft, and an abruptly exiting process leaves no partial debit. The repository includes a HTTP demo, benchmark, exact-commit receipts and Linux/Windows CI. PostgreSQL and cloud deployment are documented follow-up work.

### LiveKit product systems

My portfolio pairs an async state-feed lab with a responsive TypeScript/React product. The state-feed demo exercises reconnect replay, snapshot fallback and slow-consumer limits over real loopback connections; the UI demonstrates review interactions, persisted settings, keyboard focus and automated accessibility checks. These are separate local labs, and the transport is not WebRTC or a LiveKit integration.

### Pipekit OSS/product

I built a Go workflow lab with DAG validation, bounded concurrency, an adapter interface, a persisted journal and explicit safe-retry semantics. Interrupted or ambiguous work holds for reconciliation. The test matrix includes Linux race detection and Go 1.23/1.24 on Linux and Windows. Kubernetes integration and an upstream contribution remain open; I would present this as a local systems project.

### Tradeify design engineering

I designed and built Clearstep, a responsive session-review journal with synthetic trades. A user can filter trades, review decisions and persist a validated risk reminder. The live demo and repository include design rationale, rejected directions, keyboard/modal checks, mobile layout tests, automated accessibility checks and a measured asset budget. AI-assisted development is disclosed in the project.

## Five-minute walkthrough

1. Open the live demo or run the local lab demo.
2. Explain one concrete user problem and one invariant.
3. Show a relevant failure/adversarial test and its CI evidence.
4. Explain one deliberate tradeoff and one remaining gap.
5. Offer to modify a requirement live; do not claim the exercise predicts production success.

## Application ordering

Tradeify: portfolio ready now; rehearse the design decision walkthrough. DualEntry backend and LiveKit: project links ready, but review advertised senior experience against the actual CV. Pipekit: Go project ready for a stretch application; Kubernetes and upstream OSS gaps remain explicit. DualEntry Hardcore and LI.FI: current posting availability was not confirmed, so do not treat old shortlist links as active application targets.

Readiness times in the coverage matrix are planning estimates, not measured interview success. Country-specific employment eligibility and sponsorship must be verified at application time. These materials never substitute project tests for years of experience or applicant attestations.
