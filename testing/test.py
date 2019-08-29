import unittest
import sut
from unittest.mock import MagicMock
from unittest.mock import patch
#import math

class TestSut(unittest.TestCase):

    def test_costototal(self):
        sut.sumar=MagicMock(return_value=2)
        a = sut.costototal(3,2)
        #print(a)
        self.assertTrue(a == "El costo total es $2")


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


if __name__ == '__main__':
    unittest.main()
