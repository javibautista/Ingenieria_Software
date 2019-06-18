class Empleado():
    def __init__(self,nombre,apellido,edad,salario):
        print("Empleado")
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.salario=salario
        super(Empleado,self).__init__()

    def cobrar_sueldo(self,msje,a,b,c):
        a=(input("ingrese el nombre: "))
        b=(input("ingrese el apellido: "))
        c=(float(input("ingrese el salario: ")))
        if(self.nombre and self.apellido and self.salario):
            if (self.salario > 0 and self.salario < 100000):
                mje = "Retire su dinero"
        else:
            mje = "Ha ingresado un dato erroneo"
        print (mje)
    def __str__(self):
        return "Nombre: {}, Apellido: {}, Edad: {}, Salario: {}.".format(
            self.nombre, self.apellido, self.edad, self.salario)


class Repartidor(Empleado):
    def __init__(self,zona,nombre,edad,apellido,salario):
        self.zona=zona
        print("Repartidor")
        super(Repartidor,self).__init__(nombre,edad,apellido,salario)
    def recibir_plus(self,porcentaje,edad):
        edad=int(input("Ingrese la edad: "))
        porcentaje=float(input("Ingrese el porcentaje del plus: "))
        if(self.edad<25 and self.zona==3):
          salario+=(self.salario*porcentaje/100)
          print("Recibio plus")
          print (salario)
class Comercial(Empleado):
    def __init__(self,comision,nombre,apellido,salario,edad):
        self.comision=comision
        print("Comercial")
        super(Comercial,self).__init__(nombre,edad,apellido,salario)
    def recibir_plus(self,porcentaje,edad,zona,salario): 
          edad=int(input("Ingrese la edad: "))
          porcentaje=float(input("Ingrese el porcentaje del plus: "))
          if(edad<25 and zona==3):
            salario+=(salario*porcentaje/100)
          print("Recibio plus")
          #print (salario)  
        
if __name__=="__main__":
    empelado=Empleado("juana","velasquez",45,200)
    empelado.cobrar_sueldo("retire dinero","juana","velasquez",599)
    print(empelado)
    repartidor=Repartidor("zona2","juana","velasquez",23,456)
    repartidor.recibir_plus(6,25)
    print(repartidor)
    comercial=Comercial(50,"juana","velasquez",23,456)
    comercial.recibir_plus(567,23,3,567)
    print(comercial)
