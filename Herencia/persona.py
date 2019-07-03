class Persona:
	def __init__(self, nombre, apellido, dni, edad):
		self.nombre = nombre
		self.apellido = apellido
		self.dni = dni
		self.edad = edad
		
	def habla(self, string):
		print(string)
	#Me permite saber si lo que pregunto ocupa la misma direccionde memoria
	def __cmp__(self, otro):
		diferencia = (self.edad) - (otro.edad)
		if diferencia < 0:
			return -1
		elif diferencia > 0:
			return 1
		else:
			return 0
	#Comparo 2 objetos para saber si son iguales
	def __eq__(self,objeto2):
		print('Las edades son iguales?:',end='')
		if self.edad==objeto2.edad:
			return True
		else:
			return False
	#def __eq__(self, other):
		#return ((self.apellido, self.nombre) == (other.apellido, other.nombre))
	#me devuelve la representacion del objeto
	def __repr__(self):
		#return self.nombre, self.apellido  #-->('Juan', 'Ramirez')
		return "%s %s" % (self.nombre, self.apellido)   #--> Juan Ramirez
		
class Docente(Persona):
	def __init__(self, materia, numero_de_legajo, cantidad_de_alumnos_a_cargo, anios_de_antiguedad, **kw):#**kw es llamado si es requerido
		#--> **:comprime,guarda(diccionario)
		#--> kw: variable toma 1ª arg posicional y luego clave=valor(nombre=valor)
		super().__init__(**kw)
		self.materia = materia#['Geografía', 'Matemática', 'Programación']#
		self.numero_de_legajo = numero_de_legajo
		self.cantidad_de_alumnos_a_cargo = cantidad_de_alumnos_a_cargo
		self.anios_de_antiguedad = anios_de_antiguedad

	def __str__(self):
		return "materia:{}, numero de legajo:{}, cantidad de alumnos a cargo:{}, años de antiguedad:{}".format(
		 self.materia, self.numero_de_legajo, self.cantidad_de_alumnos_a_cargo, self.anios_de_antiguedad)

	def corregir(self, respuesta_correcta, respuesta_alumno):
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
		super().__init__( **kw)

	def dar_teorico(self, unidad):
		self.unidad = unidad
		return 'El docente teorico da la: {}'.format(self.unidad)
	def proponer_examen(self):
		if self.materia == 'Geografía':
			print('Cuál es el río más ancho del mundo?\n1) De la plata*\n2) Nylo\n3) Amazonas')
		elif self.materia == 'Matemática':
			print('Cuántos lados tiene un polígono?\n1) 5\n2) Más de 2*\n3) 5 o más')
		elif self.materia == 'Programación':
			print('Que es Scrum?\n1) Una forma de escribir código\n2) Una metodología ágil*\n3) Una herramienta de debugging')
		else:
		    print('Ingreso mal la materia debe ser una de estas: Geografía, Matemática, Programación')

class DocentePractico(Docente):

	def __init__(self, **kw):
		super().__init__(**kw)

	def dar_practico(self,unidad):
		self.unidad = unidad
		print(self.unidad)#print('El docente de práctica da la: %s'%(self.unidad))
		if self.materia == 'Matemática':
			print ('Cuanta plata gastaste si hiciste 10km en un auto que consume 1.5litros por cada kilometro y la nafta cuesta 50 pesos por litro? \n1)800\n2)750\n3)500')
		elif self.materia == 'Programación':
			print('En python,que valor resulta de hacer "a==b==a is b" si tanto a como b tiene el valor [1,2,3]? \n1)True\n2)False\n3)Da error')
		else:
		    print('Ingreso mal la materia debe ser una de estas: Matemática, Programación')

if __name__ == '__main__':
	#profe = Persona('Martin', 'Gaitan', 25678930, 38)
	"""
	docente = Docente('Maria', 'Juarez', 23465762,33, 'Matemática',35462, 12, 3)
	docente.dar_clases('Unidad Nª 5')
	docente.corregir([(10,20),(5,10)])
	"""
	print('______ DOCENTE ______')
	doc = Docente('Geografía',numero_de_legajo=35462, cantidad_de_alumnos_a_cargo=12, anios_de_antiguedad=3,nombre='Juan', apellido='Ramirez', dni=23465762,edad=33)
	# Redefinir el metodo str me permite printear el objeto
	print(doc)
	print(doc.__repr__())
	#print('dir(obj):\n %s \n'%(dir(doc)))
	print('vars(obj):\n %s'%(vars(doc)))
	# Se agregó el **kw, para instanciar ahora se debe poner:
	#el primer argumento como posicional y luego po clave(nombre igualado a su valor)
	
	#print('______ DOCENTE TEORICO ______')
	#teo = DocenteTeorico(nombre='Juan', apellido='Ramirez', dni=23465762,edad=33, materia='Geografía',numero_de_legajo=35462, cantidad_de_alumnos_a_cargo=12, anios_de_antiguedad=3)
	#print(teo.dar_teorico('Unidad Nª8'))
	#teo.proponer_examen()
	#teo.corregir((10,20),(5,10))
	
	#teo.habla('Hola')
	#print(str(teo))
	#print('______ DOCENTE PRACTICO ______')
	#pra = DocentePractico('Carla', 'Fernandez', 22463762,21, 'Matemática',12462, 17, 4)
	#pra.dar_practico('Unidad Nª1')
	#pra.corregir((14,25),(14,10))
	#pra.habla('Soy profesora')
	#print(str(pra))
	#print(teo.__eq__(pra))
	#print(pra.__repr__())
	#print(teo.__cmp__(pra))
	#print('______ TEORICO2 ______')
	#teo2 = DocenteTeorico('Myrian', 'Sosa', 21465762,35, 'Programación',35462, 22, 5)
	#print(teo2.dar_teorico('Unidad Nª2'))
	#teo2.proponer_examen()
	#teo2.corregir((10,20),(10,20))
	#print(str(teo2))
	#print('dir(obj):\n %s \n'%(dir(teo)))
	#print('vars(obj):\n %s'%(vars(teo)))
	
