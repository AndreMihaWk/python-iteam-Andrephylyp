# Desafio 03 — Sistema de Multas
# Aluno: (André Phylyp)
# Data:  (26/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

velocidade = float(input("Digite a velocidade do veículo (km/h): "))

if velocidade > 80:
    print("Você execdeu o limite de velocidade de 80KM/h")


    multa = (velocidade - 80) * 7 
    print(f"Multa: R$ {multa:.2f}")
else:
    print("Boa viagem! Dirija com segurança.")        
