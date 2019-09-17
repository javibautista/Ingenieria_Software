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

    @_registrar_operacion
    def suma(self, a, b):
        return sumar(a, b)

    @_registrar_operacion
    def producto(self, a, b):
        return multiplicar(a, b)

    @_registrar_operacion
    def sumar_varios(self, lista):
        return sumatoria(lista, len(lista))
