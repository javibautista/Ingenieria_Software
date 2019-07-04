class Persona:
	def __init__(self, nombre, apellido, dni, edad,**kw):
		self.nombre=nombre
		self.apellido=apellido
		self.dni=dni
		self.edad=edad
		print(nombre,apellido,dni,edad)
		
	def habla(self, string):
		print(string)

	def __cmp__(self, otro):
			diferencia = (self.edad) - (otro.edad)
			if diferencia < 0:
					return -1
			elif diferencia > 0:
					return 1
			else:
					return 0

en la terminal:

per=Persona(nombre='jonatan',apellido='avila',dni=33132131,edad=34)     
jonatan avila 33132131 34

par=Persona(nombre='jonatan',apellido='avila',dni=32423545,edad=32)     
jonatan avila 32423545 32

print(per.__cmp__(par))

devuelve 
1

