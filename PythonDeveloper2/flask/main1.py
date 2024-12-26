from flask import Flask, request, before_render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return"<h1>Home</h1>"

@app.route('/')
def pocetna_strana():
    return "<h1>Pocetna strana</h1>"

@app.route("/pozdrav",  defaults = {"name": "Dimitar"})

@app.route("/pozdrav/<name>")
def pozdrav(name, prezime):
    return f"<h1>Pozdrav do {name}{prezime}</h1>"


@app.route("/kvadrat",defaults = {"value": "result"})
@app.route("/kvadrat")
def calculate():
    value = request.args.get('value')
    try:
        if value is None or value == "":
            return "<h1>Ve molam vnesete broj za presmetka na kvadrat</h1>"
        number = float(value)
        result = number ** 2
        return f"<h1>Rezultat: {result}</h1>"
    except ValueError:
        return "<h1>Ve molam vnesete validen broj za presmetka na kvadrat</h1>"

@app.route("/sobiranje")
def sobiranje():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        if a is None or a == "" or b is None or b == "":
            return "<h1>Ve molam vnesete dva broja za sobiranje</h1>"
        broj_a = float(a)
        broj_b = float(b)
        rezultat = broj_a + broj_b
        return f"<h1>Zbirot na {broj_a} i {broj_b} e: {rezultat}</h1>"
    except ValueError:
        return "<h1>Ve molam vnesete validni broevi za sobiranje</h1>"


@app.route("/name")

def name():
    ime = request.args.get("ime")
    prezime = request.args.get("prezime")
    return f"<h1>Moeto ime e {ime} {prezime}</h1>"


if __name__ == '__main__':
    app.run(debug=True)