**Português (BR)** · [English](README.md) · [Español](README.es.md)

# Software Humano para SpecKit

> Construímos ferramentas para ampliar a capacidade das pessoas, não para exibir a capacidade do software.

Pacote de método que aplica o **Manifesto de Software Humano** ao ciclo de desenvolvimento guiado por especificação do [SpecKit](https://github.com/github/spec-kit), em qualquer projeto.

**Leia o manifesto:** [manifiesto.softwarehumano.com](https://manifiesto.softwarehumano.com)

> **Sobre o idioma.** O manifesto está publicado em inglês, espanhol e português do Brasil no site. **Este pacote — seus documentos, instruções, mensagens das ferramentas e comentários — está escrito apenas em espanhol.** Se você trabalha com uma equipe que não o lê, o manifesto está traduzido; o pacote não.

---

## O manifesto

O **Núcleo do manifesto para o desenvolvimento de software humano com inteligência artificial**, de **Damián Acuña**, responde a uma pergunta:

> Como construímos software que amplie a capacidade das pessoas de conseguir o que buscam, **sem transferir a elas a complexidade da tecnologia**?

Construir um produto tem um custo, e esse custo não desaparece: ele se reparte. Uma parte é paga pela equipe; a outra é repassada a quem usa o produto, em atenção, em aprendizado e em decisões que a pessoa não veio tomar. Esse repasse quase nunca é decidido.

Daí decorrem suas afirmações menos habituais: que um produto sem erros pode fracassar por saturação, que a complexidade pertence ao sistema e não à interface, e que a atenção tem orçamento e se verifica como se verifica o desempenho.

O texto completo está em [`docs/method/`](docs/method/Manifiesto_Software_Humano_IA_Nucleo_v2.1.md) (em espanhol) e no [site](https://manifiesto.softwarehumano.com). É a fonte de autoridade do resto.

## Para que tipo de produtos

O próprio manifesto declara seu escopo:

> O marco serve para produtos em que a experiência de uso influencia diretamente o resultado: **aplicações web e móveis, ferramentas internas, sistemas de aprendizagem, serviços digitais, produtos com agentes e soluções assistidas por IA.** Dirige-se a product managers, designers, desenvolvedores e agentes de código que participam de decisões de produto.

Se a experiência de uso não muda o resultado do que você constrói, este método vai cobrar mais do que devolve.

## O que o pacote faz

Um manifesto não se aplica sozinho. Um agente com a doutrina disponível pode omiti-la sem que nada o detenha, e sem que ninguém perceba até o produto já estar construído.

Este pacote coloca as disposições do manifesto **dentro dos comandos que a equipe já executa**, citando seu texto literal, sem reformulá-lo. De 300 enunciados verificáveis do núcleo, 210 estão compilados; 40 ficam declarados fora e 50 são editoriais.

Não modifica o SpecKit: usa quatro de seus mecanismos de extensão documentados.

## O que NÃO faz

**Não é um sistema de design nem um guia visual.** Não traz componentes, tipografias, paletas nem opiniões sobre como um produto deve parecer. Fixa critérios — acessibilidade, estados, carga, desempenho, rastreabilidade —, não estética. A direção visual é decisão da equipe.

**Não verifica que o produto esteja bom.** Verifica que o exigido pelo manifesto esteja presente e seja rastreável. Os comandos revisam a coerência entre artefatos e do código contra as tarefas; nenhum olha a tela. Se a experiência cumpre os princípios, quem julga é uma pessoa usando o produto.

**O método não substitui o teste com pessoas: torna-o exigível.**

## Começar

Você precisa de [SpecKit](https://github.com/github/spec-kit) `>=1.0.0,<2.0.0`, Python 3 com PyYAML, git e um agente de IA com integração do SpecKit.

```bash
# Baixe o pacote em Releases e descompacte no seu projeto
unzip software-humano-speckit-starter-vX.Y.Z.zip -d /tmp/sh
cp -R /tmp/sh/software-humano-speckit-starter-vX.Y.Z/. .

# Verifique que chegou íntegro e que o ambiente funciona
shasum -a 256 -c SHA256SUMS
tools/speckit/preflight.sh
```

Depois preencha a seção **Completar por proyecto** no fim de `AGENTS.md` e entregue ao seu agente o prompt de [`START_WITH_AI_AGENT.md`](package/START_WITH_AI_AGENT.md). O procedimento verificável, passo a passo, está em [`instructions/01`](package/instructions/01_INSTALAR_Y_VERIFICAR_SPECKIT.md).

> A instalação costuma exigir **duas sessões**: muitos agentes carregam seu catálogo de comandos ao iniciar, então os recém-instalados não existem até reabrir. É o esperado.

## O que inclui

| Camada | Mecanismo do SpecKit | O que aporta |
|---|---|---|
| Preset | `preset` | A doutrina dentro dos oito comandos e dos três modelos |
| Conformidade | `extension` | Verifica que o exigido esteja presente, e detém quando falta sem declarar |
| Comportas | `workflow` | Os pontos de controle que o próprio manifesto especifica, executados pelo motor |
| Distribuição | `bundle` | Compõe e fixa as três anteriores |

E a documentação: o núcleo, o anexo que traça cada disposição até o SpecKit, o guia de implementação, as instruções de instalação e [`PARA_QUIEN_DECIDE.md`](package/PARA_QUIEN_DECIDE.md), escrito para quem aprova e não para o agente.

## Dois modos, conforme seu jeito de trabalhar

**Comandos avulsos.** O agente invoca cada comando ao reconhecer a situação que ele nomeia, a partir de linguagem natural. Habilita a doutrina nos artefatos sem que ninguém digite nada; depende de o agente reconhecer o momento.

**Workflow.** Executa o ciclo completo de uma vez. Habilita, além disso, as comportas e a verificação de conformidade, que o motor executa e o agente não pode pular.

Nenhum é «o certo». Quem trabalha conversando e decidindo a cada turno vai se apoiar no primeiro; quem quer o ciclo fechado, ou o executa em integração contínua, no segundo. Os dois ficam instalados e podem ser alternados.

## Licenças

O pacote mistura duas naturezas, e a fronteira se define por natureza e não por pasta:

| O quê | Licença |
|---|---|
| Preset, extensão, workflow, bundle, ferramentas e instruções | [MIT](LICENSE) |
| Texto do núcleo do manifesto, incluída sua projeção como constituição | [CC BY 4.0](LICENSE-CONTENT) |

Qual arquivo cai de que lado está explicado em [`LICENSING.md`](LICENSING.md). Atribuição sugerida para o texto:

> «Núcleo del manifiesto para el desarrollo de software humano con inteligencia artificial v2.1», de Damián Acuña, sob licença CC BY 4.0.

## Autoria

Manifesto e método de **Damián Acuña**. O desenvolvimento do pacote foi feito com assistência de Claude, sob sua autoria e decisão.

## Roteiro

O que sabemos que falta está à vista, com uma issue por tema: [ROADMAP.pt-BR.md](ROADMAP.pt-BR.md).

Um tema entra nessa lista quando algo o mediu —um piloto, um ensaio, uma análise com sua evidência— e sai quando uma decisão da autoridade de produto o aplica. Se você usa o método e algo atrapalha, as [issues](https://github.com/dacunao/software-humano-speckit/issues) estão abertas.

## Como é mantido

`docs/proposals/` é o registro de manutenção: acrescenta-se, não se reescreve. Cada proposta distingue fato observado, inferência e decisão humana requerida, e nenhuma se aplica sem decisão da autoridade de produto.

O método é validado em projetos reais, e seus achados são avaliados aqui antes de mudar qualquer coisa.
