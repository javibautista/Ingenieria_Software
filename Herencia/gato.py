class Gato:
	def __init__(self, posicion):
		self.posicion = posicion
		
	def trepar(self):
		print("Esto arriba del arbol")
		
	def caminar(self):
		self.posicion += 10
	
	def maullar(self):
		print("MIAU")
		

def pasear_mascota(Gato, self):
	self.caminar *= 5
	camina = self.caminar + self.posicion
	print("La mascota quedo en ", camina)

if __name__ == '__main__':
	gato = Gato(0)
	#gato.caminar()
	print(gato.posicion)
	gato.maullar()
	
	pasea = pasear_mascota(1)
	print(pasea)
