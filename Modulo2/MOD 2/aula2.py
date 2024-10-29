# frutas = set()
# frutas.update({'maça', 'banana', 'uva', 'laranja', 'morango'})
# print('banana' in frutas)

# frutas_vermelhas = set()
# frutas_vermelhas.update(['morango', 'cereja', 'framboesa'])
# print(frutas_vermelhas)


# frutas_vermelhas = set()
# frutas_vermelhas.update(['morango', 'cereja', 'framboesa'])
# frutas_vermelhas.discard('cereja')
# print(frutas_vermelhas)


# conjunto_a = {'1,2'}
# conjunto_b = {'3,4'}
# print(conjunto_a | conjunto_b)


# conjunto1 = {'Mauro', 'Clara', 'João'}
# conjunto2 = {'Paulo', 'João', 'José'}
# print(conjunto1.intersection(conjunto2))


# lista1 = ['Mauro', 'Clara', 'João']
# lista2 = ['Paulo', 'João', 'José']
# lista1 = set(lista1)
# lista2 = set(lista2)
# print(lista1.union(lista2))



# dados_usuario = {
#     'Nome': 'José',
#     'Idade': 32
# }
# print(dados_usuario)


# dados_usuario = {
#     'Nome': 'José',
#     'Idade': 32
# }
# for chave, valor in dados_usuario.items():
#     print(f'{chave} é {valor}')



# dados = {
#     'Nome': input('Digite seu nome: '),
#     'Idade': int(input('Digite sua idade: '))
# }
# for chave, valor in dados.items():
#     print(f'{chave} é {valor}')


dados = {
    'Nome': input('Digite seu nome: '),
    'Idade': int(input('Digite sua idade: ')),
    'Cidade': 'Recife'
}
dados['Cidade'] = input('Digite a cidade: ')
print(dados)