"""
Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
introduzca un número binario e imprima por pantalla el número en formato decimal.
Para desarrollar el programa, es necesario que desarrolles una función con la
siguiente cabecera:

def esBinario(strbinario)
Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
como parámetro contiene una cadena binaria.
Ejemplo de esBinario:
print(esBinario(“1001”))
True
print(esBinario(“Hola”))
False
"""

def esBinario(strbinario):
    for numeros in strbinario:
        if((numeros != "0") and (numeros != "1")):
            print("Error. Escriba un valor binario")
            return False
    print ("Valor correcto.")
    binarioDecimal(strbinario)
    return True

def binarioDecimal(strbinario):
    decimal = 0

    for posicion, digito in enumerate(strbinario[::-1]):
        decimal += int(digito) * 2 ** posicion
    print(f"El número {strbinario} corresponde es el {decimal} en decimal.")
    return decimal

binario = input("Introduce un numero binario: ")
esBinario(binario)