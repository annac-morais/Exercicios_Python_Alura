import abc


class Conta(
    abc.ABC
):  # Sig que esta classe não pode ser instanciada diretamente. Ela serve como modelo para outras classes
    def __init__(self, numero, titular, saldo=0.0, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if valor <= self._saldo + self._limite:
            self._saldo -= valor
            return True
        return False

    @property
    def saldo(self):
        return self._saldo

    @abc.abstractmethod
    def atualiza(self, taxa):  # Toda subclasse tem que ter um método atualiza
        pass

    def __str__(self):
        tipo = getattr(self, "_tipo", "Conta")
        return (
            f"Tipo: {tipo}\n"
            f"Número: {self._numero}\n"
            f"Titular: {self._titular}\n"
            f"Saldo: {self._saldo:.2f}\n"
            f"Limite: {self._limite:.2f}"
        )


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)
        self._tipo = "Conta Corrente"

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)
        self._tipo = "Conta Poupança"

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo


class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo=0.0):
        super().__init__(numero, titular, saldo)
        self._tipo = "Conta Investimento"

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5
        return self._saldo


# Classe que atualiza contas
class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0.0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("Objeto passado não é uma instância de Conta")

        print(f"\nAtualizando: {conta._tipo}")
        print(f"Saldo antes: {conta.saldo:.2f}")
        self._saldo_total += conta.atualiza(self._selic)
        print(f"Saldo depois: {conta.saldo:.2f}")


if __name__ == "__main__":
    # EXEMPLO DE USO COM ERRO: Classe abstrata não pode ser instanciada
    try:
        c = Conta("000-0", "Erro", 1000.0)
    except TypeError as e:
        print(f"[Erro esperado] {e}")

    # Agora sem implementar atualiza()
    try:

        class ContaInvalida(Conta):
            pass

        ci = ContaInvalida("999-9", "Maria", 1000.0)
    except TypeError as e:
        print(f"[Erro esperado] {e}")

    # EXEMPLO REAL DE USO
    cc = ContaCorrente("123-4", "João", 1000.0)
    cp = ContaPoupanca("123-5", "José", 1000.0)

    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print("\n--- Após atualização ---")
    print(cc)
    print(cp)

    # Com método atualiza()
    ci = ContaInvestimento("123-6", "Maria", 1000.0)
    ci.deposita(1000.0)
    ci.atualiza(0.01)
    print("\n--- Conta Investimento ---")
    print(ci)
