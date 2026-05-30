# Desafio 05 — Gerenciador de Compras
# Aluno: (André)
# Data:  (29/05)

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