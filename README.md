<h1 align="center">Engineering Portfolio</h1>
<p align="center"><strong>Dondi · Arif Anıl Dondurmacı</strong></p>
<p align="center">AI systems · Durable workflows · Backend and product engineering</p>
<p align="center"><a href="PORTFOLIO_INDEX.md">Source &amp; CI index</a> · <a href="EVALUATION.md">Evaluation &amp; limitations</a> · <a href="APPLICATION_READY.md">Project summaries</a> · <a href="https://afimeth.github.io/design-engineering-product-lab/">Product demo</a></p>

---

Eight runnable public labs, plus a coding-agent evaluation fixture. Each isolates a concrete engineering problem and exposes the implementation, failure tests, run instructions and limits.

**Start with a mechanism—not a claim about seniority or a list of tools.**

## Choose a review path

| Focus | Start here | What to examine |
|---|---|---|
| **AI systems / agent tooling** | [Recovery](https://github.com/afimeth/agent-runtime-recovery-lab) → [scoped tools](https://github.com/afimeth/scoped-tool-gateway-lab) → [retrieval eval](https://github.com/afimeth/evidence-rag-eval-lab) | Uncertain outcomes, permission boundaries and evidence quality. |
| **Backend / workflow engineering** | [Go runtime](https://github.com/afimeth/workflow-runtime-oss-lab) → [transactional backend](https://github.com/afimeth/durable-backend-systems-lab) | Concurrency, retry contracts, idempotency and recovery. |
| **Product / developer experience** | [Interface](https://github.com/afimeth/design-engineering-product-lab) → [state feed](https://github.com/afimeth/realtime-product-systems-lab) → [patch evaluator](evaluator/README.md) | Stateful UI, reconnect behavior and contract-based review. |
| **Web3 engineering** | [Solidity lab](https://github.com/afimeth/solidity-multichain-security-lab) | Replay domains, adversarial adapters and local invariants. |

## Implemented projects

| Project | Stack | Inspectable mechanism |
|---|---|---|
| **[Agent runtime recovery](https://github.com/afimeth/agent-runtime-recovery-lab)** | Python · SQLite | Durable dispatch markers, conservative recovery and replay suppression. |
| **[Retrieval evaluation](https://github.com/afimeth/evidence-rag-eval-lab)** | Python | Deterministic lexical retrieval, citation binding, abstention and adversarial fixtures. |
| **[Scoped tool gateway](https://github.com/afimeth/scoped-tool-gateway-lab)** | Python | Tool scope, expiry and atomic usage reservation with explicit denial and outcome audit. |
| **[Go workflow runtime](https://github.com/afimeth/workflow-runtime-oss-lab)** | Go | DAG validation, bounded concurrency, explicit safe retries, cancellation and journal recovery. |
| **[Transactional backend](https://github.com/afimeth/durable-backend-systems-lab)** | Python · SQLite | Payload-bound idempotency, atomic debit/credit/outbox and exclusive job claims. |
| **[Realtime product state](https://github.com/afimeth/realtime-product-systems-lab)** | Python · asyncio | Sequence-numbered state feed, cursor replay, snapshot fallback and slow-consumer eviction. |
| **[EVM security mechanisms](https://github.com/afimeth/solidity-multichain-security-lab)** | Solidity · Foundry | Local routing-security tests for allowlists, replay domains, slippage, reentrancy and invariants. |
| **[Product interface](https://github.com/afimeth/design-engineering-product-lab)** | TypeScript · React · Playwright | Responsive session journal with persisted settings, interaction tests, axe checks and an asset-size budget. |

These are separate implementations, not eight deployments of New4. This repository is the navigation and evaluation layer, not an additional runtime lab.

## Evidence, without inflated claims

The [pinned index](PORTFOLIO_INDEX.md) identifies eight source revisions. On **8 October 2026**, a bounded review rechecked **32 successful Linux/Windows CI jobs** across their eight referenced test runs. It also distinguished the product demo's separate two-job deployment run from its four-job test matrix. These are recorded CI results, not fresh local test executions or permanent claims about current branch heads.

The existing index reports **105 checks** across the eight lab suites. Counts describe the recorded suites—not test coverage, independent confirmations or a capability score. The evaluator adds **12 reported checks and five controlled patch/specification cases**; its CI was not rechecked in the 8 October review. Repeated matrix runs and fuzz iterations do not become additional unique tests.

**[Read the per-project assessment and review limits →](EVALUATION.md)** · [Machine-readable review](EVALUATION.json) · [Original detailed receipt](PORTFOLIO_RECEIPT.json)

## Coding-agent evaluation fixture

The [fixture](evaluator/README.md) combines a small task-board application with a patch-evaluation harness: three deliberately broken patches, one correct refactor and one incomplete-specification case. It records diffs, test outcomes and rubric decisions. This demonstrates evaluation plumbing; it is not a benchmark of live model performance.

```sh
# Run from this repository's root after cloning it.
python scripts/validate.py
python scripts/career_verify.py
```

The first command validates the original portfolio receipt's internal consistency. The second exercises the evaluator. Neither is a substitute for inspecting the linked source and CI evidence.

## Scope and provenance

The labs are AI-assisted engineering work with synthetic data. They demonstrate implemented mechanisms and documented failure behavior. Production adoption, independent security audits, employment history, seniority and performance at scale require separate evidence. A limitation on one lab does not invalidate the other repositories—or prove that the author cannot work beyond that lab's scope.

The private New4U / Orkestral product is separate. No private corpus, credentials or proprietary source is part of this public evaluation.

<details>
<summary><strong>Further evidence and application materials</strong></summary>

[Coverage matrix](PORTFOLIO_COVERAGE.md) · [Claim registry](career/CLAIM_REGISTRY.md) · [Application packs](career/APPLICATION_PACKS.md) · [CV A](career/CV_A.md) · [CV B](career/CV_B.md) · [CV C](career/CV_C.md) · [Website cards](career/N4U_SITE_MATERIAL.md)

These are supporting materials, not independent endorsements. Role-specific interpretation remains distinct from the underlying source and test evidence.

</details>

---

[GitHub profile](https://github.com/afimeth) · [n4u.tech](https://n4u.tech) · [Email](mailto:anildondurmaci2@gmail.com)
