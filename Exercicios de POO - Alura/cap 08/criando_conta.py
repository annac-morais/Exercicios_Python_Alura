# @title Criando uma Conta:


class Conta:
    def __init__(
        self, numero, titular, saldo, limite
    ):  # Método construtor init para inicializar os atributos da conta.
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):  # Método para depositar um valor na conta
        self.saldo += valor

    def saca(self, valor):  # Método para sacar um valor da conta.
        self.saldo -= valor

    def extrato(self):  # Método para exibir o extrato da conta.
        print(f"Número: {self.numero} \nSaldo: {self.saldo}")


# EXEMPLO DE USO
conta = Conta("123-7", "João", 500.0, 1000.0)

conta.deposita(50.0)
conta.extrato()  # saldo: 550.0

conta.saca(20.0)
conta.extrato()  # saldo: 530.0
