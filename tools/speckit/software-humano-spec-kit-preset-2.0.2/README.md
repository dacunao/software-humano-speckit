# Software Humano — Spec Kit preset

Adds the requirements of the **Software Humano manifesto** to Spec Kit's eight core commands and to the spec, plan and tasks templates, quoting the manifesto's literal text rather than rephrasing it.

> **Language.** This preset's own content — the commands it composes, the templates it adds and the constitution it installs — is written in **Spanish**. This README is in English because it is how the preset is listed in the Spec Kit community catalog.

## What it provides

| Kind | Count | What |
|---|---|---|
| Commands | 8 | `constitution`, `specify`, `clarify`, `plan`, `tasks`, `analyze`, `implement`, `converge` |
| Templates | 4 | the constitution, plus additions to `spec-template`, `plan-template` and `tasks-template` |

`speckit.checklist` and `speckit.taskstoissues` are left untouched.

## How it composes

**Commands use `wrap` and declare no frontmatter of their own.** A layer that declares frontmatter replaces the core's, taking the description, `handoffs` and `scripts` with it. By declaring none, the native frontmatter survives intact — which is also what lets an agent recognize when each command applies from natural language, without anyone typing a command.

**Templates use `append`, not `replace`.** Replacing removes the sections the native commands look up by name. The one exception is the constitution template, whose content is the manifesto's projection and therefore entirely the preset's own.

Each command gains one table: where the manifesto says it, what it requires, and which artifact or verification dimension answers it. Every row is a literal quotation of the manifesto core v2.1.

## Installation

```bash
specify preset add --dev ./software-humano-spec-kit-preset-2.0.2
```

Then materialize the constitution with your agent's `speckit.constitution` command. Note that many agents load their command catalog at startup, so a command registered in the current session may not exist until you reopen it.

Requires Spec Kit `>=1.0.0,<2.0.0`. Verified on 1.0.8.

The preset installs at priority 10. If your project installs other presets that compose the same commands, set the order with `preset set-priority` — a lower number wins.

## Verifying the installation

After installing, these should hold:

```bash
# the eight commands are composed and keep their native frontmatter
ls .specify/presets/software-humano/.composed/ | wc -l          # 8
head -20 .specify/presets/software-humano/.composed/speckit.plan.md | grep -c '^handoffs:'   # 1

# the templates keep their native sections and gain the manifesto's
.specify/scripts/bash/resolve-template.sh spec-template | grep -c 'Success Criteria\|Edge Cases'   # 2
.specify/scripts/bash/resolve-template.sh plan-template | grep -c '__SPECKIT_COMMAND'              # 0
```

Template resolution needs Python 3 with PyYAML on `PATH`. Without it, composed template resolution fails.

`specify integration status` will report `warning` with 8 modified files. That is the expected result — they are the eight commands this preset composes — and `checklist` must not be among them.

## What it does not do

It is **not a design system or a visual guide**. It sets criteria — accessibility, states, cognitive load, performance, traceability — not aesthetics.

It checks that what the manifesto requires is **present and traceable**, not that the product is good. Whether the experience meets the principles is judged by a person using the product.

## Related components

This preset is one of four layers. The others are an extension that runs conformance checks, a workflow with the control points the manifesto specifies, and a bundle that composes them. They ship together in the method package.

## Licensing

The preset code is **MIT**. The manifesto core's text — including its projection in `templates/constitution-template.md` — is **CC BY 4.0**. The boundary is defined by nature, not by folder; see `LICENSING.md` in the package.

## Author and documentation

Manifesto and method by **Damián Acuña** · [manifiesto.softwarehumano.com](https://manifiesto.softwarehumano.com)

Full documentation, in Spanish: [github.com/dacunao/software-humano-speckit](https://github.com/dacunao/software-humano-speckit)
