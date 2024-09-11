from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sitios')
def sitios():
    return render_template('sitios.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/testimonios')
def testimonios():
    return render_template('testimonios.html')

if __name__ == '__main__':

    app.run(host='192.168.2.78', port=5000, debug=True)

 


