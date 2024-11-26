banco_de_dados = []

def adicionar_tarefa():
    tarefa = {
        'nome': input('Digite o nome da tarefa: '),
        'descrição': input('Digite a descrição da tarefa: '),
        'prioridade': int(input('Digite a prioridade (1-5): ')),
        'categoria': input('Digite a categoria da tarefa: '),
        'data': input('Digite a data (DD/MM/AAAA): '),
        'concluido': False
    }
    banco_de_dados.append(tarefa)
    print('Tarefa adicionada com sucesso!')

def listar_tarefa():
    for tarefa in banco_de_dados:
        print(f'Nome: {tarefa['nome']}')
        print(f'Descrição: {tarefa['descrição']}')
        print(f'Prioridade: {tarefa['prioridade']}')
        print(f'Categoria: {tarefa['categoria']}')
        print(f'Data: {tarefa['data']}')
        print(f'Concuido: {tarefa['concluido']}')
        print('---------------------')

def listar_por_prioridade():
    prioridade = int(input('Digite a prioridade da busca: '))
    for tarefa in banco_de_dados:
        if tarefa['prioridade'] == prioridade:
            print(f'Nome: {tarefa['nome']}')
            print(f'Descrição: {tarefa['descrição']}')
            print(f'Prioridade: {tarefa['prioridade']}')
            print(f'Categoria: {tarefa['categoria']}')
            print(f'Data: {tarefa['data']}')
            print(f'Concuido: {tarefa['concluido']}')
            print('---------------------')

def listar_por_categoria():
    categoria = int(input('Digite a categoria da busca: '))
    for tarefa in banco_de_dados:
        if tarefa['categoria'] == categoria:
            print(f'Nome: {tarefa['nome']}')
            print(f'Descrição: {tarefa['descrição']}')
            print(f'Prioridade: {tarefa['prioridade']}')
            print(f'Categoria: {tarefa['categoria']}')
            print(f'Data: {tarefa['data']}')
            print(f'Concuido: {tarefa['concluido']}')
            print('---------------------')

def deletar_tarefa():
    deletar = input('Digite a tarefa a ser deletada: ')
    for tarefa in banco_de_dados:
        if tarefa['nome'] == deletar:
            banco_de_dados.remove(tarefa)
            print('Tarefa removida com sucesso!')

while True:
    print('1- Adicionar tarefa')
    print('2- Listar tarefa')
    print('3- Listar por prioridade')
    print('4- Listar por categoria')
    print('5- Deletar tarefa')
    print('6-SAIR\n')

    opcao_escolhida = int(input('Opção: '))
    if opcao_escolhida == 1:
        adicionar_tarefa()
    elif opcao_escolhida == 2:
        listar_tarefa()
    elif opcao_escolhida == 3:
        listar_por_prioridade()
    elif opcao_escolhida == 4:
        listar_por_categoria()
    elif opcao_escolhida == 5:
        deletar_tarefa()
    elif opcao_escolhida == 6:
        break