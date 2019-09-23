import unittest
import sut
#from math import math.sum
#from unittest.mock.patch(math.exp, math.sqrt)
from unittest.mock import MagicMock, mock_open
from unittest.mock import patch, mock_open
class TestSut(unittest.TestCase):
    """
    def sumalista(listaNumeros):
        if len(listaNumeros) == 1:
            return listaNumeros[0]
        else:
            return listaNumeros[0] + sumalista(listaNumeros[1:])
    """
    #1
    def test_productoria(self):
        productoria = sut.productoria([1,2,3,4,5],3)
        self.assertTrue(productoria==6)
        #2
    def test_sumatoria(self):
        sumatoria = sut.sumatoria([1,2,3,4,5],3)
        self.assertTrue(sumatoria==6)
        #3
    def tests_area(self):
        area = sut.area(3,2)
        self.assertTrue(area==6)
        #4
    def tests_saludar(self):
        saludar = sut.saludar('Javier')
        self.assertTrue(saludar=='Hola Javier')
        #5
    def tests_sumar(self):
        sumar = sut.sumar(3, 7)
        #print(sumar)
        #Por MagicMock return 2
        #el patch corige eso
        self.assertTrue(sumar == 10)
        #6
    def tests_multiplicar(self):
        multiplicar = sut.multiplicar(3,2)
        self.assertTrue(multiplicar==6)
        #7
    def tests_valorabsoluto(self):
        valorabsoluto = sut.valorabsoluto(-5)
        self.assertTrue(valorabsoluto==5)
        #8
    def tests_comparar(self):
        comparar = sut.comparar(5, 5)
        self.assertTrue(comparar== 'A y B son iguales')
        #9
    @patch('sut.sumar')
    def tests_costototal(self, sumar):
        sumar.return_value = 2 #usando patch sut.sumar
        #sut.sumar=MagicMock(return_value=2) #entes de usar patch
        a = sut.costototal(5, 4)
        esperado = 'El costo total es $2'
        self.assertEqual(a, esperado)
        #aqui no lo toma sino
        #salta al siguiente "test_supercalc"
    def test_supercalc(self):
        math.exp=MagicMock(return_value=2)
        math.sqrt=MagicMock(return_value=2)
        a = sut.supercalc(3)
        self.assertTrue(a == 2)
        
    @patch('math.exp')
    @patch('math.sqrt')
    def test_supercalc(self, sqrt, exp):
        sqrt.return_value = 2
        exp.return_value = 2
        a = sut.supercalc(3)
        self.assertTrue(a == 2)
        
    def test_CalcuClass_sum(self):
        calc = sut.CalcuClass().suma(a=5, b=4)
        self.assertTrue(calc == 9)
        
    def test_CalcuClass_pro(self):
        calcu = sut.CalcuClass().producto(a=5, b=8)
        self.assertTrue(calcu == 40)
        
    def test_CalcuClass_list(self):
        calcu = sut.CalcuClass().sumar_varios(lista = [3,7])
        self.assertTrue(calcu == 10)

if __name__ == '__main__':
    unittest.main()
