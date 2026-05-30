# Desafio 06 — Bio-Cadastro
# Aluno: (seu nome aqui)
# Data:  (data de entrega)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
equipe = []

while True:
    nome = input("Digite o nome (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    cargo = input("Digite o cargo: ")

    colaborador = {"nome": nome, "cargo": cargo}
    equipe.append(colaborador)

print("\nEquipe cadastrada:")
for colaborador in equipe:
    print(f"Funcionário: {colaborador['nome']} | Cargo: {colaborador['cargo']}")