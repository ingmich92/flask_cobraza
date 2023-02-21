import os
import time
from flask import Flask,render_template, url_for, redirect, request,g
# import psycopg2
from flask_wtf import CSRFProtect
# import pandas as pd
# from flask_bootstrap import Bootstrap

app=Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
csrf = CSRFProtect(app)

#Ejemplo de un metodo sencillo:
# @app.route('/') #URL raíz usuario-credito
# def hello():
#     return "<p>Hello, World!</p>"

@app.route('/') #Ruta home que muestra el login
def index():
    return render_template('login.html')

@app.route('/list', methods=['GET', 'POST']) #Ruta que nos muestra la lista del trabajo
def login():
    if request.method == 'POST':
        return render_template ('index_usuario.html')
    else:
        return "<p>Bye, World!</p>"

@app.route('/home', methods=['GET', 'POST']) #Ruta que nos envie al home del usuario
def home():
    if request.method == 'POST':
        return render_template ('home.html') 
    else:
        return "<p>Bye, World!</p>"

@app.before_request
def before_request():
   g.request_start_time = time.time()
   g.request_time = lambda: "%.5fs" % (time.time() - g.request_start_time)    


def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect (url_for('index'))


if __name__=='__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True,port=5000) ##Ver las modificaciones en TR y puerto 5000