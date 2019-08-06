def avisar(f):
    def inner(*args, **kwargs):
        f(*args, **kwargs)
        print ("Se ha ejecutado %s" % f.__name__)
    return inner

def autenticado(f):
    def nuevafuncion(*args, **kwargs):
        if AUTHENTICATED:
            f(*args, **kwargs)
            print('autenticado')
        else:
            raise Exception
    return nuevafuncion

@autenticado
@avisar
def abrir_puerta():
    print ("Abrir puerta")

@autenticado
@avisar 
def cerrar_puerta():
    print ("Cerrar puerta")


AUTHENTICATED = True

abrir_puerta()
cerrar_puerta()
