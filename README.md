**English** · [Español](README.es.md) · [Português (BR)](README.pt-BR.md)

# Software Humano for SpecKit

> We build tools that extend what people can do — not tools that show off what software can do.

A method package that applies the **Software Humano manifesto** to [SpecKit](https://github.com/github/spec-kit)'s spec-driven development cycle, in any project.

**Read the manifesto:** [manifiesto.softwarehumano.com](https://manifiesto.softwarehumano.com)

> **A note on language.** The manifesto is published in English, Spanish and Brazilian Portuguese on the site. **This package — its documents, instructions, tooling output and inline comments — is written in Spanish.** If you plan to adopt it, expect to work in Spanish.

---

## The manifesto

The **Core of the manifesto for human software development with artificial intelligence**, by **Damián Acuña**, answers one question:

> How do we build software that amplifies what people can accomplish, **without handing them the complexity of the technology**?

Building a product has a cost, and that cost does not disappear — it gets divided. The team pays part of it. The rest is handed to the person using the product, paid in attention, in learning, and in decisions they never came to make. That handover is almost never a decision.

From there follow its least conventional claims: that a product with no defects can still fail through overload, that complexity belongs to the system and not to the interface, and that attention has a budget which is verified the way performance is.

The full text lives in [`docs/method/`](docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md) (Spanish) and on [the site](https://manifiesto.softwarehumano.com). It is the source of authority for everything else here.

## What kind of products this is for

The manifesto states its own scope:

> The framework serves products where the experience of use directly shapes the outcome: **web and mobile applications, internal tools, learning systems, digital services, agent-based products and AI-assisted solutions.** It addresses product managers, designers, developers and coding agents who take part in product decisions.

If the experience of use doesn't change the outcome of what you build, this method will cost you more than it returns.

## What the package does

A manifesto doesn't apply itself. An agent with the doctrine available can skip it with nothing stopping it, and with no one noticing until the product is already built.

This package puts the manifesto's provisions **inside the commands the team already runs**, quoting its literal text rather than rephrasing it. Of 300 checkable statements in the core, 210 are compiled; 40 are declared out of scope and 50 are editorial.

It does not modify SpecKit. It uses four of its documented extension mechanisms.

## What it does not do

**It is not a design system or a visual guide.** No components, no typefaces, no palettes, no opinions on how a product should look. It sets criteria — accessibility, states, cognitive load, performance, traceability — not aesthetics. Visual direction is the team's call.

**It does not check that the product is good.** It checks that what the manifesto requires is present and traceable. The commands review consistency between artifacts, and code against tasks; none of them looks at the screen. Whether the experience meets the principles is judged by a person using the product.

**The method does not replace testing with people: it makes it non-optional.**

## Getting started

You need [SpecKit](https://github.com/github/spec-kit) `>=1.0.0,<2.0.0`, Python 3 with PyYAML, git, and an AI agent with a SpecKit integration.

```bash
# Download the package from Releases and unpack it into your project
unzip software-humano-speckit-starter-vX.Y.Z.zip -d /tmp/sh
cp -R /tmp/sh/software-humano-speckit-starter-vX.Y.Z/. .

# Verify it arrived intact, and that your environment works
shasum -a 256 -c SHA256SUMS
tools/speckit/preflight.sh
```

Then fill in the **Completar por proyecto** section at the end of `AGENTS.md` and hand your agent the prompt in [`START_WITH_AI_AGENT.md`](package/START_WITH_AI_AGENT.md). The step-by-step verifiable procedure is in [`instructions/01`](package/instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md).

> Installation usually takes **two sessions**: many agents load their command catalog at startup, so freshly installed commands don't exist until you reopen. That's expected.

## What's inside

| Layer | SpecKit mechanism | What it contributes |
|---|---|---|
| Preset | `preset` | The doctrine inside the eight commands and the three templates |
| Conformance | `extension` | Checks that what is required is present, and stops when something is missing and undeclared |
| Gates | `workflow` | The control points the manifesto itself specifies, run by the engine |
| Distribution | `bundle` | Composes and pins the other three |

Plus the documentation: the core, the annex tracing every provision back to SpecKit, the implementation guide, the installation instructions, and [`PARA_QUIEN_DECIDE.md`](package/PARA_QUIEN_DECIDE.md) — written for the person who approves, not for the agent.

## Two modes, depending on how you work

**Individual commands.** The agent invokes each command when it recognizes the situation that command names, from natural language. This enables the doctrine in the artifacts without anyone typing a command; it depends on the agent recognizing the moment.

**Workflow.** The whole cycle runs at once. This additionally enables the gates and the conformance check, which the engine runs and the agent cannot skip.

Neither is "the right one". Someone working conversationally, deciding turn by turn, will lean on the first; someone who wants the closed cycle, or runs it in CI, on the second. Both are installed and you can alternate.

## Licensing

The package mixes two natures, and the boundary is defined by nature rather than by folder:

| What | License |
|---|---|
| Preset, extension, workflow, bundle, tooling and instructions | [MIT](LICENSE) |
| The manifesto core's text, including its projection as a constitution | [CC BY 4.0](LICENSE-CONTENT) |

Which file falls on which side is explained in [`LICENSING.md`](LICENSING.md). Suggested attribution for the text:

> «Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1», by Damián Acuña, licensed CC BY 4.0.

## Authorship

Manifesto and method by **Damián Acuña**. The package was developed with assistance from Claude, under his authorship and decision.

## How it's maintained

`docs/proposals/` is the maintenance record: entries are added, never rewritten. Each proposal separates observed fact, inference, and the decision that belongs to a person — and none is applied without a decision from the product authority.

The method is validated on real projects, and its findings are evaluated here before anything changes.
