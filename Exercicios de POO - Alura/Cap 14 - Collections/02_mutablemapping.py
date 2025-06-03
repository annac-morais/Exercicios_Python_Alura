from collections.abc import (
    MutableMapping,
)  # MutableMapping funciona como um dicionário mutável, ou seja, você pode armazenar pares chave: valor.
import csv  # arquivo de texto simples que armazena dados tabulares


# Classe Conta básica
class Conta:
    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def get_valor_imposto(self):
        # Exemplo: 1% do saldo como imposto
        return self.saldo * 0.01

    def __repr__(self):  # facilita a impressão para debugging.
        return f"<Conta {self.numero} de {self.titular}, saldo={self.saldo}>"


# Classe Contas que implementa MutableMapping (como um dicionário)
class Contas(MutableMapping):
    def __init__(self):
        self._dados = {}

    def __getitem__(self, chave):
        return self._dados[chave]

    def __setitem__(self, chave, valor):
        if not isinstance(valor, Conta):
            raise TypeError("valor atribuído não é uma Conta")
        self._dados[chave] = valor

    def __delitem__(self, chave):
        del self._dados[chave]

    def __iter__(self):
        return iter(self._dados)

    def __len__(self):
        return len(self._dados)

    def __repr__(self):
        return f"{self.__class__.__name__}({self._dados})"


# EXEMPLO DE USO:

if __name__ == "__main__":
    contas = Contas()

    c1 = Conta("João", "123-4", 1200.0)
    c2 = Conta("Maria", "567-8", 2500.0)
    contas[c1.numero] = c1
    contas[c2.numero] = c2

    print(f"Total de contas: {len(contas)}")

    # Acessar conta pelo número
    conta_joao = contas["123-4"]
    print(
        f"Conta do João: saldo={conta_joao.saldo}, imposto={conta_joao.get_valor_imposto()}"
    )

    # Iterar e imprimir saldo e imposto de todas as contas
    for numero in contas:
        conta = contas[numero]
        print(f"{numero}: saldo={conta.saldo}, imposto={conta.get_valor_imposto()}")

    # Leitura do arquivo CSV (contas.txt) e carregamento na estrutura Contas
    # O arquivo 'contas.txt' deve ter linhas com: titular,numero,saldo
    try:
        with open("contas.txt", "r") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                titular, numero, saldo = linha[0], linha[1], float(linha[2])
                conta = Conta(titular, numero, saldo)
                contas[numero] = conta
    except FileNotFoundError:
        print("Arquivo 'contas.txt' não encontrado. Pule a leitura do arquivo.")

    print("\nContas carregadas do arquivo:")
    for conta in contas.values():
        print(conta)
