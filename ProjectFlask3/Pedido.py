from Project.Produto import Produto
from Project.Imprimir import print_pedido
from firebase.firebase import FirebaseAuthentication
from firebase.firebase import FirebaseApplication


class Pedido:
    def __init__(self):
        self.app = FirebaseApplication('https://vegans2godatabase.firebaseio.com', authentication=None)
        self.authentication = FirebaseAuthentication('Wg6XvS7W0UftiQlBnCM1tt8gVSIE7exereBXcYx0', 'thegambiarra2@gmail.com', extra={'id': 123})
        self.app.authentication = self.authentication
        self.cod_pedido = 0
        self.dic_bebida = {}
        self.dic_comida = {}
        self.produto = Produto()
        self.pedido = []

    def criar_pedido(self, user):
        self.produto.listar_produtos_disponiveis()

        p = str(input("\n •Digite o codigo dos produtos desejados separando por espaços: "))
        plis = p.split()
        # print(plis)
        for x in plis:
            self.pedido.append('00' + x)
        user = user.replace(" ", "")
        for x in self.pedido:
            qt = self.app.get("/Pedidos/" + user, x)
            if qt is None:
                qt = 1
            elif qt >= 1:
                qt += 1
            self.app.put("/Pedidos/" + user, x, qt)
        print("Pedido Realizado Com sucesso")
        self.imprimir_pedido(user)



    def buscar_pedido(self):
        pass

    def editar_pedido(self):
        pass

    def imprimir_pedido(self, user):
        litas = []
        p = """
    Pedido de {0}
=======================
        """
        for ftstr in self.pedido:
            qt = str(self.app.get("/Pedidos/" + user, ftstr))
            nome = str(self.app.get('/Produtos/' + ftstr, 'Nome'))
            if ftstr in litas:
                continue
            else:
                p += '\n' + nome + ' ------ ' + qt + 'x'
            litas.append(ftstr)
        p += '\n' + "======================="
        print_pedido(p.format(user), user)
