# @title Interfaces e aulas Resumos:

# SISTEMA ANTERIOR SEM MIX-IN

import abc


class Tributavel(abc.ABC):
    """Classe que contém operações de um objeto tributável.

    As subclasses concretas devem sobrescrever o método get_valor_imposto.
    """

    @abc.abstractmethod
    def get_valor_imposto(self):
        """Aplica taxa de imposto sobre um determinado valor do objeto"""
        pass


class Conta:
    def __init__(self, titular, numero, saldo=0.0):
        self._titular = titular
        self._numero = numero
        self._saldo = saldo

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False

    def get_saldo(self):
        return self._saldo

    def __repr__(self):
        return f"<{self.__class__.__name__} de {self._titular}>"


class ContaCorrente(
    Conta
):  # As classes não herdam diretamente de Tributavel como antes
    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaPoupanca(Conta):
    pass


class SeguroDeVida:
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

    def __repr__(self):
        return f"<SeguroDeVida de {self._titular}>"


class ContaInvestimento(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def get_valor_imposto(self):
        return self._saldo * 0.03


class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.get_valor_imposto()
            else:
                print(f"{t} não é um tributável")
        return total


# EXEMPLO DE USO:

if __name__ == "__main__":
    cc = ContaCorrente("João", "123-4")
    cc.deposita(1000.0)

    seguro = SeguroDeVida(100.0, "José", "345-77")

    cp = ContaPoupanca("Maria", "123-6")

    ci = ContaInvestimento("Ana", "123-0")
    ci.deposita(100.0)

    # Registrando classes como tributáveis já que não herdam diretamente
    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    Tributavel.register(ContaInvestimento)
    # Se tem get_valor_imposto(), é tributável! Mas para o Python reconhecer, precisa registrar!

    lista_tributaveis = [cc, seguro, cp, ci]

    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)

    print(f"Total de impostos: R${total:.2f}")
