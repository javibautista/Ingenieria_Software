
class Persona:
	def __init__(self, nombre, apellido, dni, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.edad = edad
		
	def habla(self, string):
		print(string)
		
class Docente(Persona):
	def __init__(self, nombre, apellido, dni, edad, materia, numero_de_legajo,
	 cantidad_de_alumnos_a_cargo, anios_de_antiguedad):
		 Persona.__init__(self, nombre, apellido, dni, edad)
		 self.materia = ["Geografia", "Matematica", "Programacion"]
		 self.numero_de_legajo = numero_de_legajo
		 self.cantidad_de_alumnos_a_cargo = cantidad_de_alumnos_a_cargo
		 self.anios_de_antiguedad = anios_de_antiguedad
		 
	def corregir(self, respuestas=[(1,2),(1,3)]):	
		respuesta_correcta = respuestas[0]
		respuesta_alumno = respuestas[1]
		promedio = respuesta_correcta == respuesta_alumno #comparo las tuplas
		print (promedio)
			
	def dar_clases(self):#Imprimo por pantalla que materia da y cantidad de alumnos  
		unidad = 'Hola soy profesor de  %s y tengo %s alumnos' % (self.materia[0], self.cantidad_de_alumnos_a_cargo)
		print (unidad)
		

				
if __name__ == '__main__':
	profe = Persona('Martin', 'Gaiten', 25678930, 38)
	docente = Docente("maria", "uarez", 23465762,33, "matematicas",35462, 12, 3)
	docente.dar_clases()
	docente.corregir()
	
	
