# Desafio 08 — Banco Digital
# Aluno: (André)
# Data:  (29/05)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print(f"Saldo insuficiente. Saldo atual: R$ {self.saldo:.2f}")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")

    def exibir_extrato(self):
        print(f"\n     EXTRATO")
        print(f"Titular : {self.titular}")
        print(f"Saldo   : R$ {self.saldo:.2f}")



conta = ContaBancaria("Ricardo", 1000.00)
conta.exibir_extrato()

conta.depositar(500.00)
conta.sacar(200.00)
conta.sacar(2000.00)  

conta.exibir_extrato()