"""
=============================================================
 SISTEMA DE URNA ELETRÔNICA - PROJETO INTEGRADOR (A3)
 Módulo 07 - Programação em Python
 Paradigma: Programação Orientada a Objetos (POO)
=============================================================

Recursos implementados:
- Herança (Pessoa -> Candidato / Eleitor)
- Encapsulamento (atributos protegidos e privados + @property)
- Tratamento de exceções (try/except em todas as entradas)
- Menu interativo, gráfico ASCII e persistência em .txt (bônus)
"""

from abc import ABC, abstractmethod


# ============================================================
# CLASSE BASE (Herança + Abstração)
# ============================================================
class Pessoa(ABC):
    """Classe base abstrata que representa uma pessoa do sistema."""

    def __init__(self, identificador, nome):
        self._identificador = identificador   # atributo protegido
        self._nome = nome

    @property
    def identificador(self):
        return self._identificador

    @property
    def nome(self):
        return self._nome

    @abstractmethod
    def descricao(self):
        """Cada subclasse implementa sua própria descrição (polimorfismo)."""
        pass


# ============================================================
# CLASSE CANDIDATO (herda de Pessoa)
# ============================================================
class Candidato(Pessoa):
    """Representa um candidato. O número é usado como identificador."""

    def __init__(self, numero, nome, partido):
        super().__init__(numero, nome)
        self._partido = partido
        self.__votos = 0           # atributo PRIVADO (name mangling)

    @property
    def numero(self):
        return self._identificador

    @property
    def partido(self):
        return self._partido

    @property
    def votos(self):
        """Getter: votos só podem ser lidos, não alterados diretamente."""
        return self.__votos

    def registrar_voto(self):
        """Único meio de incrementar os votos (proteção do dado)."""
        self.__votos += 1

    def descricao(self):
        return f"[{self.numero}] {self.nome} — {self._partido}"

    def __str__(self):
        return self.descricao()


# ============================================================
# CLASSE ELEITOR (herda de Pessoa)
# ============================================================
class Eleitor(Pessoa):
    """Representa um eleitor habilitado a votar."""

    def __init__(self, id_eleitor, nome):
        super().__init__(id_eleitor, nome)
        self.__ja_votou = False    # atributo PRIVADO

    @property
    def id_eleitor(self):
        return self._identificador

    @property
    def ja_votou(self):
        return self.__ja_votou

    def registrar_participacao(self):
        """Marca o eleitor como já tendo votado (não reversível)."""
        self.__ja_votou = True

    def descricao(self):
        status = "já votou" if self.__ja_votou else "não votou"
        return f"Eleitor {self.id_eleitor} - {self.nome} ({status})"


# ============================================================
# EXCEÇÕES PERSONALIZADAS
# ============================================================
class EleitorNaoEncontradoError(Exception):
    pass


class EleitorJaVotouError(Exception):
    pass


class CandidatoInvalidoError(Exception):
    pass


