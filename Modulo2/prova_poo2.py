# class Veiculo:
#     def movimentar(self):
#         print("Veículo esta em movimento.")

# class Carro(Veiculo):
#     def movimentar(self):
#         print("Carro está dirigindo.")

# class Moto(Veiculo):
#     def movimentar(self):
#         print("Moto está acelerando")

# veic = Veiculo()
# car = Carro()
# mot = Moto()

# veic.movimentar()
# car.movimentar()
# mot.movimentar()


class Pessoa: 

    def __init__(self, nome, idade): 
        self.__nome = nome 
        self.__idade = idade 
    def get_nome(self): 
        return self.__nome 



pessoa = Pessoa("Maria", 30) 

print(pessoa.get_nome())