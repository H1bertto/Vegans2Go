from flask import Flask, render_template_string, render_template, redirect, url_for

app = Flask(__name__)

AUTHORS_INFO = {
    'souza': {
        'full_name': 'Humberto V S',
        'natio': 'BR',
        'work': 'Accenture',
        'born': '26/07',
        'img': 'link'
    },
    'borges': {
        'full_name': 'Hugo V S',
        'natio': 'BR',
        'work': 'Accenture',
        'born': '10/10',
        'img': 'link2'
    }
}


@app.route('/')
def page():
    return redirect(url_for('index'))


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/omg')
def omg():
    testando = open("teste.html", "r", encoding="utf-8")
    return testando.read()


@app.route('/issae')
def taligado():
    html = """
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>É NOZES</title>
        </head>
        <body>
            <h1>MANU DU CEU</h1>
            {0}
        </body>
        </html>
    """
    authors = ["<h1>Humberto</h1>", "É", "O", "CARAAAAA", "PUTA QUE CARAIOOOOOOOOOOOOOO"]
    authlist = "<ul>"
    authlist += "\n".join(["<li>{0}</li>".format(auth) for auth in authors])
    authlist += "</ul>"
    print(authlist)
    return html.format(authlist)


@app.route('/jinja')
def jinjacarai():
    libname = "Poe"
    html = """
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>mlk sinistro</title>
    </head>
    <body>
        <h1>Wheels come tbm {{libs}} lib name</h1>
        <ul>
            {% for auth in authors %}
                <li>{{ auth }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    authors = ["1", "Ber", "To", "Hugo", "Vai", "Pirar"]
    render_html = render_template_string(html, libs=libname, authors=authors)
    return render_html


@app.route('/putz')
def omgaoquadrado():
    testando = open("teste2.html", "r", encoding="utf-8")
    authors = ["1", "Ber", "To", "Hugo", "Vai", "Pirar"]
    html = render_template_string(testando.read(), authors=authors)
    return html


@app.route('/rendido')
def opsfizca():
    authors = ["1", "Ber", "To", "Hugo", "Vai", "Pirar"]
    return render_template("teste2.html", authors=authors)


@app.route('/fi')
def diniamo1():
    return render_template("teste.html")


@app.route('/fi/<bago>')
def diniamo(bago):
    return render_template("teste1.html", fi=AUTHORS_INFO[bago])
