# SourceGuard Architecture

## Overview

SourceGuard uses GenLayer intelligent contract capabilities to evaluate claims against live web sources.

The system separates nondeterministic interpretation from deterministic decision logic.

## Flow

1. User submits a claim.
2. User provides two source URLs.
3. SourceGuard retrieves both web sources.
4. The leader analyzes the sources.
5. Each source receives a verdict.
6. Evidence is extracted from each source.
7. Authority is classified.
8. Freshness is classified.
9. Validators independently repeat the analysis.
10. Validator results are compared with the leader result.
11. The contract calculates the final verdict deterministically.
12. Evidence quality is calculated deterministically.
13. The verification is stored in contract history.

## Source Verdicts

Each source can return:

- SUPPORTED
- NOT_SUPPORTED
- INCONCLUSIVE

## Deterministic Verdict

SUPPORTED + SUPPORTED = SUPPORTED

NOT_SUPPORTED + NOT_SUPPORTED = NOT_SUPPORTED

All other combinations = INCONCLUSIVE

## Evidence Quality

HIGH authority + CURRENT/RECENT freshness = STRONG

MEDIUM authority + CURRENT/RECENT freshness = MODERATE

LOW or UNKNOWN authority = WEAK

## Validation

Validators independently evaluate the sources.

The contract compares the stable source-level verdicts rather than requiring exact agreement on free-form evidence text.

This helps separate variable language generation from the stable decision fields required for consensus.

## Storage

SourceGuard stores:

- Last claim
- Source URLs
- Source verdicts
- Source evidence
- Source authority
- Source freshness
- Source quality
- Overall verdict
- Overall quality
- Verification count
- Verification history

## Purpose

SourceGuard demonstrates how GenLayer can be used to build applications where smart contracts need to reason about information from the web while maintaining validator-based verification and deterministic state updates.
