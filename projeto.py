import uuid
class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = uuid.uuid4()

class Quarto:
    def __init__(self, num, tp_quarto, preco_diaria):
        self.num = num
        self.tp_quarto = tp_quarto
        self.preco_diario = preco_diaria
        self.disponivel = True

class Reserva:
    def __init__(self, dono_reserva, quarto_reservado, ckeck_in_or_out, status):
        self.dono_reserva = dono_reserva
        self.quarto_reservado = quarto_reservado
        self.ckeck_in_or_out = ckeck_in_or_out
        self.status = status
        self.lista_quartos = []

class GerenciadorDeReservas:
    def __init__(self):
        self.quartos = []
        self.reservas = []
        self.clientes = []
        
    def verificar_disponibilidade(self, num_quarto):
        for quarto in self.quartos:
            if quarto.num == num_quarto:
                if not quarto.disponivel:
                    return False        
                else:
                    return True
        else:
            print('Quarto não encontrado!')