# Governance (Human-in-the-loop)

## Rules
1. Every experiment must be replayable (seeded).
2. CI runs `pytest` and includes at least one replay test.
3. Changes affecting outputs require updated docs/tests.
4. Keep heavy outputs out of git; commit only small examples in `data/`.

## Kill conditions
- Replay fails (non-determinism introduced)
- Invariants break without justification
