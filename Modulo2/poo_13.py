class Cliente:
    def __init__(self, nome, cpf, cep):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.pedido = []

    def listar_pedidos(self):
        for p in self.pedido:
            return f'Cliente: {self.nome}\n Pedido: {self.pedido}'
        
class Pedido:
    def __init__(self, data, produto, qtde, cliente):
        self.data = data
        self.produto = produto
        self.qtde = qtde
        self.cliente = cliente