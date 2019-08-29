import calculos
import unittest
from unittest.mock import MagicMock

class TestBase(unittest.TestCase):
    def test_richtSequenceOfCalls(self):
        calculos.cuadrado = MagicMock(return_value=2)
        calculos.dividir = MagicMock(return_value=2)
        a = calculos.calcula(5)
        #esperado = 12.5
        esperado = 2
        self.assertEqual(a, esperado)
        
if __name__ == '__main__':
    unittest.main()
