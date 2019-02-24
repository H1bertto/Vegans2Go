from firebase.firebase import FirebaseAuthentication
from firebase.firebase import FirebaseApplication


class Produto:
    def __init__(self):
        self.app = FirebaseApplication('https://vegans2godatabase.firebaseio.com', authentication=None)
        self.authentication = FirebaseAuthentication('Wg6XvS7W0UftiQlBnCM1tt8gVSIE7exereBXcYx0', 'thegambiarra2@gmail.com', extra={'id': 123})
        self.app.authentication = self.authentication
        self.cod_produto = 0
        self.nome = ""
        self.status = ""
        self.descricao = ""
        self.valor = .0
        self.dic_prod = {}

    def add_produto(self, nome, desc, vlr, ft):
        tam = self.app.get("/", "Produtos")
        if tam is None:
            cod = "000"
        elif len(tam) < 9:
            cod = "00" + str(len(tam))
        elif len(tam) < 99:
            cod = "0" + str(len(tam))
        else:
            cod = str(tam)
        self.app.put("/Produtos", cod, {"Nome": nome, "Descricao": desc, "Valor": vlr, "Foto": ft, "Status": "Ativo"})

    def remover_produto(self, cod):
        self.app.put("/Produtos/" + cod, "Status", "Esgotado")

    def ativar_produto(self, cod):
        self.app.put("/Produtos/" + cod, "Status", "Ativo")

    def editar_produto(self, cod):
        produto = self.buscar_produto(cod)
        if produto is not None:
            print("-----\nAtualize as informações do Produto (Digite: 0 se quiser manter a informação)")
            nome = str(input("Novo Nome: "))
            nome = nome.upper()
            if nome == "0":
                nome = produto["Nome"]
            desc = input("Nova Descrição: ")
            desc = desc[0:1].upper() + desc[1:].lower()
            if desc == "0":
                desc = produto["Descricao"]
            vlr = input("Novo Valor:")
            if vlr == "0":
                vlr = produto["Valor"]
            status = produto["Status"]
            self.app.put("/Produtos", cod, {"Nome": nome, "Descricao": desc, "Valor": vlr, "Status": status})

    def buscar_produto(self, cod):
        produto = self.app.get("/Produtos", cod)
        if produto is None:
            print("\n• Não há esse produto ainda")
            return None
        else:
            print("\n• Produto Encontrado:")
            self.listar_produtos(cod)
            return produto

    def listar_produtos(self, cod=None):
        prod = "-----\n{0} - {1}\n{2}\nPreço: R${3}\nStatus: {4}"
        if cod is not None:
            produto = self.app.get("/Produtos", cod)
            produto["Valor"] = str(produto["Valor"]).replace(".", ",")
            if len(produto["Valor"][produto["Valor"].find(","):]) < 3:
                produto["Valor"] += "0"
            print(prod.format(cod, produto["Nome"], produto["Descricao"], produto["Valor"], produto["Status"]))
        else:
            produtos = self.app.get("/", "Produtos")
            for cod in produtos.keys():
                produtos[cod]["Valor"] = str(produtos[cod]["Valor"]).replace(".", ",")
                if len(produtos[cod]["Valor"][produtos[cod]["Valor"].find(","):]) < 3:
                    produtos[cod]["Valor"] += "0"
                print(prod.format(cod, produtos[cod]["Nome"], produtos[cod]["Descricao"], produtos[cod]["Valor"], produtos[cod]["Status"]))

    def listar_produtos_disponiveis(self):
        prod = "-----\n{0} - {1}\n{2}\nPreço: R${3}"
        produtos = self.app.get("/", "Produtos")
        for cod in produtos.keys():
            if produtos[cod]["Status"] == "Esgotado":
                continue
            else:
                produtos[cod]["Valor"] = str(produtos[cod]["Valor"]).replace(".", ",")
                if len(produtos[cod]["Valor"][produtos[cod]["Valor"].find(","):]) < 3:
                    produtos[cod]["Valor"] += "0"
                print(prod.format(cod, produtos[cod]["Nome"], produtos[cod]["Descricao"], produtos[cod]["Valor"]))
