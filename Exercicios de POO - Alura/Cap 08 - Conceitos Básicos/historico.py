# @title Desafio: Crie uma classe Historico que represente o histórico de uma Conta seguindo o exemplo acima


class Historico:
    def __init__(self):
        self.transacoes = []  # Lista das transações realizadas

    def nova_transacao(self, operacao):
        self.transacoes.append(operacao)  # Add no final da lista

    def mostrar(self):
        print("Histórico de transações:")
        for t in self.transacoes:
            print("-", t)


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()  # Cria histórico para esta conta

    def deposita(self, valor):
        self.saldo += valor
        self.historico.nova_transacao(f"Depósito de R${valor:.2f}")

    def saca(self, valor):
        self.saldo -= valor
        self.historico.nova_transacao(f"Saque de R${valor:.2f}")

    def extrato(self):
        print(f"Conta: {self.numero} - Saldo: R${self.saldo:.2f}")

    def mostrar_historico(self):
        self.historico.mostrar()


# EXEMPLO DE USO
if __name__ == "__main__":
    conta1 = Conta("123-7", "João", 500.0, 1000.0)
    conta1.deposita(100.0)
    conta1.saca(50.0)
    conta1.extrato()
    conta1.mostrar_historico()
