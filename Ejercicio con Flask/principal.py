from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Inicio.html')

@app.route('/luisa')
def luisa():
    return render_template('Luisa/inicio.html')

@app.route('/luisa/Datos básicos')
def luisas():
    return render_template('Luisa/datosbásicos.html')

@app.route('/luisa/Formación')
def luisat():
    return render_template('Luisa/formación.html')

@app.route('/luisa/Intereses')
def luisac():
    return render_template('Luisa/intereses.html')

@app.route('/william')
def william():
    return render_template('William/segunda.html')

@app.route('/william/Datos básicos')
def williams():
    return render_template('William/Primera.html')

@app.route('/william/Formación')
def williamt():
    return render_template('William/tercera.html')

@app.route('/william/Intereses')
def williamc():
    return render_template('William/cuarta.html')

@app.route('/sergio')
def sergio():
    return render_template('Sergio/Primera.html')

@app.route('/sergio/Datos básicos')
def sergios():
    return render_template('Sergio/Segunda.html')

@app.route('/sergio/Formación')
def sergiot():
    return render_template('Sergio/Tercera.html')

@app.route('/sergio/Intereses')
def sergioc():
    return render_template('Sergio/Cuarta.html')

if __name__ == '__main__':
    app.run(debug=True)