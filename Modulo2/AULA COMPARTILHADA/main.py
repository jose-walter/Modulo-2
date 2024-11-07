#LER O ARQUIVO E GERAR UM .CSV COM TODOS OS USUARIOS QUE TENHAM
#MAIS DE 30 ANOS

import csv

with open('csv/dados.csv', 'r', encoding='utf-8') as arquivo:
    reader = csv.DictReader(arquivo)
    dados = list(reader)

# soma = 0
# for pessoa in dados:
#     soma += int(pessoa['Idade'])
#     media = soma / len(dados)
# print(media)

# dados_saida = [
#     {'Nome': 'Média',
#      'Idade': media}
# ]

with open('output/saida.csv', 'w', encoding='utf-8') as arquivo:
    nomes_colunas = ['Nome', 'Idade']
    writer = csv.DictWriter(arquivo, fieldnames=nomes_colunas)
    writer.writeheader()
    writer.writerows(dados_saida)
print('Arquivo gerado com sucesso!')