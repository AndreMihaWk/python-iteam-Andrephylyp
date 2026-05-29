# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────


nome = str(input("Digite aqui seu nome Completo: "))

cpf = str(input("Digite aqui seu CPF: "))



try:
    ano = int(input("Digite aqui seu ano de nascimento: "))
    altura = float(input("Digite aqui sua altura: "))

    idade = 2026 - ano
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    

except ValueError:
    print("Valor inválido para o ano de nascimento. Por favor, insira um número inteiro.")