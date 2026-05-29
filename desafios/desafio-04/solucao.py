# Desafio 04 — Tabuada Personalizada
# Aluno: (André Phylyp)
# Data:  (27/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

print("====== tabuada ======")

while True:
    try:
        numero = int(input("\nDigite o número para gera a tabuada: "))

        if numero == 0:
            print("\nFechamos o programa aqui! ")
            break

        if numero > 0:
            for i in range(1,11):
                resultado = numero * i
                print(f"{numero} * {i} = {resultado}")
        else:
            print("Digite um valor inteiro ")
    except:
        print("A entrada invalida")