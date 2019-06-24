class Animal:
	#def __init__(self):
		#super().__init__()#super(Animal,self).__init__()
	def pasear_mascota(self):
		for _ in range(5):
			self.caminar()
		print("La mascota quedó en {}".format(self.posicion))
		#print("La mascota quedo en %d"%(self.posicion))
	def __str__(self):
		return "Posicion donde se encuentra el Animal: %s"%(self.posicion)
	def __eq__(self,objeto2):
		print('Las Posiciones son iguales?:',end='')
		if self.posicion==objeto2.posicion:
			return True
		else:
			return False

class Gato(Animal):
	def __init__(self, posicion=0):
		super().__init__()#super(Gato,self).__init__()
		self.posicion = posicion
		
	def trepar(self):
		print("Estoy arriba del arbol")
		
	def caminar(self):
		self.posicion += 10
		return self.posicion
	
	def maullar(self):
		print("MIAU")



class Perro(Animal):
	def __init__(self, posicion=0):
		super().__init__()#super(Perro,self).__init__()
		self.posicion = posicion
		
	def caminar(self):
		self.posicion += 4
		return self.posicion
		
	def ladrar(self):
		print("GUAU GUAU")

if __name__ == '__main__':
	print('\n______ PERRO _______\n')
	perro = Perro()
	print(perro.posicion)
	#print(perro.caminar())
	perro.pasear_mascota()
	perro.pasear_mascota()
	perro.pasear_mascota()
	perro.pasear_mascota()
	#print(perro.caminar())
	perro.ladrar()

	print('\n______ GATO _______\n')
	gato = Gato()
	print(gato.caminar())
	print(gato.caminar())
	print(gato.posicion)
	gato.maullar()
	gato.trepar()
	gato.pasear_mascota()
	print(gato.caminar())
	print(str(gato))
	print(perro.__eq__(gato))
	print('dir(obj):\n %s \n'%(dir(gato)))
	print('vars(obj):\n %s'%(vars(gato)))
