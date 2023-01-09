import unittest
from func import imprima_nombre, greater, suma_int, resta_int


class TestFunc(unittest.TestCase):

    def test_imprima_nombre(self):
        self.assertEqual(
            imprima_nombre(), 
            "Mi nombre es Dave", 
            "Deberia imprimir Dave"
        )
    
    def test_suma_int(self):
        self.assertEqual(suma_int(2, 2), 4, "Deberia ser 4")
    
    def test_resta_int(self):
        self.assertEqual(resta_int(2, 2), 0, "Deberia ser cero")

    #Write a test for greater function
    def test_greater(self):
        self.assertEqual(greater(5, 3), 5, "Deberia ser 5")
        self.assertEqual(greater(3, 5), 5, "Deberia ser 5")
        self.assertEqual(greater(3, 3), 3, "Deberia ser 3")
        

if __name__ == "__main__":
    unittest.main()