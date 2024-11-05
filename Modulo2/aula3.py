# idade = int(input('Digite sua idade: '))
# if idade < 12:
#     print(f'Você tem {idade} anos, portanto é uma criança.')
# elif idade >= 12 and idade <= 17:
#     print(f'Você tem {idade} anos, portanto é um adolescente.')
# elif idade >=18 and idade <= 59:
#     print(f'Você tem {idade} anos, portanto é adulto.')
# else:
#     print(f'Você tem {idade} anos, portanto é idoso.')


# numero1 = int(input('Digite o primeiro número:'))
# numero2 = int(input('Digite o segundo número:'))
# numero3 = int(input('Digite o terceiro número:'))
# maior = None
# menor = None

# if numero1 > numero2 and numero1 > numero3:
#     maior = numero1
#     menor = numero3 if numero2 > numero3 else numero2

# elif numero2 > numero1 and numero2 > numero3:
#     maior = numero2
#     menor = numero3 if numero1 > numero3 else numero1

# else:
#     maior = numero3
#     menor = numero2 if numero1 > numero2 else numero1

# print (f"O maior número é {maior}.")
# print (f'O menor número é {menor}.')



# pares = 0
# impares = 0

# for numro in range(10):
#     numero = int(input('Digite um número interiro: '))
#     if numero %2 == 0:
#         pares += 1
#     else:
#         impares += 1

# print(f'Quatidade de números pares: {pares}')
# print(f'Quatidade de números ímpares: {impares}')



# soma = 0
# pessoas = int(input('Informe a quantidade de pessoas: '))
# for i in range(pessoas):
#     idade = int(input('Digite a idade: '))
#     soma += idade
#     media = soma / pessoas
# if media >=0 and media <= 25:
#     print(f'A média da turma é {media}. A turma é jovem.')
# elif media <=60:
#     print(f'A média da turma é {media}. A turma é adulta.')
# else:
#     print(f'A média da turma é {media}. Aturma é idosa.')



# conjunto = (10, 20, 30, 40, 50)
# print(f'O menor valor do confunto é: {min(conjunto)}')
# print(f'O maior valor do confunto é: {max(conjunto)}')
# print(f'A soma do conjunto é: {sum(conjunto)}')


# quantidade_produtos = 0
# total = 0 
# continuar = 'S'
# while continuar == 'S':
#     nome_produto = input('Digite o nome do produto: ')
#     valor_produto = float(input('Digite o valor do produto: '))
#     total += valor_produto
#     continuar = input('Deseja continuar? (S/N): ')
#     if valor_produto >= 1000:
#         quantidade_produtos += 1
    
# print(f'O total da compra foi de R${total}')
# print(quantidade_produtos)