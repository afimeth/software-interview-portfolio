# Code review record

Status: author/self-review, not independent approval. Scope: domain logic, HTTP routes, HTML UI and fixed patch harness.

Review findings: mutation tests expose silent completion acknowledgement, invalid sequential IDs and blank admission. HTTP integration verifies the route/domain contract. UI renders task titles with textContent. Fixed mutations execute only trusted owned code; temporary copies are not a sandbox. Unknown priority semantics produce ABSTAIN, with null score and no executed patch. Restart persistence and browser automation are explicit gaps.

Reproduce: `python scripts/career_verify.py`. Its JSON receipt binds the exact commit, actual test count, each patch diff/digest, process output and unsupported claims. A dirty local receipt describes candidate bytes; CI receipts bind a clean checked-out commit.
