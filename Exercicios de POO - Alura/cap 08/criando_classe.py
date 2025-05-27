# @title Primeira classe Python:


# Classe que representa um cliente do banco
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __str__(self):  # Define como o objeto será exibido
        return f"{self.nome} {self.sobrenome} (CPF: {self.cpf})"  # Retorna uma string representando o cliente de forma legível


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"  # Data formatada no padrão DD/MM/AAAA


class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura

    def deposita(self, valor):
        # Adiciona um valor ao saldo da conta
        self.saldo += valor

    def saca(self, valor):
        # Verifica se o saque é possível considerando o limite
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        # Imprime as informações da conta, incluindo os dados do titular
        print(f"Número: {self.numero}")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Titular: {self.titular}")
        print(f"Data de Abertura: {self.data_abertura}")


# EXEMPLO DE USO

cliente1 = Cliente("João", "Silva", "123.456.789-00")
data_abertura = Data(19, 5, 2025)
conta1 = Conta("123-7", cliente1, 500.0, 1000.0, data_abertura)

print("\n- Depósito de R$50,00 -")
conta1.deposita(50.0)

print("\nExtrato:")
conta1.extrato()

print("\n- Saque de R$20,00 -")
conta1.saca(20.0)

print("\nExtrato:")
conta1.extrato()
