import os

#NODO DE LA COLA
class NodoCola:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

    def getNum(self):
        return self.numero

    def setNum(self, numero):
        self.numero = numero


#COLA
class Cola():

    def __init__(self):
        self.inicio = None
        self.fin = None

    def vacio(self):
        if self.inicio == None:
            return True
        else:
            return False

    def ingresar(self, numero):
        nuevoNodo = NodoCola(numero)

        if self.vacio() == True:
            self.inicio = nuevoNodo
        else:
            self.fin.siguiente = nuevoNodo

        self.fin = nuevoNodo

    def eliminar(self):
        if self.vacio() == False:
            temp = self.inicio

            if self.inicio.siguiente != None:
                self.inicio = self.inicio.siguiente
                temp = None
            else:
                self.inicio = self.fin = None

    def listar(self):
        print("----------------")
        temporal = self.inicio

        while temporal != None:
            print(temporal.getNum())
            temporal = temporal.siguiente

    def hacerGrafica(self):
        if self.vacio() == True:
            return
        else:
            file = open("cola.dot", "w")
            file.write("digraph G\n{\n")
            aux = self.inicio

            while aux != None:
                file.write("\"n"+str(aux.getNum())+"\"[label = \""+str(aux.getNum())+"\", style = filled]\n")
                if(aux.siguiente != None):
                    file.write("\"n"+str(aux.getNum())+"\" -> \"n"+str(aux.siguiente.getNum())+"\"\n")
                    file.write("{rank=same; \"n"+str(aux.getNum())+"\" \"n"+str(aux.siguiente.getNum())+"\"}\n");

                aux = aux.siguiente
            file.write("}")
            file.close()
            os.system("dot -Tjpg cola.dot > cola.jpg")


# ----------------------------------------------------------------------------------------------------------------------------
#NODO DE LA LISTA
class NodoLista:

    def __init__(self, cadena):
        self.cadena = cadena
        self.siguiente = None

    def getCadena(self):
        return self.cadena

    def setCadena(self, cadena):
        self.cadena = cadena


#LISTA
class Lista:

    def __init__(self):
        self.inicio = None
        self.fin = None


    def ingresar(self, cadena):
        nuevoNodo = NodoLista(cadena)

        if self.listaVacia() == True:
            self.inicio = nuevoNodo
        else:
            self.fin.siguiente = nuevoNodo

        self.fin = nuevoNodo


    def listaVacia(self):
        if(self.inicio == None):
            return True
        else:
            return False

    def listar(self):
        print("----------------")
        temporal = self.inicio

        while temporal != None:
            print(temporal.getCadena())
            temporal = temporal.siguiente

    def eliminar(self, indice):
        if self.listaVacia() == True:
            return
        else:
            aux = self.inicio
            aux2 = None
            i = 0
            while aux != None:
                i = i+1
                if(i == indice):
                    break
                aux2 = aux
                aux = aux.siguiente

            if i == indice and aux != None:
                if aux == self.inicio and self.inicio.siguiente != None:
                    self.inicio = self.inicio.siguiente

                elif aux == self.inicio and self.inicio.siguiente == None:
                    self.inicio = self.fin = None

                elif aux == self.fin:
                    self.fin = aux2
                    aux2.siguiente = None

                else:
                    aux2.siguiente = aux.siguiente
                    aux = None


    def buscar(self, cadena):
        if self.listaVacia() == True:
            return 0
        else:
            aux = self.inicio
            aux2 = None
            i = 0
            while aux != None:
                i = i + 1
                if (aux.getCadena() == cadena):
                    break
                aux2 = aux
                aux = aux.siguiente

            if aux != None and aux.getCadena() == cadena:
                return i

            else:
                return 0



    def hacerGrafica(self):
        if self.listaVacia() == True:
            return
        else:
            file = open("lista.dot", "w")
            file.write("digraph G\n{\n")
            aux = self.inicio

            while aux != None:
                file.write("\"n" + str(aux.getCadena()) + "\"[label = \"" + str(aux.getCadena()) + "\", style = filled]\n")
                if (aux.siguiente != None):
                    file.write("\"n" + str(aux.getCadena()) + "\" -> \"n" + str(aux.siguiente.getCadena()) + "\"\n")
                    file.write("{rank=same; \"n" + str(aux.getCadena()) + "\" \"n" + str(aux.siguiente.getCadena()) + "\"}\n");

                aux = aux.siguiente

            file.write("}")
            file.close()
            os.system("dot -Tjpg lista.dot > lista.jpg")


