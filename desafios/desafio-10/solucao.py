# Desafio 10 — Projeto Final — Urna Eletrônica
# Aluno: (André Silva)
# Data:  (29/05/2026)

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

from abc import ABC, abstractmethod


def __init__(self, identificador, nome):
    self._idetificador = identificador
    self._nome = nome
    
    @property
    def nome(self):
        return self.nome
    
    @abstractmethod
    def descricao(self):
        pass
        