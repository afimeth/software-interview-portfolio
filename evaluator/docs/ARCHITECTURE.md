# Architecture and specification trace

Browser form -> loopback HTTP handler -> locked in-memory domain -> JSON response -> textContent rendering.

| Requirement | Implementation | Evidence |
|---|---|---|
| Trim and reject blank/oversized/non-string titles | logic.normalize | Domain.test_trim/blank/type/length |
| Create unique sequential IDs | logic.create | Domain.test_create; HTTP.test_roundtrip; wrong_id mutation |
| Complete known task, reject missing ID | logic.complete; POST route | Domain.test_complete/unknown; HTTP.test_unknown; wrong_completion mutation |
| Reject malformed JSON | server.Handler.do_POST | HTTP.test_malformed |
| Render untrusted text as text | index.html textContent | HTTP.test_page static check; browser behavior unmeasured |
| Admit only contract-preserving patch | evaluate.py fixed temporary copies | correct PASS, three FAIL receipts |
| Avoid guessing an incomplete requirement | missing_spec fixture | ABSTAIN with null score |

Only repository-owned synthetic patches run. Temporary directories isolate files, not privileges. The runner is not suitable for executing hostile submissions.