#----------------------------------------------------------------------------------------------------------------------------
# NODO DE LA PILA
class NodoPila:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

    def getNum(self):
        return self.numero

    def setNum(self, numero):
        self.numero = numero

# PILA
class Pila():

    def __init__(self):
        self.inicio = None
        self.fin = None

    def vacio(self):
        if self.inicio == None:
            return True
        else:
            return False

    def ingresar(self, numero):
        nuevoNodo = NodoPila(numero)

        if self.vacio() == True:
            self.inicio = nuevoNodo
        else:
            self.fin.siguiente = nuevoNodo

        self.fin = nuevoNodo

    def eliminar(self):
        if self.vacio() == False:
            temp = self.inicio
            while temp.siguiente != self.fin and temp.siguiente != None:
                temp = temp.siguiente

            if self.inicio == self.fin:
                val = self.inicio.getNum()
                self.inicio = self.fin = None
                return val
            else:
                val = temp.siguiente.getNum()
                temp.siguiente = None
                self.fin = temp
                return val

        return 0

    def listar(self):
        print("----------------")
        temporal = self.inicio

        while temporal != None:
            print(temporal.getNum())
            temporal = temporal.siguiente

    def hacerGrafica(self):
        if self.vacio() == True:
            return
        else:
            file = open("pila.dot", "w")
            file.write("digraph G\n{\n")
            aux = self.inicio

            while aux != None:
                file.write("\"n" + str(aux.getNum()) + "\"[label = \"" + str(aux.getNum()) + "\", style = filled]\n")
                if (aux.siguiente != None):
                    file.write("\"n" + str(aux.getNum()) + "\" -> \"n" + str(aux.siguiente.getNum()) + "\"\n")
                    file.write("{rank=same; \"n" + str(aux.getNum()) + "\" \"n" + str(aux.siguiente.getNum()) + "\"}\n");

                aux = aux.siguiente

            file.write("}")
            file.close()
            os.system("dot -Tjpg pila.dot > pila.jpg")


#--------------------------------------------------------------------------------------------------------------------
#NODO MATRIZ
class NodoMatriz:

    def __init__(self, nCorreo, letra, dominio):
        self.nombreCorreo = nCorreo
        self.letra = letra
        self.dominio = dominio
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.atras = None
        self.adelante = None

    def getNombre(self):
        return self.nombreCorreo

    def setNombre(self, nCorreo):
        self.nombreCorreo = nCorreo

    def getLetra(self):
        return self.letra

    def getDominio(self):
        return self.dominio


