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

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username']) 
        # print(request.form['password'])
        # user = request.form['username']
        # password = request.form['password']
        # datos.append({"email":user, "contraseña": password})
        return render_template ('index_usuario.html')
    else:
        return "<p>Bye, World!</p>"

@app.route('/home', methods=['GET', 'POST']) #URL raíz usuario-credito
def home():
    if request.method == 'POST':
        # data= {
        # 'titulo':'Gestor Cobranza - creze',
        # 'bienvenido':'Cobranza'
        # } 
        return render_template ('home.html') ##Regreso nuevo y diccionario data
    else:
        return "<p>Bye, World!</p>"

# @app.route('/<username>') #URL tabla trabajo
# def params (username):
#     data= {
#         'titulo':'Gestor Cobranza - creze',
#         'bienvenido':'Cobranza'
#      }   
#     return render_template ('index_usuario.html',data=data) ##Regreso nuevo y diccionario data    

@app.route('/list' , methods=['GET', 'POST'])
def params ():
    if request.method == 'POST':
        return render_template ('index_usuario.html') 
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