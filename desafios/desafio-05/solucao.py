# Desafio 05 — Gerenciador de Compras
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
produtos = []

while True:
    produto = input("Digite um produto (ou 'fim' para encerrar): ")

    if produto.lower() == "fim":
        break

    produtos.append(produto)

produtos.sort()

print("\nLista de produtos:")
for produto in produtos:
    print(f"  - {produto}")

print(f"\nTotal de itens: {len(produtos)}")