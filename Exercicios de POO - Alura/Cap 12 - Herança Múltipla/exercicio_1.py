# @title Mix-Ins: uma classe que não se destina a ser independente - existe para adicionar funcionalidade extra a outra classe através de herança múltipla.

# SISTEMA DE CÁLCULO DE IMPOSTOS PARA CB E SV


class TributavelMixIn:
    def get_valor_imposto(
        self,
    ):  # Obriga que quem herdar tenha o método get_valor_imposto
        raise NotImplementedError(
            "Subclasses devem implementar get_valor_imposto"
        )  # Sinaliza erro ou exceção


class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self._numero = numero
        self._titular = titular
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


class ContaCorrente(Conta, TributavelMixIn):  # Herda duas classes
    def get_valor_imposto(self):
        return self._saldo * 0.01


class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05


class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()  # Pega tudo da lista e soma
        return total


# EXEMPLO DE USO:

if __name__ == "__main__":
    cc1 = ContaCorrente("123-4", "João", 1000.0)
    cc2 = ContaCorrente("567-8", "José", 2000.0)
    seguro1 = SeguroDeVida(100.0, "José", "345-77")
    seguro2 = SeguroDeVida(200.0, "Maria", "237-98")

    lista_tributaveis = [cc1, cc2, seguro1, seguro2]

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(f"Total de impostos: R${total:.2f}")
