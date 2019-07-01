import math

class Poligono:
    def __init__(self, vertices):
        self.vertices = vertices
        #print(self.vertices[1][0])
    def __str__(self):
        return str(self.vertices)

class Rectangulo(Poligono):
    def __init__(self, **kw):
        super().__init__(**kw)
    def altura(self):
        if self.vertices[0][0] == self.vertices[1][0]:
            altura = math.sqrt (abs((self.vertices[1][0]- self.vertices[0][0])**2+(self.vertices[1][1]- self.vertices[0][1])**2))
            return altura
        elif self.vertices[0][0] == self.vertices[2][0]:
            altura = math.sqrt (abs((self.vertices[2][0]- self.vertices[0][0])**2+(self.vertices[2][1]- self.vertices[0][1])**2))
            return altura
        elif self.vertices[0][0] == self.vertices[3][0]:
            altura = math.sqrt (abs((self.vertices[3][0]- self.vertices[0][0])**2+(self.vertices[3][1]- self.vertices[0][1])**2))
            return altura

    def base(self):
        if self.vertices[1][1] == self.vertices[2][1]:
            base = math.sqrt (abs((self.vertices[2][0]- self.vertices[1][0])**2+(self.vertices[2][1]- self.vertices[1][1])**2))
            if not base == self.altura():
                return base
        elif self.vertices[1][1] == self.vertices[3][1]:
            base = math.sqrt (abs((self.vertices[3][0]- self.vertices[1][0])**2+(self.vertices[3][1]- self.vertices[1][1])**2))
            if not base == self.altura():
                return base
        elif self.vertices[1][1] == self.vertices[0][1]:
            base = math.sqrt (abs((self.vertices[0][0]- self.vertices[1][0])**2+(self.vertices[0][1]- self.vertices[1][1])**2))
            if not base == self.altura():
                return base

    def superficie(self):
        return self.base() * self.altura()

if __name__ == '__main__':
    print('_____________clase Rectangulo_______________')
    print()
    #pol = Poligono([(1,2),(1,5),(6,2),(6,5)])
    #rect = Rectangulo([[1,2],[1,5],[6,2],[6,5]])
    rect = Rectangulo(vertices = [(1,2),(1,5),(6,2),(6,5)])
    print(rect.altura())
    print(rect.base())
    print(rect.superficie())
    print(str(rect))
    print(dir(rect))
    print(vars(rect))
