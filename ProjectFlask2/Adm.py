from Cardapio import Cardapio
from Produto import Produto
from Pedido import Pedido
from Mesa import Mesa

prod = Produto()
cad = 0

while cad < 0:
    nome = str(input("Nome: "))
    nome = nome.upper()
    descricao = str(input("Descrição: "))
    descricao = descricao[0:1].upper() + descricao[1:].lower()
    foto = str(input("Link da Foto:"))
    valor = ""
    while isinstance(valor, str):
        try:
            valor = input("Valor: ")
            valor = float(valor.replace(",", "."))
        except ValueError:
            print("Formato de Valor Incorreto!")
            valor = ""
    prod.add_produto(nome, descricao, valor, foto)
    cad += 1
prod.listar_produtos_disponiveis()
prod.editar_produto("006")
# print("--------------------------------")
# prod.ativar_produto("001")
# print(prod.buscar_produto("001"))


