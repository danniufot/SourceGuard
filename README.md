# SourceGuard

> Decentralized multi-source web claim verification powered by GenLayer Intelligent Contracts.

SourceGuard evaluates claims against live web sources using GenLayer web access, nondeterministic execution, validator verification, deterministic decision logic, and persistent onchain history.

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

The contract separates nondeterministic source analysis from deterministic state updates and final verdict calculation.

## Persistent Verification History

Each successful verification is recorded in contract storage.

Previous verification records can be queried through the contract's public view functions.

## Example

### Claim

The Example Domain webpage is provided for documentation examples.

### Sources

https://example.com/

https://iana.org/help/example-domains

### Expected Result

SUPPORTED

## GenLayer Deployment

SourceGuard V8 was successfully deployed and tested on GenLayer.

### Deployment Status

FINALIZED

### Contract Address

0x9c58ad6ba1b42b93336e59731adbdafdbd3dff33d759c3a1137045ebe0cd7eaf

### Transaction Evidence

Transaction 1:

0x64e6ca416900417f4f679482442b28735d67642adcd020a831db8919ce9215b7

Transaction 2:

0xE2920f5dbD7541Ee989834c2aaceA00e594f8EA8

## Testing

SourceGuard has been tested with:

- Supporting claims
- Unsupported claims
- Multi-source verification
- Evidence extraction
- Authority classification
- Freshness classification
- Evidence quality
- Deterministic verdict calculation
- Validator verification
- Persistent verification history

All completed tests returned the expected results and successfully reached finalization/consensus.

## Project Status

SourceGuard V8 is deployed and tested on GenLayer.

This project is an experimental demonstration of decentralized web-source verification using GenLayer Intelligent Contracts.
