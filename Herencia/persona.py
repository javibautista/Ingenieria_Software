class Persona: # Creamos la clase padre
	def __init__(self, nombre, apellido, dni, edad): # definimos sus atributos 
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.edad = edad
	
	def __str__(self):
		""" Devuelve una cadena representativa de persona """
		cadena = self.nombre +","+ self.apellido +","+ str(self.dni) +","+ str(self.edad)
		return cadena
	
	def habla(self, string): # Metodo de instancia
		print (string)

	def __cmp__(self, otro):
		diferencia = (self.edad) - (otro.edad)
		if diferencia < 0:
			return -1
		elif diferencia > 0:
			return 1
		else: 
			return 0
		
class Docente(Persona): # Creamos la clase hija que hereda de padre
	def __init__(self, materia, numero_de_legajo,
		cantidad_de_alumnos_a_cargo, anios_de_antiguedad, **kw):
		self.materia = materia  # Especificamos el nuevo atribuo de la clase hija
		self.numero_de_legajo = numero_de_legajo
		self.cantidad_de_alumnos_a_cargo = cantidad_de_alumnos_a_cargo
		self.anios_de_antiguedad = anios_de_antiguedad
		super().__init__(**kw)
		
	def __str__(self):
		caden = self.nombre +","+ self.apellido +","+ str(self.dni) +","+ str(self.edad) 
		","+ self.materia +","+ str(self.numero_de_legajo) +","+ str(self.cantidad_de_alumnos_a_cargo) 
		","+ str(self.anios_de_antiguedad)
		return caden
		 
	def corregir(self, lista):
		contador = 0
		for respuesta in lista:
			if respuesta[0] == respuesta[1]:
				contador += 1
		promedio = contador / len(lista)
		print (promedio)

	def dar_clases(self): #Imprimo por pantalla que materia da y cantidad de alumnos  
		mensaje = 'Hola soy profesor de  %s y tengo %s alumnos' % (self.materia,
			self.cantidad_de_alumnos_a_cargo)
		print (mensaje)


if __name__ == '__main__':
	pers = Persona("jose","suarez", 24567822, 44)
	pers.habla("buenas tardes alumnado")
	print(pers.nombre)
	print(str(pers))
	doc = Docente("Geografia", 435576, 12,3, nombre = "Fernando", apellido = "Suares", dni = 34567890,edad = 33)
	print(str(doc))
	print(doc.materia)
	print(doc.nombre)
	doc.dar_clases()
	print(doc.habla())
