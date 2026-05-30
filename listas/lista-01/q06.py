# Lista 01 — Questão 06: Validador de Senha
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────

tentativas = 0

while True:
    senha = input("Digite uma senha: ")
    tentativas += 1
    valida = True

   
    if len(senha) < 8:
        print(" A senha deve ter pelo menos 8 caracteres.")
        valida = False

   
    tem_digito = False
    for caractere in senha:
        if caractere.isdigit():
            tem_digito = True
    if not tem_digito:
        print("A senha deve conter pelo menos um número.")
        valida = False


    tem_maiuscula = False
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
    if not tem_maiuscula:
        print("A senha deve conter pelo menos uma letra maiúscula.")
        valida = False

    
    if valida:
        print(f"Senha válida após {tentativas} tentativa(s).")
        break