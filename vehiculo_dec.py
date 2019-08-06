def manejar_vehiculo(self):
    for _ in range(3):
        self.andar()
    print("El {} quedó en posicion {}".format(type(self).__name__, self.posicion))


class Vehiculo:
    def __init__(self, posicion = 0):
        self.posicion = posicion

def verificar_ruedas(f):
    def nuevafuncion(self, *args, **kwargs):
        f(self, *args, **kwargs)
        if self.posicion%100 == 0:
            print('Verificar ruedas, el {} tiene 100km recorridos'.format(type(self).__name__))
    return nuevafuncion

def verificar_ruedas_camion(f):
    def nuevafuncion(self, *args, **kwargs):
        f(self, *args, **kwargs)
        if self.posicion%20 == 0:
            print('Verificar ruedas, el {} tiene 20km recorridos'.format(type(self).__name__))
    return nuevafuncion

class Auto(Vehiculo):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    @verificar_ruedas
    def andar(self):
        self.posicion += 20
        return self.posicion

class Camion(Vehiculo):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    @verificar_ruedas_camion
    def andar(self):
        self.posicion += 5
        return self.posicion

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
