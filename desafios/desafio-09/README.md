# Desafio 09 — Sistema de Frota

**Aula:** 09 | **Tema:** Herança e Polimorfismo
**Prazo:** até o final da Aula 09

---

## Enunciado

Crie um arquivo `solucao.py` com um ecossistema de transporte:
1. Classe pai `Veiculo` com atributos `marca` e `ano`.
2. Classes filhas `Caminhao` (adicione `capacidade_carga`) e `Moto` (adicione `cilindradas`).
3. Sobrescreva `exibir_dados()` em cada filha usando `super()`.
4. Proteja `__quilometragem` e exponha apenas via método `rodar(km)`.

---

## Pergunta Obrigatória (responda em `explicacao.md`)

> Por que `Caminhao` e `Moto` 'herdam de' `Veiculo` e não simplesmente repetem os atributos? O que você ganha e o que arrisca ao usar herança?

---

## Critérios de Avaliação

| Critério | Pontos |
|---|---|
| solucao.py entregue e sem erros de sintaxe | 4 |
| Herança correta com super(), polimorfismo e encapsulamento | 3 |
| explicacao.md com resposta autoral à pergunta obrigatória | 3 |
| **Total** | **10** |
