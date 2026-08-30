# SourceGuard Verification Flow

```text
                    USER
                     |
                     v
              CLAIM + 2 URLS
                     |
                     v
             SOURCE RETRIEVAL
               /           \
              /             \
             v               v
        SOURCE 1         SOURCE 2
             |               |
             v               v
        LLM ANALYSIS     LLM ANALYSIS
             |               |
             v               v
        VERDICT           VERDICT
        EVIDENCE          EVIDENCE
        AUTHORITY         AUTHORITY
        FRESHNESS         FRESHNESS
             \               /
              \             /
               v           v
                VALIDATORS
                     |
                     v
                  CONSENSUS
                     |
                     v
          DETERMINISTIC RULE
                     |
          +----------+----------+
          |          |          |
          v          v          v
      SUPPORTED  NOT_SUPPORTED  INCONCLUSIVE
                     |
                     v
             QUALITY SCORING
                     |
                     v
             HISTORY STORAGE
