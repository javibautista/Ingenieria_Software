#Priscila aportó las clases
#la mala identacion se dejo poque corria
#quite los input y variables 
class Empleado():
    def __init__(self,nombre,apellido,edad,salario):
        print("Empleado\n")
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.salario=salario
        super(Empleado,self).__init__()

    def cobrar_sueldo(self,msje,a,b,c):
        self.nombre#(input("ingrese el nombre: "))
        self.apellido#(input("ingrese el apellido: "))
        self.salario#(float(input("ingrese el salario: ")))
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
    def __init__(self,zona,nombre,apellido,edad,salario):
        self.zona=zona
        print("Repartidor\n")
        super(Repartidor,self).__init__(nombre,apellido,edad,salario)
    def recibir_plus(self,porcentaje,edad):
        #edad=int(input("Ingrese la edad: "))
        #porcentaje=float(input("Ingrese el porcentaje del plus: "))
        if(self.edad<25 and self.zona==3):
          salario+=(self.salario*porcentaje/100)
          print("Recibio plus")
          print (salario)
        else:
          print('No recibio')
class Comercial(Empleado):
    def __init__(self,comision,nombre,apellido,edad,salario):
        self.comision=comision
        print("Comercial\n")
        super(Comercial,self).__init__(nombre,apellido,edad,salario)
    def recibir_plus(self,porcentaje,edad,zona,salario): 
          #edad=int(input("Ingrese la edad: "))
          #porcentaje=float(input("Ingrese el porcentaje del plus: "))
          if(edad<25 and zona==3):
            salario+=(salario*porcentaje/100)
            print("Recibio plus")
          #print (salario)  
          else:
            print('No recibio plus')
        
if __name__=="__main__":
    print('\n______ Empleado ______\n')
    empelado=Empleado("Juan","Vazquez",45,200)
    empelado.cobrar_sueldo("retire dinero","Juan","Vazquez",599)
    print(empelado)
    print('\n______ Repartidor ______\n')
    repartidor=Repartidor("zona2","juana","velasquez",23,456)
    repartidor.recibir_plus(6,25)
    print(repartidor)
    print('\n______ Comercial ______\n')
    comercial=Comercial(50,"Andrea","Bautista",23,456)
    print('Comision:%s'%(comercial.comision))
    comercial.recibir_plus(567,23,3,567)
    print(comercial)
    print('dir(obj):\n %s \n'%(dir(comercial)))
    print('vars(obj):\n %s'%(vars(comercial)))