#MATRIZ
class Matriz:

    def __init__(self):
        self.inicio = NodoMatriz("", "", "")
        self.inicioHorizontal = None
        self.inicioVertical = None

    def ingresar(self, nombre, letra, dominio):
        nuevoNodoMatriz = NodoMatriz(nombre, letra, dominio)

        if self.vacioHorizont() == True:
            nuevoNodoHorizontal = NodoMatriz("","",dominio)
            self.inicioHorizontal = nuevoNodoHorizontal

        if self.vacioVerti() == True:
            nuevoNodoVertical = NodoMatriz("",letra,"")
            self.inicioVertical = nuevoNodoVertical

        ################# CREACION CABECERA HORIZONTAL #################

        tempHorizont = self.inicioHorizontal

        if self.existeHorizont(dominio) == True:
            while tempHorizont.getDominio() != dominio:
                tempHorizont = tempHorizont.derecha

        else:
            nuevoNodoHorizontal = NodoMatriz("","",dominio)
            temp2 = None
            while tempHorizont != None and tempHorizont.getDominio() < dominio:
                temp2 = tempHorizont
                tempHorizont = tempHorizont.derecha

            if tempHorizont != None and tempHorizont.getDominio() > dominio:

                if tempHorizont == self.inicioHorizontal:
                    temp4 = self.inicioHorizontal
                    tempHorizont = nuevoNodoHorizontal
                    tempHorizont.izquierda = None
                    tempHorizont.derecha = temp4
                    temp4.izquierda = tempHorizont
                    self.inicioHorizontal = tempHorizont

                else:
                    temp4 = tempHorizont
                    tempHorizont = nuevoNodoHorizontal
                    temp2.derecha = tempHorizont
                    tempHorizont.derecha = temp4
                    temp4.izquierda = tempHorizont
                    tempHorizont.izquierda = temp2

            else:
                tempHorizont = nuevoNodoHorizontal
                temp2.derecha = tempHorizont
                tempHorizont.izquierda = temp2

        ################# APUNTADORES CON CABECERA HORIZONTAL #################

        if tempHorizont.abajo != None:
            temp5 = None
            while tempHorizont.abajo != None:
                temp5 = tempHorizont
                tempHorizont = tempHorizont.abajo
                if  tempHorizont.getLetra() == letra or tempHorizont.getLetra() > letra:
                    break

        if tempHorizont.getLetra() == letra:
            if tempHorizont.atras != None:
                while tempHorizont.atras != None:
                    tempHorizont = tempHorizont.atras
            tempHorizont.atras = nuevoNodoMatriz
            nuevoNodoMatriz.adelante = tempHorizont

        elif tempHorizont.abajo != None and tempHorizont.getLetra() == "" and tempHorizont.abajo.getLetra() > letra:
            temp5 = tempHorizont
            temp6 = tempHorizont.abajo
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        elif tempHorizont != None and tempHorizont.getLetra() > letra:
            temp6 = tempHorizont
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        else:
            tempHorizont.abajo = nuevoNodoMatriz
            nuevoNodoMatriz.arriba = tempHorizont

        ################# CREACION DE CABECERA VERTICAL #################

        tempVerti = self.inicioVertical

        if self.existeVerti(letra) == True:
            while tempVerti.getLetra() != letra:
                tempVerti = tempVerti.abajo

        else:
            nuevoNodoVertical = NodoMatriz("", letra, "")
            temp3 = None
            while tempVerti != None and tempVerti.getLetra() < letra:
                temp3 = tempVerti
                tempVerti = tempVerti.abajo

            if tempVerti != None and tempVerti.getLetra() > letra:
                if tempVerti == self.inicioVertical:
                    temp4 = self.inicioVertical
                    tempVerti = nuevoNodoVertical
                    tempVerti.arriba = None
                    tempVerti.abajo = temp4
                    temp4.arriba = tempVerti
                    self.inicioVertical = tempVerti

                else:
                    temp4 = tempVerti
                    tempVerti = nuevoNodoVertical
                    temp3.abajo = tempVerti
                    tempVerti.abajo = temp4
                    temp4.arriba = tempVerti
                    tempVerti.arriba = temp3

            else:
                tempVerti = nuevoNodoVertical
                temp3.abajo = tempVerti
                tempVerti.arriba = temp3

        ################# INICIA APUNTADORES CON CABECERA VERTICAL #################

        if tempVerti.derecha != None:
            temp5 = None
            while tempVerti.derecha != None:
                temp5 = tempVerti
                tempVerti = tempVerti.derecha
                if  tempVerti.getDominio() == dominio or tempVerti.getDominio() > dominio:
                    break

        if tempVerti.derecha != None and tempVerti.derecha.getDominio() > dominio:
            temp5 = tempVerti
            temp6 = tempVerti.derecha
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        elif tempVerti != None and  tempVerti.getDominio() != "" and tempVerti.getDominio() > dominio:
            temp6 = tempVerti
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        else:
            tempVerti.derecha = nuevoNodoMatriz
            nuevoNodoMatriz.izquierda = tempVerti

    def vacioHorizont(self):
        if self.inicioHorizontal == None:
            return True
        else:
            return False

    def vacioVerti(self):
        if self.inicioVertical == None:
            return True
        else:
            return False

    def existeVerti(self, letra):
        temporal = self.inicioVertical
        while temporal != None:
            if temporal.getLetra() == letra:
                return True
            else:
                temporal = temporal.abajo

        return False

    def existeHorizont(self, dominio):
        temp = self.inicioHorizontal

        while temp != None:
            if temp.getDominio() == dominio:
                return True
            else:
                temp = temp.derecha

        return False

    def listarHorizont(self, letra):
        if self.vacioVerti() == False:
            aux = self.inicioVertical
            while aux != None and aux.getLetra() != letra:
                aux = aux.abajo

            if aux.getLetra() == letra:
                print("** " + aux.getLetra() + " **")
                if aux.derecha != None:
                    aux = aux.derecha
                    while aux != None:
                        print(aux.getNombre() + " " + aux.getDominio())
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                print(aux2.getNombre() + " " + aux2.getDominio())
                                aux2 = aux2.atras
                        aux = aux.derecha


    def listarVerti(self, dominio):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux != None and aux.getDominio() != dominio:
                aux = aux.derecha

            if aux.getDominio() == dominio:
                print("** " + aux.getDominio() + " **")
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux != None:
                        print(aux.getNombre() + " " + aux.getLetra())
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                print(aux2.getNombre() + " " + aux2.getLetra())
                                aux2 = aux2.atras
                        aux = aux.abajo


