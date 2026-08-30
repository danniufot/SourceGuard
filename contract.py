# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class SourceGuard(gl.Contract):

    last_claim: str

    source_1_url: str
    source_2_url: str

    source_1_verdict: str
    source_2_verdict: str

    source_1_evidence: str
    source_2_evidence: str

    source_1_authority: str
    source_2_authority: str

    source_1_freshness: str
    source_2_freshness: str

    source_1_quality: str
    source_2_quality: str

    overall_quality: str

    last_verdict: str
    last_evidence: str

    total_verifications: u256

    verification_history: DynArray[str]

    def __init__(self):

        self.last_claim = ""

        self.source_1_url = ""
        self.source_2_url = ""

        self.source_1_verdict = ""
        self.source_2_verdict = ""

        self.source_1_evidence = ""
        self.source_2_evidence = ""

        self.source_1_authority = ""
        self.source_2_authority = ""

        self.source_1_freshness = ""
        self.source_2_freshness = ""

        self.source_1_quality = ""
        self.source_2_quality = ""

        self.overall_quality = ""

        self.last_verdict = ""
        self.last_evidence = ""

        self.total_verifications = u256(0)

    @gl.public.write
    def verify_sources(
        self,
        claim: str,
        source_1: str,
        source_2: str
    ) -> None:

        if claim == "":
            raise gl.vm.UserError("Claim cannot be empty")

        if source_1 == "":
            raise gl.vm.UserError("Source 1 cannot be empty")

        if source_2 == "":
            raise gl.vm.UserError("Source 2 cannot be empty")

        def evaluate_sources():

            response_1 = gl.nondet.web.get(source_1)
            webpage_1 = response_1.body.decode("utf-8")

            response_2 = gl.nondet.web.get(source_2)
            webpage_2 = response_2.body.decode("utf-8")

            prompt = f"""
You are SourceGuard.

Analyze two web sources against a claim.

CLAIM:
{claim}

SOURCE 1 URL:
{source_1}

SOURCE 1 CONTENT:
{webpage_1}

SOURCE 2 URL:
{source_2}

SOURCE 2 CONTENT:
{webpage_2}

Analyze each source independently.

For each source determine:

1. VERDICT
2. DIRECT EVIDENCE
3. AUTHORITY
4. FRESHNESS

VERDICT must be exactly:

SUPPORTED
NOT_SUPPORTED
INCONCLUSIVE

SUPPORTED means the actual source contains direct
evidence supporting the claim.

NOT_SUPPORTED means the actual source contains evidence
contradicting the claim.

INCONCLUSIVE means there is not enough evidence.

AUTHORITY must be exactly:

HIGH
MEDIUM
LOW
UNKNOWN

HIGH means an official government source, regulator,
official organization, primary document, or clear
primary source.

MEDIUM means an established news organization,
recognized institution, professional organization,
or reputable secondary source.

LOW means an unknown publisher, personal blog,
forum, anonymous source, or unclear publisher.

UNKNOWN means authority cannot be determined.

FRESHNESS must be exactly:

CURRENT
RECENT
OLD
UNKNOWN

Use only dates actually present in the source.

Do not invent dates.

Do not invent evidence.

Do not treat topical similarity as proof.

Return valid JSON containing exactly these fields:

source_1_verdict
source_1_evidence
source_1_authority
source_1_freshness
source_2_verdict
source_2_evidence
source_2_authority
source_2_freshness

Do not return an overall verdict.

The smart contract calculates the final verdict
deterministically.
"""

            result = gl.nondet.exec_prompt(
                prompt,
                response_format="json"
            )

            if not isinstance(result, dict):
                raise gl.vm.UserError("Invalid LLM response")

            allowed_verdicts = (
                "SUPPORTED",
                "NOT_SUPPORTED",
                "INCONCLUSIVE"
            )

            allowed_authority = (
                "HIGH",
                "MEDIUM",
                "LOW",
                "UNKNOWN"
            )

            allowed_freshness = (
                "CURRENT",
                "RECENT",
                "OLD",
                "UNKNOWN"
            )

            source_1_verdict = result.get(
                "source_1_verdict"
            )

            source_1_evidence = result.get(
                "source_1_evidence"
            )

            source_1_authority = result.get(
                "source_1_authority"
            )

            source_1_freshness = result.get(
                "source_1_freshness"
            )

            source_2_verdict = result.get(
                "source_2_verdict"
            )

            source_2_evidence = result.get(
                "source_2_evidence"
            )

            source_2_authority = result.get(
                "source_2_authority"
            )

            source_2_freshness = result.get(
                "source_2_freshness"
            )

            if source_1_verdict not in allowed_verdicts:
                raise gl.vm.UserError(
                    "Invalid source 1 verdict"
                )

            if source_2_verdict not in allowed_verdicts:
                raise gl.vm.UserError(
                    "Invalid source 2 verdict"
                )

            if source_1_authority not in allowed_authority:
                raise gl.vm.UserError(
                    "Invalid source 1 authority"
                )

            if source_2_authority not in allowed_authority:
                raise gl.vm.UserError(
                    "Invalid source 2 authority"
                )

            if source_1_freshness not in allowed_freshness:
                raise gl.vm.UserError(
                    "Invalid source 1 freshness"
                )

            if source_2_freshness not in allowed_freshness:
                raise gl.vm.UserError(
                    "Invalid source 2 freshness"
                )

            if not isinstance(
                source_1_evidence,
                str
            ):
                raise gl.vm.UserError(
                    "Invalid source 1 evidence"
                )

            if not isinstance(
                source_2_evidence,
                str
            ):
                raise gl.vm.UserError(
                    "Invalid source 2 evidence"
                )

            return {
                "source_1_verdict": source_1_verdict,
                "source_1_evidence": source_1_evidence,
                "source_1_authority": source_1_authority,
                "source_1_freshness": source_1_freshness,
                "source_2_verdict": source_2_verdict,
                "source_2_evidence": source_2_evidence,
                "source_2_authority": source_2_authority,
                "source_2_freshness": source_2_freshness
            }

        def calculate_overall(
            source_1_verdict,
            source_2_verdict
        ):

            if (
                source_1_verdict == "SUPPORTED"
                and
                source_2_verdict == "SUPPORTED"
            ):
                return "SUPPORTED"

            if (
                source_1_verdict == "NOT_SUPPORTED"
                and
                source_2_verdict == "NOT_SUPPORTED"
            ):
                return "NOT_SUPPORTED"

            return "INCONCLUSIVE"

        def calculate_quality(
            authority,
            freshness
        ):

            if (
                authority == "HIGH"
                and
                freshness in (
                    "CURRENT",
                    "RECENT"
                )
            ):
                return "STRONG"

            if (
                authority == "MEDIUM"
                and
                freshness in (
                    "CURRENT",
                    "RECENT"
                )
            ):
                return "MODERATE"

            return "WEAK"

        def calculate_overall_quality(
            quality_1,
            quality_2
        ):

            if (
                quality_1 == "STRONG"
                and
                quality_2 == "STRONG"
            ):
                return "STRONG"

            if (
                quality_1 == "WEAK"
                or
                quality_2 == "WEAK"
            ):
                return "WEAK"

            return "MODERATE"

        def validator_fn(leader_result) -> bool:

            if not isinstance(
                leader_result,
                gl.vm.Return
            ):
                return False

            leader_data = leader_result.calldata

            if not isinstance(
                leader_data,
                dict
            ):
                return False

            leader_source_1 = leader_data.get(
                "source_1_verdict"
            )

            leader_source_2 = leader_data.get(
                "source_2_verdict"
            )

            allowed_verdicts = (
                "SUPPORTED",
                "NOT_SUPPORTED",
                "INCONCLUSIVE"
            )

            if leader_source_1 not in allowed_verdicts:
                return False

            if leader_source_2 not in allowed_verdicts:
                return False

            leader_overall = calculate_overall(
                leader_source_1,
                leader_source_2
            )

            validator_result = evaluate_sources()

            if not isinstance(
                validator_result,
                dict
            ):
                return False

            validator_source_1 = validator_result.get(
                "source_1_verdict"
            )

            validator_source_2 = validator_result.get(
                "source_2_verdict"
            )

            validator_overall = calculate_overall(
                validator_source_1,
                validator_source_2
            )

            if leader_source_1 != validator_source_1:
                return False

            if leader_source_2 != validator_source_2:
                return False

            if leader_overall != validator_overall:
                return False

            return True

        result = gl.vm.run_nondet_unsafe(
            evaluate_sources,
            validator_fn
        )

        source_1_verdict = result[
            "source_1_verdict"
        ]

        source_2_verdict = result[
            "source_2_verdict"
        ]

        overall_verdict = calculate_overall(
            source_1_verdict,
            source_2_verdict
        )

        source_1_quality = calculate_quality(
            result["source_1_authority"],
            result["source_1_freshness"]
        )

        source_2_quality = calculate_quality(
            result["source_2_authority"],
            result["source_2_freshness"]
        )

        overall_quality = calculate_overall_quality(
            source_1_quality,
            source_2_quality
        )

        self.last_claim = claim

        self.source_1_url = source_1
        self.source_2_url = source_2

        self.source_1_verdict = source_1_verdict
        self.source_2_verdict = source_2_verdict

        self.source_1_evidence = result[
            "source_1_evidence"
        ]

        self.source_2_evidence = result[
            "source_2_evidence"
        ]

        self.source_1_authority = result[
            "source_1_authority"
        ]

        self.source_2_authority = result[
            "source_2_authority"
        ]

        self.source_1_freshness = result[
            "source_1_freshness"
        ]

        self.source_2_freshness = result[
            "source_2_freshness"
        ]

        self.source_1_quality = source_1_quality
        self.source_2_quality = source_2_quality

        self.overall_quality = overall_quality

        self.last_verdict = overall_verdict

        self.last_evidence = (
            "Source 1: "
            + self.source_1_evidence
            + " | Source 2: "
            + self.source_2_evidence
            + " | Deterministic rule: "
            + source_1_verdict
            + " + "
            + source_2_verdict
            + " = "
            + overall_verdict
        )

        self.total_verifications += u256(1)

        history_record = (
            "Verification #"
            + str(self.total_verifications)
            + " | CLAIM: "
            + claim
            + " | SOURCE1: "
            + source_1
            + " | SOURCE1 VERDICT: "
            + source_1_verdict
            + " | SOURCE1 AUTHORITY: "
            + self.source_1_authority
            + " | SOURCE1 FRESHNESS: "
            + self.source_1_freshness
            + " | SOURCE1 QUALITY: "
            + source_1_quality
            + " | SOURCE2: "
            + source_2
            + " | SOURCE2 VERDICT: "
            + source_2_verdict
            + " | SOURCE2 AUTHORITY: "
            + self.source_2_authority
            + " | SOURCE2 FRESHNESS: "
            + self.source_2_freshness
            + " | SOURCE2 QUALITY: "
            + source_2_quality
            + " | OVERALL: "
            + overall_verdict
            + " | OVERALL QUALITY: "
            + overall_quality
        )

        self.verification_history.append(
            history_record
        )

    @gl.public.view
    def get_last_claim(self) -> str:
        return self.last_claim

    @gl.public.view
    def get_source_1(self) -> str:
        return self.source_1_url

    @gl.public.view
    def get_source_2(self) -> str:
        return self.source_2_url

    @gl.public.view
    def get_source_1_verdict(self) -> str:
        return self.source_1_verdict

    @gl.public.view
    def get_source_2_verdict(self) -> str:
        return self.source_2_verdict

    @gl.public.view
    def get_source_1_evidence(self) -> str:
        return self.source_1_evidence

    @gl.public.view
    def get_source_2_evidence(self) -> str:
        return self.source_2_evidence

    @gl.public.view
    def get_source_1_authority(self) -> str:
        return self.source_1_authority

    @gl.public.view
    def get_source_2_authority(self) -> str:
        return self.source_2_authority

    @gl.public.view
    def get_source_1_freshness(self) -> str:
        return self.source_1_freshness

    @gl.public.view
    def get_source_2_freshness(self) -> str:
        return self.source_2_freshness

    @gl.public.view
    def get_source_1_quality(self) -> str:
        return self.source_1_quality

    @gl.public.view
    def get_source_2_quality(self) -> str:
        return self.source_2_quality

    @gl.public.view
    def get_overall_quality(self) -> str:
        return self.overall_quality

    @gl.public.view
    def get_last_verdict(self) -> str:
        return self.last_verdict

    @gl.public.view
    def get_last_evidence(self) -> str:
        return self.last_evidence

    @gl.public.view
    def get_total_verifications(self) -> u256:
        return self.total_verifications

    @gl.public.view
    def get_history_length(self) -> u256:
        return u256(len(self.verification_history))

    @gl.public.view
    def get_history_item(
        self,
        index: u256
    ) -> str:

        if index >= len(self.verification_history):
            return ""

        return self.verification_history[index]