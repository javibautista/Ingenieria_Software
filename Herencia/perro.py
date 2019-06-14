class Perro:
	def __init__(self, posicion):
		self.posicion = 0
		
	def caminar(self):
		self.posicion += 4
		
	def ladrar(self):
		print("GUAU GUAU")

if __name__ == '__main__':
	perro = Perro(0)
	perro.caminar()
	print(perro.posicion)
	perro.ladrar()
	def pasear_mascota(caminar):
		caminar += 5
		camina = caminar + perro.posicion
		print("La mascota quedo en ", camina)
	
pasea = pasear_mascota(2)
print(pasea)
