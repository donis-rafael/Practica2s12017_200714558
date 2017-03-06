from flask import Flask, request, Response
import Practica2
from Practica2 import *

app = Flask("Web Service Flask")

cola = Practica2.Cola()
pila = Practica2.Pila()
lista = Practica2.Lista()
matrix = Practica2.Matriz()

################### COLA #########################
@app.route('/metodoWeb', methods=['POST'])
def hola():
    parametro = str(request.form['nombre'])
    return 'Hola '+str(parametro)+' Exitos'

@app.route('/ingresaCola', methods=['POST'])
def ingresa():
    valor = int(str(request.form['valor']))
    cola.ingresar(valor)
    cola.hacerGrafica()
    return 'ya'

@app.route('/eliminaCola', methods=['POST'])
def imprime():
    valor = request.form['valor']
    cola.eliminar()
    cola.hacerGrafica()
    return 'otroYa'

################### LISTA #########################
@app.route('/ingresaLista', methods=['POST'])
def list():
    valor = str(request.form['palabra'])
    lista.ingresar(valor)
    lista.hacerGrafica()
    return 'otroYa'

@app.route('/eliminaLista', methods=['POST'])
def elimLista():
    valor = int(str(request.form['valor']))
    lista.eliminar(valor)
    lista.hacerGrafica()
    return 'ya'

@app.route('/buscarLista', methods=['POST'])
def searchLista():
    valor = str(request.form['palabra'])
    dato = str(lista.buscar(valor))
    lista.hacerGrafica()
    return dato

################### PILA #########################
@app.route('/ingresaPila', methods=['POST'])
def ingresaPila():
    valor = int(str(request.form['valor']))
    pila.ingresar(valor)
    pila.hacerGrafica()
    return 'ya'

@app.route('/eliminaPila', methods=['POST'])
def eliminaPila():
    valor = request.form['valor']
    dato = str(pila.eliminar())
    pila.hacerGrafica()
    return dato

################### MATRIZ #########################
@app.route('/ingresaMatriz', methods=['POST'])
def matrixaa():
    nombre = str(request.form['nombre'])
    letra = str(request.form['letra'])
    dominio = str(request.form['dominio'])
    matrix.ingresar(nombre, letra, dominio)
    matrix.hacerGrafica()
    #matrix.hacerGrafica()
    return 'otroYa'

@app.route('/eliminaMatriz', methods=['POST'])
def deleteMatrix():
    nombre = str(request.form['nombre'])
    letra = str(request.form['letra'])
    dominio = str(request.form['dominio'])
    matrix.eliminar(nombre, letra, dominio)
    matrix.hacerGrafica()
    #matrix.hacerGrafica()
    return 'otroYa'

@app.route('/buscaLetra', methods=['POST'])
def buscaLetras():
    letra = str(request.form['letra'])
    correos = str(matrix.buscarPorLetra(letra))
    #matrix.hacerGrafica()
    return correos

@app.route('/buscaDominios', methods=['POST'])
def buscaDominio():
    dominio = str(request.form['dominio'])
    correos = str(matrix.buscarPorDominio(dominio))
    #matrix.hacerGrafica()
    return correos

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')