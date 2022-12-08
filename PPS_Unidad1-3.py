"""
Realiza, utilizando Python 3, el ejercicio 3 de la página 35 del libro “Introducción a
Python” de Jon Vadillo e inclúyelo en un fichero llamado lista.py. Las funciones que
debes usar en el ejercicio 3 deben utilizar OBLIGATORIAMENTE las siguientes
cabeceras:
def estaEnRango(valor, minimoimo, maximoimo)
Devuelve True o False determinimoando que valor se encuentra entre el mínimo y el
máximo.
def estaEnLista(valor, lista)
Devuelve True o False determinimoando si el valor está en la lista.
"""


lista = [5, 14, 11, 3, 2, 1, 15, 19]
valor = int(input("Introduzca un valor entre 1 y 20: "))
minimo = 1
maximo = 20

def estaEnRango(valor, minimo, maximo):
    if valor > maximo:
        print("El maximo es 20, tu numero supera este valor.")
        return False
    elif valor < minimo:
        print("El minimo es 1, tu numero no supera este valor.")
        return False
    else:
        estaEnLista(valor, lista)
        return True

def estaEnLista(valor, lista):

    recorreLista = 0

    for valores in lista:
        if valor == valores:
            recorreLista = 1
    if recorreLista == 1:
        print("El valor está en lista")
        return True
    else:
        print("El valor no esta en lista")
        return False
    

estaEnRango(valor, minimo, maximo)
