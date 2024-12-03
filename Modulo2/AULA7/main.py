# # import modulos as md
# from utilidades.modulos import *

# lista =[]
# item = input('Digite algo: ')
# nova_lista = adicionar_item(item, lista)
# print(nova_lista)



# from modulos import *

# while True:
#     print('-------------------------')
#     print('Escolha a operação: ')
#     print('1- Adição')
#     print('2- subtração')
#     print('3- Multiplicação')
#     print('4- Divisão')
#     print('5- Sair')
#     print('-------------------------')
#     opção = int(input('Digite uma opção: '))
    
#     if opção == 5:
#         break

#     numero1 = int(input('Digite o primeiro número: '))
#     numero2 = int(input('Digite o segundo número: '))

#     if opção == 1:
#        resultado = soma(numero1, numero2)
#        print(f'{numero1} + {numero2} = {resultado}')
#     elif opção == 2:
#         resultado = subtração(numero1, numero2)
#         print(f'{numero1} - {numero2} = {resultado}')
#     elif opção == 3:
#         resultado = multiplicação(numero1, numero2)
#         print(f'{numero1} x {numero2} = {resultado}')
#     elif opção == 4:
#         resultado = divisão(numero1, numero2)
#         print(f'{numero1} / {numero2} = {resultado}')            





from random

numero_correto = random.rand

while True:
    print('Acerte o numero correto.')
    computador = randint(1,10)
    if computador > 5:
        print('O numero correto é maior que 5.')
    elif computador <= 5:

    tentativa = int(input('Digite a sua tentativa: '))
    if tentativa == computador:
        print('Parabens voce acertou!')