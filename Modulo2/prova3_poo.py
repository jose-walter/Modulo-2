class ContaBancaria:
    def __init__(self,saldo, titular):        
        self.__titular = titular
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Depósito realizado com sucesso! Saldo R$: {self.__saldo}')
    
    def sacar(self, valor):
        if self.__saldo < valor:
            print(f'Saldo insuficiente! Saldo R$: {self.__saldo}')
            return
        self.__saldo -= valor
        print(f'Saque realizado com sucesso! Saldo R$: {self.__saldo}')

    def exibir_saldo(self):
        print(f'Saldo R$: {self.__saldo}')

conta = ContaBancaria(0, "Walter")
conta.depositar(1000)
conta.sacar(100)
conta.exibir_saldo()