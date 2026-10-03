# Practice scenarios

1. Run `python scripts/career_verify.py`. Open the receipt and compare `wrong_completion` with `correct`: cite a diff line, failing assertion, smallest repair and unsupported claims.
2. Remove blank-title validation; predict domain and HTTP failures before running the mutant. Explain why a happy-path screenshot misses the regression.
3. Add priority sorting. First ask for range, default, direction and tie-breaker; the existing missing-spec case should abstain until these are supplied. Then update domain, API, UI and tests.
4. Replace the in-memory store with durable storage. Discuss migrations, transaction boundaries and restart tests; these remain design extensions.
5. Review the HTML rendering boundary and explain why a static textContent assertion does not establish browser security.

These are original role-family practice scenarios, not actual employer take-home questions. A 15-minute session can run the fixture, diagnose one mutant and implement one specified requirement.
