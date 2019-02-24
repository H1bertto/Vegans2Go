from Project.Cardapio import Cardapio
from Project.Produto import Produto
from Project.Pedido import Pedido
from Project.Mesa import Mesa

prod = Produto()
cad = 0

while cad < 0:
    nome = str(input("Nome: "))
    nome = nome.upper()
    descricao = str(input("Descrição: "))
    descricao = descricao[0:1].upper() + descricao[1:].lower()
    foto = str(input("Link da Foto: "))
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
prod.ativar_produto('002')
prod.ativar_produto('003')
# prod.editar_produto("006")
# print("--------------------------------")
# prod.ativar_produto("001")
# print(prod.buscar_produto("001"))


