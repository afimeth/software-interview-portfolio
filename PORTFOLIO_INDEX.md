# Source and CI evidence index

**Review date: 8 October 2026.** Source revisions below are the portfolio's recorded snapshots, not a claim that every current branch head was re-audited. Test totals are repository-reported. CI job conclusions were retrieved again for the eight lab test runs.

[Portfolio](README.md) · [Assessment and limitations](EVALUATION.md) · [Machine-readable review](EVALUATION.json)

| Project / pinned source | Reported checks | Test CI | Rechecked jobs |
|---|---:|---|---:|
| [agent-runtime-recovery-lab](https://github.com/afimeth/agent-runtime-recovery-lab/tree/b3b2287093acfc4cefb3e3796f4696d81d78f7e5) · `b3b2287093ac` | 10 | [Recorded run](https://github.com/afimeth/agent-runtime-recovery-lab/actions/runs/37134986507) | 4 success |
| [evidence-rag-eval-lab](https://github.com/afimeth/evidence-rag-eval-lab/tree/35920533825bd9f899ce3d25191d2bd9b1fc694d) · `35920533825b` | 11 | [Recorded run](https://github.com/afimeth/evidence-rag-eval-lab/actions/runs/37134994525) | 4 success |
| [scoped-tool-gateway-lab](https://github.com/afimeth/scoped-tool-gateway-lab/tree/3b6e627aa044e2e0261389da901e43d4f6d71d12) · `3b6e627aa044` | 9 | [Recorded run](https://github.com/afimeth/scoped-tool-gateway-lab/actions/runs/37135003386) | 4 success |
| [workflow-runtime-oss-lab](https://github.com/afimeth/workflow-runtime-oss-lab/tree/33df6e7f4e4d77791becc0cb6fe2c41f39b9dff6) · `33df6e7f4e4d` | 17 | [Recorded run](https://github.com/afimeth/workflow-runtime-oss-lab/actions/runs/37137592153) | 4 success |
| [durable-backend-systems-lab](https://github.com/afimeth/durable-backend-systems-lab/tree/f015aa654c3a216a79a2483aed52073b0fb5fb8d) · `f015aa654c3a` | 16 | [Recorded run](https://github.com/afimeth/durable-backend-systems-lab/actions/runs/37137575754) | 4 success |
| [realtime-product-systems-lab](https://github.com/afimeth/realtime-product-systems-lab/tree/ee0314e2aa275ac5d29a93a61494b9304a8554cd) · `ee0314e2aa27` | 15 | [Recorded run](https://github.com/afimeth/realtime-product-systems-lab/actions/runs/37137915377) | 4 success |
| [solidity-multichain-security-lab](https://github.com/afimeth/solidity-multichain-security-lab/tree/31f25a16bba671f6bb5347d90e797c0f3a24e92b) · `31f25a16bba6` | 16 | [Recorded run](https://github.com/afimeth/solidity-multichain-security-lab/actions/runs/37137599899) | 4 success |
| [design-engineering-product-lab](https://github.com/afimeth/design-engineering-product-lab/tree/4a64601086b2b673031fdc59dd673accdcde45a3) · `4a64601086b2` | 11 | [Recorded run](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137669803) | 4 success |

**32 recorded test jobs rechecked; 105 reported checks.** Repeating the same suite across operating systems/toolchains does not produce additional unique tests. Foundry groups two invariant predicates into one campaign; fuzz iterations are not counted as independent tests.

## Product demo: deployment is separate evidence

[Static demo](https://afimeth.github.io/design-engineering-product-lab/) · [Deployment run 37137671237](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137671237) · [Test CI run 37137669803](https://github.com/afimeth/design-engineering-product-lab/actions/runs/37137669803)

Both runs identify source commit `4a64601086b2b673031fdc59dd673accdcde45a3`. The deployment run has two successful jobs (build/deploy); the test run has four successful Linux/Windows jobs. The previous table linked the deployment run in the CI column. This correction changes the link and its interpretation, not the underlying source or historical receipt.

## Additional evaluator

[Coding-agent evaluator source](https://github.com/afimeth/software-interview-portfolio/tree/9c21a7afa059a1fe475e94b74f98724366e22827/evaluator) · [Repository-recorded CI](https://github.com/afimeth/software-interview-portfolio/actions/runs/37152878281) · [Run guide](evaluator/README.md)

The evaluator documentation reports 12 unit/integration checks and five deterministic patch/spec cases. Its README was read in this review; its implementation, run metadata and test results were not independently rechecked. It is therefore excluded from the 32-job verification total above.

## Reading the evidence

The source/run associations, except for the directly checked product test/deployment pairing, were taken from the existing portfolio index. All eight listed test runs had four successful jobs when queried. Full checkout logs, every uploaded receipt and independent source/run binding were not reverified for all eight projects.

[Original machine-readable receipt](PORTFOLIO_RECEIPT.json) · [Claim registry](career/CLAIM_REGISTRY.md) · [Application packs](career/APPLICATION_PACKS.md)
