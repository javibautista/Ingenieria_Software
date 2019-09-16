def manejar_vehiculo(self):
    for _ in range(3):
        self.andar()
    print("El {} quedó en posicion {}".format(type(self).__name__, self.posicion))
    
def carga_limite(linite):
    def nuevo_limite(self):
        if self.kilos > 300:
            print('Camión sobrecargado no arrancar')
        limite(self)
    return nuevo_limite
    
"""
def verificar_rueda(func):
    def nueva_funcion(self):
        print('revisar rueda antes')
        func(self)
"""

class Vehiculo:
    def __init__(self, posicion = 0):
        self.posicion = posicion

def verificar_ruedas(f):
    def nuevafuncion(self, *args, **kwargs):
        f(self, *args, **kwargs)
        if type(self).__name__ == 'Auto' and self.posicion%100 == 0:
            print('Verificar ruedas, el {} superó los 100km recorridos'.format(type(self).__name__))
        elif type(self).__name__ == 'Camion' and self.posicion%20 == 0:
            print('Verificar ruedas, el {} superó los 20km recorridos'.format(type(self).__name__))
        else:
            pass
    return nuevafuncion
'''
def verificar_ruedas_camion(f):
    def nuevafuncion(self, *args, **kwargs):
        f(self, *args, **kwargs)
        if self.posicion%20 == 0:
            print('Verificar ruedas, el {} superó los 20km recorridos'.format(type(self).__name__))
    return nuevafuncion'''

def carga_limite(f):
    def nueva

class Auto(Vehiculo):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    @verificar_ruedas
    def andar(self):
        self.posicion += 20
        #print(self.posicion)
        return self.posicion

class Camion(Vehiculo):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.carga_actual = 0
    
    @verificar_ruedas
    def andar(self):
        self.posicion += 5
        #print(self.posicion)
        return self.posicion
    
        
    def cargar(self, numero=0):
        self.carga_actual += numero
        print('{} kgs'.format(self.carga_actual))
        return self.carga_actual

if __name__ == '__main__':
    print('\n_____ AUTO _____\n')
    a = Auto()
    a.andar()
    a.andar()
    a.andar()
    a.andar()
    a.andar()
    print('\n_____ CAMION _____\n')
    c = Camion()
    c.andar()
    c.andar()
    c.andar()
    c.andar()
    manejar_vehiculo(c)
    c.cargar(30)
    c.cargar(40)
