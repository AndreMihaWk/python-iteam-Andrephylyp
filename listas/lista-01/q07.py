# Lista 01 — Questão 07: Progressão e Análise
# Aluno: (seu nome)
# Data:  (data)

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────


notas = []


while len(notas) < 10:
    numero = len(notas) + 1  

    while True:  
        try:
            nota = float(input(f"Digite a nota {numero}/10: "))
            if nota < 0.0 or nota > 10.0:
                print("Nota fora do intervalo! Digite entre 0.0 e 10.0.")
            else:
                notas.append(nota)  
                break  
        except ValueError:
            
            print("Valor inválido! Digite um número (ex: 7.5).")


maior = notas[0]
menor = notas[0]
soma  = 0.0

for nota in notas:
    soma += nota
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

media = soma / len(notas)

acima_da_media = 0
for nota in notas:
    if nota > media:
        acima_da_media += 1


if media >= 7.0:
    classificacao = "Aprovado"
elif media >= 5.0:
    classificacao = "Recuperação"
else:
    classificacao = "Reprovado"



print(f"Notas digitadas : {notas}")
print(f"Maior nota      : {maior:.1f}")
print(f"Menor nota      : {menor:.1f}")
print(f"Média           : {media:.2f}")
print(f"Acima da média  : {acima_da_media} aluno(s)")
print(f"Classificação   : {classificacao}")
