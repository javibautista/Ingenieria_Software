class Animal:
	#def __init__(self):
		#super(Animal,self).__init__()
	def pasear_mascota(self):
		for _ in range(5):
			self.caminar()
		print("La mascota quedo en {}".format(self.posicion))
		#print("La mascota quedo en %d"%(self.posicion))

class Gato(Animal):
	def __init__(self, posicion=0):
		super(Gato,self).__init__()
		self.posicion = posicion
		
	def trepar(self):
		print("Esto arriba del arbol")
		
	def caminar(self):
		self.posicion += 10
		return self.posicion#return self.posicion
	
	def maullar(self):
		print("MIAU")



class Perro(Animal):
	def __init__(self, posicion=0):
		super(Perro,self).__init__()
		self.posicion = posicion
		
	def caminar(self):
		self.posicion += 4
		return self.posicion#return self.posicion
		
	def ladrar(self):
		print("GUAU GUAU")

if __name__ == '__main__':
	print('______ PERRO _______')
	perro = Perro()
	print(perro.posicion)
	#print(perro.caminar())
	perro.pasear_mascota()
	print(perro.caminar())
	perro.ladrar()

	print('______ GATO _______')
	gato = Gato()
	print(gato.caminar())
	print(gato.posicion)
	gato.maullar()
	gato.trepar()
	gato.pasear_mascota()

