# Conformidad — Spec Kit extension

Checks that a project's artifacts contain what the **Software Humano manifesto** requires, that every absence is declared as an approved exception, and that the method is still installed intact.

> **Language.** This extension's output, its configuration file and its comments are written in **Spanish**. This README is in English because it is how the extension is listed in the Spec Kit community catalog.

## Why it exists

Spec Kit's hooks are invoked by the agent, which means an agent can skip one without anything noticing. This extension ships a **deterministic script** that a person, a CI job or a workflow `shell` step runs — outside the agent's discretion.

It is registered as a mandatory `before_implement` hook, so it also runs before code is generated, which is the moment the manifesto names.

Category: `quality`. Effect: `read-only` — it never modifies an artifact.

## What it checks

**1 · That the method is still installed.** A preset can be left without effect and nothing says so: a project-local override wins over any preset, another preset with higher precedence can register a command in its place, and an emptied template layer leaves the doctrine out. In all three cases the artifact comes out clean because nothing was ever asked of it.

So before looking at artifacts, it verifies that the eight commands are composed and carry the manifesto's additions, that the three template layers are not empty, that no project override shadows one of the eight, and — reading Spec Kit's own preset registry — that no preset with higher precedence has taken one of them over.

**2 · That decisions reached the artifacts.** A decision made in conversation gets recorded in `AGENTS.md` or in the product foundation, and may never reach `spec.md` or `plan.md`. The artifact stays complete and correct, so no other check can see it. This one compares each file's last commit date and stops when a governing source is newer.

It detects one direction only: the reverse proves nothing. A newer `spec.md` does not mean it absorbed the decision.

**3 · That the required sections have content**, and that every absence is declared.

## Approved exceptions

The manifesto admits two states and no more: an element has implementation and verifiable evidence, **or** an explicit and approved exception. An exception needs four fields, and without all four it is not one:

```yaml
excepciones:
  - artefacto: "plan.md"
    seccion: "Presupuesto de complejidad"
    razon: "The product predates the method; it will be raised when the next capability is planned."
    aprobada_por: "Name of the product authority"
```

`artefacto` is required because the same section appears in more than one artifact. Without it, an exception declared for one silently covered the other.

When a field is missing, the check names which one rather than reporting the section as simply absent.

**This is what makes the method adoptable on a repository that predates it:** declare what you do not yet meet, with its reason and who approved it, and the method does not block you. What it rejects is what is missing without anyone knowing.

## Installation

```bash
specify extension add --dev ./conformidad-2.2.2
```

This scaffolds `conformidad-config.yml`, where exceptions are declared.

Requires Spec Kit `>=1.0.0,<2.0.0`. Verified on 1.0.8.

## Running it

```bash
.specify/extensions/conformidad/scripts/conformidad.sh
```

Exit `0` when everything is covered or declared, `1` when something is missing undeclared or the method is not installed intact, `2` when it cannot find the project.

It needs `git` to compare dates, and `python3` to read the preset registry. Without either it says so and does not check, rather than reporting green.

## What it does not check

**Whether what is written is any good.** A table full of plausible sentences passes. That is judged by `analyze` and by a person.

And it does not look at the screen. Whether the experience meets the manifesto's principles is not something any of these checks can reach.

## Pairs with

The Software Humano preset, which puts the manifesto's requirements into the commands and templates this extension then verifies. They ship together in the method package.

## Licensing

MIT.

## Author and documentation

Manifesto and method by **Damián Acuña** · [manifiesto.softwarehumano.com](https://manifiesto.softwarehumano.com)

The package was developed with assistance from Claude, under his authorship and decision.

Full documentation, in Spanish: [github.com/dacunao/software-humano-speckit](https://github.com/dacunao/software-humano-speckit)
