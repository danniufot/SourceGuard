# SourceGuard V8 Test Evidence

## Test Environment

Project: SourceGuard

Network: GenLayer

Version: V8

Deployment status: FINALIZED

---

## Test 1 — Supported Claim

### Claim

The Example Domain webpage is provided for documentation examples.

### Source 1

https://example.com/

### Source 2

https://iana.org/help/example-domains

### Expected Result

SUPPORTED

### Observed Result

SUPPORTED

### Evidence

Both sources were successfully retrieved and analyzed.

Source-level verdicts were returned successfully.

### Status

PASS

---

## Test 2 — Unsupported Claim

### Claim

The Example Domain website sells automobiles in Nigeria.

### Source 1

https://example.com/

### Source 2

https://iana.org/help/example-domains

### Expected Result

NOT_SUPPORTED

### Observed Result

NOT_SUPPORTED

### Evidence

The sources did not provide evidence supporting the claim.

### Status

PASS

---

## Test 3 — Source Evidence

SourceGuard successfully returned evidence text for the analyzed sources.

### Status

PASS

---

## Test 4 — Authority Classification

SourceGuard successfully classified source authority.

Possible classifications:

- HIGH
- MEDIUM
- LOW
- UNKNOWN

### Status

PASS

---

## Test 5 — Freshness Classification

SourceGuard successfully classified source freshness.

Possible classifications:

- CURRENT
- RECENT
- OLD
- UNKNOWN

### Status

PASS

---

## Test 6 — Evidence Quality

SourceGuard successfully calculated evidence quality.

Possible results:

- STRONG
- MODERATE
- WEAK

### Status

PASS

---

## Test 7 — Deterministic Verdict

SourceGuard calculates the final verdict independently from the LLM's free-form response.

### Rules

SUPPORTED + SUPPORTED

= SUPPORTED

NOT_SUPPORTED + NOT_SUPPORTED

= NOT_SUPPORTED

Any other combination

= INCONCLUSIVE

### Status

PASS

---

## Test 8 — Validator Verification

The SourceGuard validator independently evaluated the source analysis.

Successful tests reached consensus and finalized.

### Status

PASS

---

## Test 9 — Persistent Verification History

SourceGuard successfully stored verification records.

The verification history was queried through the contract's public view functions.

### Status

PASS

---

## Summary

SourceGuard V8 successfully demonstrated:

- Multi-source web retrieval
- Source-level claim verification
- Evidence extraction
- Authority classification
- Freshness classification
- Evidence quality scoring
- Deterministic final verdicts
- Validator-based verification
- Consensus
- Persistent verification history

Overall test status:

PASS
