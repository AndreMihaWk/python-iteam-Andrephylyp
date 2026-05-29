# Desafio 02 — Calculadora de IMC
# Aluno: (André Phylyp)
# Data:  (20/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────


nomeusuario = str(input("Digite o seu nome: "))

peso = int(input("Qual seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura**2)


print(f"Olá {nomeusuario}, seu IMC é {imc:.2f}")