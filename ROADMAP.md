**English** · [Español](ROADMAP.es.md) · [Português (BR)](ROADMAP.pt-BR.md)

# Roadmap

What we know is missing, in plain sight. Each item has an issue for discussion and, where applicable, the proposal where it is analyzed.

This list **promises no dates**. None of its items is committed: they are identified, measured and open.

It is published for the same reason the method exists. The manifesto's definition of done admits two states and no more: met with verifiable evidence, **or** an explicit and approved exception. This roadmap is the second. Hiding it would break the doctrine in the repository that distributes it.

---

## Open

| Item | Why it matters | Where |
|---|---|---|
| **The package claims the project's root** | Installing the method leaves seven of its files in someone else's root, and one of them — `LICENSE` — is still pinned by the integrity check | [#1](https://github.com/dacunao/software-humano-speckit/issues/1) · [proposal 011](docs/proposals/011-el-paquete-reclama-la-raiz-del-proyecto.md) |
| **Execution cost** | A `plan` invocation loads ~36,500 tokens of method before touching the project. Two thirds is the constitution, and it was never optimized | [#2](https://github.com/dacunao/software-humano-speckit/issues/2) · [analysis 007](docs/proposals/007-analisis-de-costo-de-ejecucion-del-metodo.md) |
| **Editing the agent-facing file is not detected** | It is the fourth of four ways the method can be left without effect. The other three are closed | [#3](https://github.com/dacunao/software-humano-speckit/issues/3) · [proposal 010](docs/proposals/010-evaluacion-del-piloto-del-sitio.md) |
| **Workflow gates cannot be resumed** | Without a terminal — CI, or an agent running it for you — the run pauses and there is no way to supply the verdict | [#8](https://github.com/dacunao/software-humano-speckit/issues/8) |
| **The bundle cannot be installed** | Spec Kit's community catalog is discovery-only: being listed does not make anything installable by name. And the bundle is in no catalog. The fourth layer exists and does not work | [#4](https://github.com/dacunao/software-humano-speckit/issues/4) |
| **No command propagates a change in the foundation** | In the first site the foundation changed six times, and the spec and plan were rewritten by hand all six | [#5](https://github.com/dacunao/software-humano-speckit/issues/5) · [proposal 010](docs/proposals/010-evaluacion-del-piloto-del-sitio.md) |
| **The package exists only in Spanish** | Deliberate — the doctrine holds its authority in Spanish — and a real limit on adoption | [#6](https://github.com/dacunao/software-humano-speckit/issues/6) |
| **No quick-start guide** | The method supports three ways of working — conversing, invoking, workflow — and nothing tells a newcomer which one fits their style | [#9](https://github.com/dacunao/software-humano-speckit/issues/9) |

## How items get here

An item joins this list when **something measured it**: a pilot, a rehearsal, or an analysis with its evidence. It does not join for sounding like a good idea.

And it leaves the list when it is applied **with a decision from the product authority**. The record of every decision lives in [`docs/proposals/`](docs/proposals/), which is added to and never rewritten.

## Taking part

The [issues](https://github.com/dacunao/software-humano-speckit/issues) are open. If you use the method and something gets in your way, say so there: **what gets measured joins this list.**

The four items that say the most about the method came from a real project using it, not from planning it.
