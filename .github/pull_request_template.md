## Change

Describe the prompt, documentation, or tool change and the distinct problem it solves.

## Preserved boundaries

State which requirements, source roles, stable IDs, and outputs remain unchanged. Explain any deliberate contract change.

## Verification

- [ ] Generated catalogs and folder indexes are current.
- [ ] `python3 tools/library.py validate` passed.
- [ ] `python3 -m unittest discover -s tests -v` passed.
- [ ] Representative inputs render without missing placeholders.
- [ ] Model evaluations, if any, are distinguished from structural checks.
- [ ] No secrets, private data, or unsupported licensing claims were added.
