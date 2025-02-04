class Conta:
    def __init__(self, numero_conta, titular_conta):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = 0

class Conta_Corrente(Conta):
    def __init__(self, numero_conta, titular_conta, deposito, exibir_saldo, manutencao):
        super().__init__(numero_conta, titular_conta)
        self.deposito = deposito
        self.exibir_saldo = exibir_saldo
        self.manutencao = manutencao

class Conta_Poupanca(Conta):
    def __init__(self, numero_conta, titular_conta,tx_juros):
        super().__init__(numero_conta, titular_conta)
