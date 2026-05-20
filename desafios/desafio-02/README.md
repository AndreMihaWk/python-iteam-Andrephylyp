# Desafio 02 — Calculadora de IMC

**Aula:** 02 | **Tema:** Operadores e Tipos de Dados
**Prazo:** até o final da Aula 02

---

## Enunciado

Crie um script `solucao.py` que:
1. Solicite o nome do usuário.
2. Solicite o peso (kg) e a altura (m).
3. Calcule o IMC: peso ÷ altura².
4. Exiba: `"Olá {nome}, seu IMC é {valor_imc:.2f}"`.

---

## Pergunta Obrigatória (responda em `explicacao.md`)

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?
 
 _quando usamos o 'float()' indicamos para 'input()' que receberemos todo os tipos de números REAIS. Se fosse utilizar o 'int()' para indicar Kilo ou Altura iria dar um 'ValueError' pelo o número inserido não ser um ponto flutuante_
---

## Critérios de Avaliação

| Critério | Pontos |
|---|---|
| solucao.py entregue e sem erros de sintaxe | 4 |
| IMC calculado e exibido corretamente com 2 casas decimais | 3 |
| explicacao.md com resposta autoral à pergunta obrigatória | 3 |
| **Total** | **10** |
