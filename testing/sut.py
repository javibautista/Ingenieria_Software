import math
from collections import defaultdict

def prod(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] * prod(listaNumeros[1:])

def productoria(lista, hasta):
    return prod(lista[:hasta])

def sumatoria(lista, hasta):
    return sum(lista[:hasta])

def area(ancho, alto):
    return ancho * alto

def saludar(nombre):
    return "Hola " + nombre

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def valorabsoluto(n):
    n = -n
    return n



def comparar(a, b):
    if a < b:
        return "A menor que B"
    if a > b:
        return "A mayor que B"
    if a == b:
        return "A y B son iguales"

def costototal(producto1, producto2):
    total = sumar(producto1, producto2)
    return "El costo total es $" + str(total)


def supercalc(num):
    exp = math.exp(num)
    sum = exp + 2
    sqrt = math.sqrt(sum)
    return sqrt


class CalcuClass:

    def _registrar_operacion(func):
        def operacion_decorada(self, **kwargs):
            try:
                getattr(self.historico, func.__name__)
            except AttributeError:
                self.historico[func.__name__] = []

            self.historico[func.__name__].append(tuple(kwargs.values()))
            return func(self, **kwargs)

        return operacion_decorada

    def __init__(self):
        self.historico = defaultdict(list)
        #print(self.historico)

    @_registrar_operacion
    def suma(self, a, b):
        return sumar(a, b)

    @_registrar_operacion
    def producto(self, a, b):
        return multiplicar(a, b)

    @_registrar_operacion
    def sumar_varios(self, lista):
        return sumatoria(lista, len(lista))
        
if __name__ == '__main__':
    print('\n_____ CalcuClass _____\n')
    calc = CalcuClass()
    print(calc.suma(a=5, b=4))
    print(calc.historico)
    print(calc.suma(a=4, b=2))
    print(calc.historico)
    print(sumar(4,1))
