**Português (BR)** · [English](ROADMAP.md) · [Español](ROADMAP.es.md)

# Roteiro

O que sabemos que falta, à vista. Cada tema tem sua issue para discussão e, quando for o caso, a proposta onde está analisado.

Esta lista **não promete datas**. Nenhum de seus temas está comprometido: estão identificados, medidos e abertos.

É publicada pela mesma razão pela qual o método existe. A definição de conclusão do manifesto admite dois estados e não mais: cumprido com evidência verificável, **ou** exceção explícita e aprovada. Este roteiro é o segundo. Escondê-lo seria descumprir a doutrina no repositório que a distribui.

---

## Aberto

| Tema | Por que importa | Onde |
|---|---|---|
| **O pacote se apropria da raiz do projeto** | Instalar o método deixa sete arquivos seus na raiz alheia, e um deles — `LICENSE` — segue fixado pela verificação de integridade | [#1](https://github.com/dacunao/software-humano-speckit/issues/1) · [proposta 011](docs/proposals/011-el-paquete-reclama-la-raiz-del-proyecto.md) |
| **Custo de execução** | Uma invocação de `plan` carrega ~36.500 tokens de método antes de tocar o projeto. Dois terços são a constituição, e nunca foi otimizada | [#2](https://github.com/dacunao/software-humano-speckit/issues/2) · [análise 007](docs/proposals/007-analisis-de-costo-de-ejecucion-del-metodo.md) |
| **Editar o arquivo que o agente lê não é detectado** | É a quarta de quatro vias pelas quais o método pode ficar sem efeito. As outras três estão fechadas | [#3](https://github.com/dacunao/software-humano-speckit/issues/3) · [proposta 010](docs/proposals/010-evaluacion-del-piloto-del-sitio.md) |
| **O bundle não pode ser instalado** | O Spec Kit resolve componentes a partir de catálogos, não de caminhos locais. A quarta camada existe e não funciona | [#4](https://github.com/dacunao/software-humano-speckit/issues/4) |
| **Nenhum comando propaga uma mudança do fundamento** | No primeiro site o fundamento mudou seis vezes, e a especificação e o plano foram refeitos à mão nas seis | [#5](https://github.com/dacunao/software-humano-speckit/issues/5) · [proposta 010](docs/proposals/010-evaluacion-del-piloto-del-sitio.md) |
| **O pacote existe apenas em espanhol** | É deliberado — a doutrina tem sua autoridade em espanhol — e é um limite real de adoção | [#6](https://github.com/dacunao/software-humano-speckit/issues/6) |
| **Registro no catálogo do Spec Kit** | Desbloqueia o bundle e torna o método descobrível | [#7](https://github.com/dacunao/software-humano-speckit/issues/7) |

## Como se decide o que entra

Um tema entra nesta lista quando **algo o mediu**: um piloto, um ensaio, ou uma análise com sua evidência. Não entra por parecer uma boa ideia.

E sai da lista quando é aplicado **com decisão da autoridade de produto**. O registro de cada decisão vive em [`docs/proposals/`](docs/proposals/), que se acrescenta e não se reescreve.

## Como participar

As [issues](https://github.com/dacunao/software-humano-speckit/issues) estão abertas. Se você usa o método e algo atrapalha, conte lá: **o que se mede entra nesta lista.**

Os quatro temas que mais dizem sobre o método saíram de um projeto real usando-o, não de planejá-lo.
