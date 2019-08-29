import math

def area(ancho, alto):
    return ancho * alto

def saludar(nombre):
    return "Hola " + nombre
    
def sumar(a, b):
    return a + b
    
def comparar(a, b):
    if a < b:
        return "A menor que B"
    if a > b:
        return "A mayor que B"
    if a == b:
        return "A y B son iguales"
   
def valorabsoluto(n):
    if n < 0:
        n = -n
    return n
    
def costototal(producto1, producto2):
    total = sumar(producto1, producto2)
    return "El costo total es $" + str(total)


def supercalc(num):
    exp = math.exp(num)
    sum = exp + 2
    sqrt = math.sqrt(sum)
    return sqrt

