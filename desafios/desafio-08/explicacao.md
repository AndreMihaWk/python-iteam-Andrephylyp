# Explicação — Desafio 08 — Banco Digital

**Aluno:** _(André)_
**Data:** _(29/05)_

---

## O que meu programa faz

_(Cria uma conta bancária com titular e saldo inicial, e permite fazer depósitos, saques e exibir o extrato — bloqueando saques se o saldo for insuficiente.)_

---

## Resposta à Pergunta Obrigatória

> Por que `saldo` deve ser um **atributo da instância** (`self.saldo`) e não uma variável comum dentro do método? O que mudaria no comportamento do programa?

_(pertence ao objeto ele é criado uma vez no __init__ e todos os métodos conseguem acessar e modificar o mesmo valor, Se fosse uma variável comum dentro de um método, ela existiria só enquanto aquele método roda e depois sumia. Cada método teria seu próprio saldo do zero, sem memória do que aconteceu antes.)_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
