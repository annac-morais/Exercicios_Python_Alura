# @title Criando nossa Sequência:

from collections.abc import (
    MutableSequence,
)  # importa uma classe abstrata que define o comportamento de uma sequência mutável, tipo uma lista customizada


class Conta:
    def __init__(self, titular, numero, saldo=0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def get_valor_imposto(self):
        return 0


class ContaCorrente(Conta):
    def get_valor_imposto(self):
        return self.saldo * 0.01


class Contas(MutableSequence):
    _dados = []

    def __len__(self):
        return len(self._dados)  # Retorna quantos itens tem

    def __getitem__(self, posicao):
        return self._dados[posicao]  # Pega um item da lista (como contas[0])

    def __setitem__(self, posicao, valor):
        if isinstance(valor, Conta):
            self._dados[posicao] = (
                valor  # Substitui um item, mas antes verifica se o valor é uma Conta
            )
        else:
            raise TypeError("valor atribuído não é uma Conta")

    def __delitem__(self, posicao):
        del self._dados[posicao]  # Remove um item

    def insert(self, posicao, valor):
        if isinstance(valor, Conta):
            self._dados.insert(
                posicao, valor
            )  # Insere um item em uma posição, com a mesma verificação
        else:
            raise TypeError("valor inserido não é uma Conta")


# EXEMPLO DE USO:

if __name__ == "__main__":
    contas = Contas()
    contas.append(ContaCorrente("João", "123-4", 1200.0))
    contas.append(ContaCorrente("Maria", "234-5", 2200.0))
    contas.append(ContaCorrente("Ana", "345-6", 1500.0))

    print("saldo - imposto")
    for conta in contas:
        print(f"{conta.saldo} - {conta.get_valor_imposto()}")
