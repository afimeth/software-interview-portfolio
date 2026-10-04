# Evidence Contract

Public repositories should expose the smallest useful, inspectable unit of engineering evidence.

## 1. Preserve meaning

Raw human input is evidence and should not be overwritten by a normalized sentence.

A working representation may be projected into English, Go-like syntax, JSON/YAML, CJK/other compact relay forms, an AST/graph, or a model-specific encoding. No projection is the meaning itself.

```text
source input
  -> semantic filter
  -> structured semantic object
  -> task/model/engineer projection
```

Compression is acceptable only when the source and the semantic relation remain recoverable.

## 2. Bind claims to references

A technical claim should resolve to the concrete object that supports it:

```text
claim
  -> implementation reference
  -> fixture/input reference
  -> test/eval reference
  -> observed output/receipt
  -> limitation
```

Do not substitute repository size, feature count, screenshots, or product polish for this chain.

## 3. Headless runtime first

A runtime should have a stable invocation that can be triggered from a CLI, IDE action, web button, desktop shell, or automation.

```text
input -> runtime -> output -> receipt
```

The public evidence contract does not require a bundled UI. UI is an optional projection and can be supplied by the user or another project.

## 4. Separate evidence classes

Keep these claims mechanically distinct:

- **IMPLEMENTED**: code exists.
- **MEASURED**: a specific run produced a bound measurement/receipt.
- **DESIGNED**: specified but not demonstrated.
- **NOT CLAIMED**: outside current evidence.
- **INDEPENDENTLY REVIEWED**: only when an external review actually exists.
- **PRODUCTION-VALIDATED**: only when production evidence exists.

Passing tests do not automatically promote a claim into a stronger class.

## 5. Prefer clean data over rich presentation

Useful public evidence is small, referenceable, and reproducible:

- synthetic fixtures instead of private data;
- machine-readable receipts where practical;
- stable IDs/hashes/timestamps when causality or freshness matters;
- explicit failure cases and abstentions;
- minimal dependencies;
- no API keys, credentials, private topology, or customer information.

## 6. Encoding is replaceable

Repository interfaces should not make English, one model vendor, or one UI framework canonical.

```text
one semantic object
  -> many valid encodings
  -> one evaluated outcome
```

Choose an encoding for the current consumer. Preserve the semantic object and evidence references across projections.
