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

	def __eq__(self,objeto2):
			print('Las edades son iguales?:',end='')
			if self.edad==objeto2.edad:
					return True
			else:
					return False
	#def __eq__(self, other):
		#return ((self.apellido, self.nombre) == (other.apellido, other.nombre))

	def __repr__(self):
			return "%s %s" % (self.nombre, self.apellido)
		
class Docente(Persona):
	def __init__(self,materia, numero_de_legajo, cantidad_de_alumnos_a_cargo, anios_de_antiguedad,**kw):
		self.materia = ["Geografia", "Matematica", "Programacion"]
		self.numero_de_legajo = numero_de_legajo
		self.cantidad_de_alumnos_a_cargo = cantidad_de_alumnos_a_cargo
		self.anios_de_antiguedad = anios_de_antiguedad
		print(materia,numero_de_legajo,cantidad_de_alumnos_a_cargo,anios_de_antiguedad)
		super().__init__(**kw)

	def __str__(self):
		return "Nombre: {}, Apellido: {}, DNI: {}, Edad: {}".format(
		self.nombre, self.apellido, self.dni, self.edad)

	def corregir(self, respuesta):
		self.respuesta_correcta = respuesta_correcta
		self.respuesta_alumno = respuesta_alumno
		respuesta = []
		respuesta.append(self.respuesta_correcta)
		respuesta.append(self.respuesta_alumno)
		respuesta = respuesta#[(respuesta_correcta), (respuesta_alumno)]
		promedio1 = (respuesta[1][0] * 100) / respuesta[0][0] #comparo las tuplas
		promedio2 = (respuesta[1][1] * 100) / respuesta[0][1]
		promedio = (promedio1 + promedio2) / 2
		print('El promedio del alumno es del: {} %'.format(promedio))

	def dar_clases(self, unidad):#Imprimo por pantalla que materia da y cantidad de alumnos  
		unidad = unidad
		print('Estoy dando la clase de  %s y tengo %s alumnos' % (unidad, self.cantidad_de_alumnos_a_cargo))

class DocenteTeorico(Docente):
	def __init__(self, **kw):
		#Persona.__init__(self, nombre, apellido, dni, edad)
		super().__init__(**kw)

	def __str__(self):
		return "Nombre: {}, Apellido: {}, DNI: {}, Edad: {}".format(
		self.nombre, self.apellido, self.dni, self.edad)

	def dar_teorico(self, unidad):
		return 'El docente teorico da la: {}'.format(unidad)
		#materia = ['Geografía', 'Matemática', 'Programación']

	def proponer_examen(self):
		if self.materia == 'Geografía':
			print('Cuál es el río más ancho del mundo?\n1) De la plata*\n2) Nylo\n3) Amazonas')
		elif self.materia == 'Matemática':
			print('Cuántos lados tiene un polígono?\n1) 5\n2) Más de 2*\n3) 5 o más')
		elif self.materia == 'Programación':
			print('Que es Scrum?\n1) Una forma de escribir código\n2) Una metodología ágil*\n3) Una herramienta de debugging')

class DocentePractico(Docente):
	def __init__(self,**kw):
		#Persona.__init__(self, nombre, apellido, dni, edad)
		super().__init__(**kw)

	def __str__(self):
		return "Nombre: {}, Apellido: {}, DNI: {}, Edad: {}".format(
		self.nombre, self.apellido, self.dni, self.edad)

	def DarPractico(self,unidad):
		self.unidad=unidad
		print(self.unidad)
		if self.materia == 'Matemática':
			print ("cuanta plata gastaste si hiciste 10km en un auto que consume 1.5litros por cada kilometro y la nafta cuesta 50 pesos por litro? \n1)800,\n2)750,\n3)500" )
		else:
			if self.materia == 'Programación':
				print ("En python,que valor resulta de hacer 'a==b==a is b' si tanto a como b tiene el valor [1,2,3]? \n1)True,\n2)False,\n3)Da error")

if __name__ == '__main__':
	teo=DocenteTeorico(materia='Geografia',numero_de_legajo=24,cantidad_de_alumnos_a_cargo=34,anios_de_antiguedad=45,nombre="javier",apellido="avila",dni=23424354545,edad=34)
	pra=DocenteTeorico(materia='Programación',numero_de_legajo=23,cantidad_de_alumnos_a_cargo=37,anios_de_antiguedad=43,nombre="jonatan",apellido="avila",dni=2343424324,edad=23)	
	print(pra)
	print(str(pra))
	print(teo.__cmp__(pra))	


