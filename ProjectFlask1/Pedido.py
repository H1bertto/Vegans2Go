from Project.Produto import Produto
from Project.Imprimir import print_pedido


class Pedido:
    def __init__(self):
        self.cod_pedido = 0
        self.dic_bebida = {}
        self.dic_comida = {}
        self.produto = Produto()

    def criar_pedido(self):
        self.produto.listar_produtos_disponiveis()

    def buscar_pedido(self):
        pass

    def editar_pedido(self):
        pass

    def imprimir_pedido(self):
        print_pedido("")
