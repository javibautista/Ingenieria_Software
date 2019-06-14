from Persona import *
from Docente import *

class DocenteTeorico(Persona, Docente):

    def dar_teorico(self, unidad):
        return unidad
    #materia = ['Geografía', 'Matemática', 'Programación']
    def proponer_examen(self):
        if self.materia[0] == 'Geografía':
            print('Cuál es el río más ancho del mundo?\n1) De la plata\n2) Nylo\n3) Amazonas')
        elif self.materia[1] == 'Matemática':
            print('Cuántos lados tiene un polígono?\n1) 5\n2) Más de 2\n3) 5 o más')
        elif self.materia[2] == 'Programación':
            print('Que es Scrum?\n1) Una forma de escribir código\n2) Una metodología ágil\n3) Una herramienta de debugging')
