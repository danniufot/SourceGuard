# SourceGuard

SourceGuard is a GenLayer intelligent contract for multi-source web claim verification.

## Overview

SourceGuard allows a user to submit a claim together with two web sources.

The contract retrieves both sources and uses GenLayer's nondeterministic execution to analyze their contents.

For each source, SourceGuard produces:

- Verdict
- Evidence
- Authority
- Freshness
- Evidence quality

The contract then calculates the final verdict deterministically.

## Verdict Logic

SUPPORTED + SUPPORTED = SUPPORTED

NOT_SUPPORTED + NOT_SUPPORTED = NOT_SUPPORTED

Any other combination = INCONCLUSIVE

## Evidence Quality

HIGH authority + CURRENT or RECENT freshness = STRONG

MEDIUM authority + CURRENT or RECENT freshness = MODERATE

LOW or UNKNOWN authority = WEAK

## Validation

SourceGuard uses GenLayer's validator mechanism.

Validators independently evaluate the sources and compare the resulting source-level verdicts.

The contract only accepts the result when the required verification conditions are satisfied.

## Persistent Verification History

Each successful verification is recorded in contract storage.

Previous verification records can be queried through the contract's public view functions.

## Example

Claim:

The Example Domain webpage is provided for documentation examples.

Sources:

https://example.com/

https://iana.org/help/example-domains

Expected result:

SUPPORTED

## Testing

SourceGuard has been tested with:

- Supporting claims
- Unsupported claims
- Multi-source verification
- Evidence extraction
- Authority classification
- Freshness classification
- Evidence quality
- Validator verification
- Persistent verification history

## Project Status

SourceGuard V8 has been successfully deployed and tested on GenLayer.

This project is an experimental demonstration of decentralized web-source verification using GenLayer intelligent contracts.