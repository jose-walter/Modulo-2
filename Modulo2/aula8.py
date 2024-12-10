# cores = {'azul', 'verde', 'branco', 'amarelo', 'vermelho'}

# def verificar_cores(conjunto):
#     lista = []
#     for cor in conjunto:
#         if len(cor) > 4:
#             lista.append(cor)
#     return lista
# print(verificar_cores(cores))



# numeros = [51,92,63,44,65,100,68,66]
# nova_lista = []
# for numero in numeros:
#     if numero % 2 == 0:
#         nova_lista.append(numero)
# print(nova_lista)



# Crie um dicionário com informações de produtos,
# incluindo nome, preço e quantidade em estoque.
# Implemente funções para adicionar, remover e atualizar produtos no dicionário.

# lista_de_produtos = {}
# while True:
#     nome = input('Informe o nome do produto: '),
#     preço = float(input('Informe o preço do produto: ')),
#     quantidade = int(input('Informe a quantidade em estoque: ')) 
#     lista_de_produtos[nome]= [preço, quantidade]
#     adicionar = input('Quer continuar adicionando(s/n): ').strip().lower()
#     if adicionar == 'n':
#         break
# print(lista_de_produtos)





dados_producao = [
    {'ano': 2020, 'fazenda': 'Fazenda A', 'cultura': 'Milho', 'produção': 500},
    {'ano': 2020, 'fazenda': 'Fazenda B', 'cultura': 'Soja', 'produção': 300},
    {'ano': 2020, 'fazenda': 'Fazenda C', 'cultura': 'Trigo', 'produção': 400},
    {'ano': 2021, 'fazenda': 'Fazenda A', 'cultura': 'Milho', 'produção': 600},
    {'ano': 2021, 'fazenda': 'Fazenda B', 'cultura': 'Soja', 'produção': 450},
    {'ano': 2021, 'fazenda': 'Fazenda C', 'cultura': 'Trigo', 'produção': 500},
    {'ano': 2022, 'fazenda': 'Fazenda A', 'cultura': 'Milho', 'produção': 550},
    {'ano': 2022, 'fazenda': 'Fazenda B', 'cultura': 'Soja', 'produção': 700},
    {'ano': 2022, 'fazenda': 'Fazenda C', 'cultura': 'Trigo', 'produção': 350},
    {'ano': 2023, 'fazenda': 'Fazenda A', 'cultura': 'Milho', 'produção': 620},
    {'ano': 2023, 'fazenda': 'Fazenda B', 'cultura': 'Soja', 'produção': 400},
    {'ano': 2023, 'fazenda': 'Fazenda C', 'cultura': 'Trigo', 'produção': 480},
    {'ano': 2024, 'fazenda': 'Fazenda A', 'cultura': 'Milho', 'produção': 700},
    {'ano': 2024, 'fazenda': 'Fazenda B', 'cultura': 'Soja', 'produção': 650},
    {'ano': 2024, 'fazenda': 'Fazenda C', 'cultura': 'Trigo', 'produção': 520}
]