# ============================================================
# CLASSE URNA (sistema principal)
# ============================================================
class Urna:
    """
    Classe principal que gerencia candidatos, eleitores e a votação.
    Os dicionários internos são privados para garantir o encapsulamento.
    """

    def __init__(self):
        self.__candidatos = {}     # numero -> Candidato (privado)
        self.__eleitores = {}      # id     -> Eleitor   (privado)
        self.__total_votos = 0
        self.__brancos = 0
        self.__nulos = 0

    # ---------------- Cadastro ----------------
    def cadastrar_candidato(self, candidato):
        
        if candidato.numero in self.__candidatos:
            raise ValueError(f"Já existe candidato com o número {candidato.numero}.")
        self.__candidatos[candidato.numero] = candidato

    def cadastrar_eleitor(self, eleitor):
        if eleitor.id_eleitor in self.__eleitores:
            raise ValueError(f"Eleitor {eleitor.id_eleitor} já cadastrado.")
        self.__eleitores[eleitor.id_eleitor] = eleitor

    # ---------------- Listagem ----------------
    def listar_candidatos(self):
        print("\n----- CANDIDATOS DISPONÍVEIS -----")
        for c in self.__candidatos.values():
            print(c.descricao())
        print("[0] BRANCO")
        print("----------------------------------")

    # ---------------- Votação ----------------
    def votar(self, id_eleitor, numero_candidato):
        """
        Valida o eleitor e o candidato, registra o voto de forma sigilosa
        (o nome do eleitor NUNCA é associado ao candidato escolhido).
        """
        # 1) valida eleitor
        eleitor = self.__eleitores.get(id_eleitor)
        if eleitor is None:
            raise EleitorNaoEncontradoError(
                f"Identificação '{id_eleitor}' não encontrada no cadastro."
            )

        # 2) verifica se já votou
        if eleitor.ja_votou:
            raise EleitorJaVotouError(
                f"O eleitor '{id_eleitor}' já registrou seu voto."
            )

        # 3) registra o voto (branco, válido ou inválido)
        if numero_candidato == 0:
            self.__brancos += 1
            resultado = "Voto em BRANCO registrado."
        elif numero_candidato in self.__candidatos:
            self.__candidatos[numero_candidato].registrar_voto()
            resultado = "Voto registrado com sucesso."
        else:
            raise CandidatoInvalidoError(
                f"Não existe candidato com o número {numero_candidato}."
            )

        # 4) atualiza status do eleitor e o total
        eleitor.registrar_participacao()
        self.__total_votos += 1
        return resultado

    # ---------------- Apuração ----------------
    def apuracao(self, salvar_arquivo=True):
        """Gera e exibe o relatório final da eleição."""
        linhas = []
        linhas.append("=" * 45)
        linhas.append("           RELATÓRIO DE APURAÇÃO")
        linhas.append("=" * 45)

        total_habilitados = len(self.__eleitores)
        total_validos = sum(c.votos for c in self.__candidatos.values())

        participacao = (
            (self.__total_votos / total_habilitados * 100)
            if total_habilitados > 0 else 0
        )

        linhas.append(f"Total de eleitores habilitados : {total_habilitados}")
        linhas.append(f"Total de votos registrados     : {self.__total_votos}")
        linhas.append(f"Votos válidos                  : {total_validos}")
        linhas.append(f"Votos em branco                : {self.__brancos}")
        linhas.append(f"Percentual de participação     : {participacao:.1f}%")
        linhas.append("-" * 45)
        linhas.append("RESULTADO POR CANDIDATO (ordem decrescente):")
        linhas.append("")

        # ordena candidatos por votos (decrescente)
        ordenados = sorted(
            self.__candidatos.values(),
            key=lambda c: c.votos,
            reverse=True,
        )

        for c in ordenados:
            perc = (c.votos / total_validos * 100) if total_validos > 0 else 0
            barra = "█" * c.votos   # gráfico de barras ASCII (bônus)
            linhas.append(f"{c.nome:<15} | {c.votos:>2} votos "
                          f"({perc:5.1f}%) {barra}")

        linhas.append("-" * 45)

        # ---------------- Vencedor / Empate ----------------
        if total_validos == 0:
            linhas.append("Nenhum voto válido foi registrado.")
        else:
            maior = ordenados[0].votos
            vencedores = [c for c in ordenados if c.votos == maior]

            if len(vencedores) == 1:
                linhas.append(f">>> VENCEDOR: {vencedores[0].nome} "
                              f"({vencedores[0].votos} votos) <<<")
            else:
                nomes = ", ".join(c.nome for c in vencedores)
                linhas.append(f"EMPATE entre: {nomes}")
                linhas.append("O critério de desempate seria definido "
                              "pelo regulamento da eleição.")

        linhas.append("=" * 45)

        relatorio = "\n".join(linhas)
        print("\n" + relatorio)

        # ---------------- Persistência em arquivo (bônus) ----------------
        if salvar_arquivo:
            try:
                with open("resultado_eleicao.txt", "w", encoding="utf-8") as f:
                    f.write(relatorio)
                print("\n[Relatório salvo em 'resultado_eleicao.txt']")
            except OSError as e:
                print(f"\n[Não foi possível salvar o arquivo: {e}]")


# ============================================================
# DADOS PRÉ-CARREGADOS
# ============================================================
def carregar_dados():
    """Cria a urna com 3 candidatos e 5 eleitores pré-cadastrados."""
    urna = Urna()

    # Candidatos
    urna.cadastrar_candidato(Candidato(10, "André Silva", "Chapa Renovação"))
    urna.cadastrar_candidato(Candidato(20, "Ryan Kaio", "Chapa União"))
    urna.cadastrar_candidato(Candidato(30, "Guilherme Dias", "Chapa Avante"))

    # Eleitores (identificação -> nome)
    urna.cadastrar_eleitor(Eleitor("111", "João Pereira"))
    urna.cadastrar_eleitor(Eleitor("222", "Maria Santos"))
    urna.cadastrar_eleitor(Eleitor("333", "Pedro Alves"))
    urna.cadastrar_eleitor(Eleitor("444", "Lucas Costa"))
    urna.cadastrar_eleitor(Eleitor("555", "Júlia Rocha"))

    return urna


# ============================================================
# MENU INTERATIVO (bônus)
# ============================================================
def menu():
    urna = carregar_dados()

    while True:
        print("\n========== URNA ELETRÔNICA ==========")
        print("[1] Votar")
        print("[2] Listar candidatos")
        print("[3] Encerrar votação e apurar")
        print("[4] Sair sem apurar")
        print("=====================================")

        try:
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                id_eleitor = input("Digite sua identificação de eleitor: ").strip()
                urna.listar_candidatos()
                entrada = input("Digite o número do candidato (0 = branco): ").strip()

                # Validação de entrada numérica
                if not entrada.isdigit():
                    raise ValueError("O número do candidato deve conter apenas dígitos.")

                numero = int(entrada)
                print(">>", urna.votar(id_eleitor, numero))

            elif opcao == "2":
                urna.listar_candidatos()

            elif opcao == "3":
                urna.apuracao()
                print("\nVotação encerrada. Obrigado!")
                break

            elif opcao == "4":
                print("Saindo sem apurar...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        # Tratamento gracioso de todos os erros previstos
        except ValueError as e:
            print(f"[ERRO DE ENTRADA] {e}")
        except EleitorNaoEncontradoError as e:
            print(f"[ERRO] {e}")
        except EleitorJaVotouError as e:
            print(f"[ERRO] {e}")
        except CandidatoInvalidoError as e:
            print(f"[ERRO] {e}")
        except Exception as e:
            print(f"[ERRO INESPERADO] {e}")


# ============================================================
# PONTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    menu()