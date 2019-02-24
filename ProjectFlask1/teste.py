itens = {
        "000": {
            "name": "Picadinho de Legumes",
            "img": "../static/imagens/hamburguer_graodebico.jpg",
            "desc": "Descrição",
            "price": "R$25,00",
        },
        "001": {
            "name": "Picadinho de Jaca",
            "img": "../static/imagens/hamburguer_graodebico.jpg",
            "desc": "Descrição",
            "price": "R$25,00",
        },
    }

for item in itens.keys():
    print(item)
    print(itens[item]['name'])
    for vaal in itens:
        print(vaal)