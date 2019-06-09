class Persona:
    def __init__(self, nombre, apellido, dni, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad

    def habla(self, string):
        print(string)
