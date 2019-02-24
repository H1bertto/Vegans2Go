from Project.Produto import Produto
import tkinter

prod = Produto()
cad = int(input("Quantos produtos irá cadastrar: "))
i = 0
while i < cad:
    nome = str(input("Nome: "))
    nome = nome.upper()
    descricao = str(input("Descrição: "))
    descricao = descricao[0:1].upper() + descricao[1:].lower()
    foto = str(input("Link da Foto: "))
    ft = "../static/imagens/imagenscardapio/" + foto + ".jpg"
    valor = ""
    while isinstance(valor, str):
        try:
            valor = input("Valor: ")
            valor = float(valor.replace(",", "."))
        except ValueError:
            print("Formato de Valor Incorreto!")
            valor = ""
    prod.add_produto(nome, descricao, valor, ft)
    i += 1
prod.listar_produtos_disponiveis()
print("\n")
# cod = str(input("Digite o codigo do produto para editar"))
# prod.remover_produto(cod)
# print("--------------------------------")
# prod.ativar_produto("001")
# print(prod.buscar_produto("001"))


