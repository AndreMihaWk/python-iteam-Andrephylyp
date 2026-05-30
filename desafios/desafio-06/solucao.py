# Desafio 06 — Bio-Cadastro
# Aluno: (André)
# Data:  (29/05)

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