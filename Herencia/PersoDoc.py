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
		print(string)
		
class Docente(Persona): # Creamos la clase hija que hereda de padre
	def __init__(self, nombre, apellido, dni, edad, materia, numero_de_legajo,
		cantidad_de_alumnos_a_cargo, anios_de_antiguedad):
		self.materia = materia  # Especificamos el nuevo atribuo de la clase hija
		self.numero_de_legajo = numero_de_legajo
		self.cantidad_de_alumnos_a_cargo = cantidad_de_alumnos_a_cargo
		self.anios_de_antiguedad = anios_de_antiguedad
		super(Docente,self).__init__(nombre, apellido, dni, edad)
		
	def __str__(self):
		caden = self.nombre +","+ self.apellido +","+ str(self.dni) +","+ str(self.edad) 
		","+ self.materia +","+ str(self.numero_de_legajo) +","+ str(self.cantidad_de_alumnos_a_cargo) 
		","+ str(self.anios_de_antiguedad)
		return caden
		 
	def corregir(self, respuestas=[(1,2),(1,3)]):
		print (respuestas)

	def dar_clases(self): #Imprimo por pantalla que materia da y cantidad de alumnos  
		mensaje = 'Hola soy profesor de  %s y tengo %s alumnos' % (self.materia,
			self.cantidad_de_alumnos_a_cargo)
		print (mensaje)


if __name__ == '__main__':
	pers = Persona("jose","suarez", 24567822, 44)
	print(pers.nombre)
	print(str(pers))
	doc = Docente("Fernando", "Suares", 34567890, 33, "Geografia", 435576, 12, 3)
	print(str(doc))
	print(doc.materia)
	print(doc.nombre)
	doc.dar_clases()

