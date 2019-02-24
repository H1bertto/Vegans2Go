from Project.Cardapio import Cardapio
from Project.Produto import Produto
from Project.Pedido import Pedido
from Project.Mesa import Mesa


def pedir():
    p = Pedido()
    print("Bem vindo ao Vegans 2 Go")
    print("Faça seu pedido")
    user = str(input("Digite seu nome: "))
    p.criar_pedido(user)


if __name__ == '__main__':
    pedir()