#--------------------------------------------------------------------------------------------------------------------
#-------------------------------------------- PRUEBAS ---------------------------------------------------------------
# colita = Cola()
# colita.ingresar(3)
# colita.ingresar(5)
# colita.ingresar(7)
# colita.ingresar(9)
# colita.listar()
# colita.hacerGrafica()
# colita.eliminar()
# colita.listar()
# colita.eliminar()
# colita.listar()
# colita.eliminar()
# colita.listar()
# colita.eliminar()
# colita.listar()
# colita.eliminar()

# caden = Lista()
# caden.ingresar(2)
# caden.ingresar(4)
# caden.ingresar(6)
# caden.ingresar(8)
# caden.listar()
# caden.eliminar(4)
# caden.listar()
# caden.eliminar(2)
# caden.listar()
# caden.eliminar(8)
# caden.listar()
# caden.eliminar(6)
# caden.listar()

#pilin = Pila()
#pilin.ingresar(20)
#pilin.ingresar(40)
#pilin.ingresar(60)
#pilin.ingresar(80)
#pilin.listar()
#pilin.eliminar()
#pilin.listar()
#pilin.eliminar()
#pilin.listar()
#pilin.eliminar()
#pilin.listar()
#pilin.eliminar()
#pilin.listar()
#pilin.eliminar()

matrix = Matriz()
matrix.ingresar("rafa", "r", "yahoo")
matrix.ingresar("jorge", "j", "gmail")
matrix.ingresar("ramon", "r", "hotmail")
matrix.ingresar("Pantera", "p", "yahoo")
matrix.ingresar("parto", "p", "hotmail")
matrix.ingresar("popo", "p", "yahoo")
matrix.ingresar("paolita", "p", "outlock")
matrix.ingresar("pedrito", "p", "yahoo")
matrix.ingresar("paco", "p", "gmail")
matrix.ingresar("taty", "t", "yahoo")
matrix.listarHorizont("r")
matrix.listarVerti("gmail")
matrix.listarVerti("yahoo")
matrix.listarHorizont("p")