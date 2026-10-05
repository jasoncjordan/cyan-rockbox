# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

For product scope and target constraints, read root `PRD.md` and `HARDWARE.md`. Use `docs/README.md` to find relevant project records: `docs/design.md` describes the implemented design baseline, `docs/rockbox-notes.md` records implementation mechanisms, and `docs/release.md` identifies outstanding release gates. Consult the relevant records before proposing changes to established behavior.

This repo uses a **single-context** layout:

- **`GLOSSARY.md`** at the repo root: read its domain terms.
- **`docs/adr/`**: read ADRs that touch the area you are about to work in.

If these files do not exist, **proceed silently**. Do not flag their absence or suggest creating them upfront. The `/domain-modeling` skill (also used by `/grill-with-docs` and `/improve-codebase-architecture`) creates them lazily when terms or decisions actually get resolved.

## File structure

```text
/
├── GLOSSARY.md
├── docs/
│   └── adr/
│       └── NNNN-decision-title.md
└── src/
```

## Use the glossary's vocabulary

When naming a domain concept in an issue, proposal, hypothesis, or test, use the term defined in `GLOSSARY.md`. Do not drift to synonyms the glossary explicitly avoids.

If a needed concept is missing, reconsider whether it reflects the project's language. Note real vocabulary gaps for `/domain-modeling`.

## Flag ADR conflicts

If a proposal contradicts an existing ADR, identify the ADR and explain why reopening the decision may be justified rather than silently overriding it.
