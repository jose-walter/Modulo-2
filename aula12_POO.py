# class Micoondas:
#     def __init__(self, tamanho, botoes, espaço_interno, voltagem, potencia):
#         self.tamanho = tamanho
#         self.botoes = botoes
#         self.espaço_interno = espaço_interno
#         self.voltagem = voltagem
#         self.potencia = potencia
#         self.ligado = False

#     def ligar(self):
#         if not


# class Pessoa:
#     def __init__(self, nome, endereco):
#         self.nome = nome
#         self.endereco = endereco

#     def mostrar_nome(self):
#         print(f'O nome é: {self.nome}')

#     def mostrar_endereco(self):
#         print(f'O endereço é {self.endereco}')

# class PessoaFisica(Pessoa):
#     def __init__(self, nome, endereco, cpf):
#         super().__init__(nome, endereco)
#         self.cpf = cpf


# class PessoaJuridica(Pessoa):
#     def __init__(self, nome, endereco, cnpj):
#         super().__init__(nome, endereco)
#         self.cnpj = cnpj

# walter = PessoaFisica('Walter', 'Ibura', '65089698536')
# walter.mostrar_nome()
# walter.mostrar_endereco()

# riothey = PessoaJuridica('Riothey', 'Recife', '25326666000152')
# riothey.mostrar_nome()
# riothey.mostrar_endereco()


# import math

# class Forma:
#     def __init__(self, cor, preenchimento):
#         self.cor = cor
#         self.preenchimento = preenchimento
        
# class Circulo(Forma):
#     def __init__(self, cor, preenchimento, raio):
#         super().__init__(cor, preenchimento)
#         self.raio = raio

#     def calcular_area_cir(self):
#         area = math.pi * (self.raio ** 2)
#         return area
    
#     def calcular_perimetro_cir(self):
#         per = 2 * math.pi * self.raio
#         return per

# class Retangulo(Forma):
#     def __init__(self, cor, preenchimento, base, altura):
#         super().__init__(cor, preenchimento)
#         self.base = base
#         self.altura = altura

#     def calcular_area_ret(self):
#         area = self.base * self.altura
#         return area
    
#     def calcular_perimetro_ret(self):
#         per = 2 * self.base + 2 * self.altura
#         return round(per, 2)

# # redondo = Circulo('Vermelho', True, 4)
# # print(redondo.calcular_area_cir())

# quadrado = Retangulo('Verde', True, 8, 5)
# print(quadrado.calcular_perimetro_ret())



# class Animal:
#     def fazer_som(self):
#         pass

# class Cachorro(Animal):
#     def fazer_som(self):
#         return 'Au Au'
    
# class Gato(Animal):
#     def fazer_som(self):
#         return 'Miau'
    
# class Pato(Animal):
#     def fazer_som(self):
#         return 'Quá Quá'
    
# def fazer_animal_falar(animal):
#     return animal.fazer_som()

# caramelo = Cachorro()
# tom = Gato()
# tiao = Pato()

# animais = [caramelo, tom, tiao]


# for animal in animais:
#     print(f'{animal.__class__.__name__} faz {fazer_animal_falar(animal)}')




class Veiculo:
    def __init__(self, acelerar, frear):
        self.acelerar = acelerar
        self.frear = frear


class Carro(Veiculo):
    def __init__(self, acelerar, frear,):
        super().__init__(acelerar, frear)