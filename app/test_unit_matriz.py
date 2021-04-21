import unittest
from model.matriz import Matriz

class TestUnitarios(unittest.TestCase):
    def setUp(self):
        self.matriz = Matriz(6,8,3)
        self.matriz.crear_matriz()

    def test_crear_matriz(self):
        self.assertIsInstance(self.matriz, Matriz)
        self.assertIsNot(type(self.matriz), str)

    def test_crear_matriz_tipo(self):
        self.assertIsInstance(self.matriz.r, int)
        self.assertIsInstance(self.matriz.c, int)
        self.assertIsInstance(self.matriz.z, int)

    def test_crear_matriz_excep(self):
        matriz_err = Matriz('6','x',8)
        self.assertRaises(Exception, matriz_err.crear_matriz)

    def test_sumar_matriz(self):
        self.assertNotEqual(self.matriz.sumar_matriz(2,4), 6)
        self.assertEqual(self.matriz.sumar_matriz(2,4), 75)

    def test_sumar_matriz_excep(self):
        self.assertRaises(Exception, self.matriz.sumar_matriz, '8', 5.4)

    def test_sumar_matriz_param(self):
        self.assertEqual(self.matriz.sumar_matriz(-4,8), 0)



if __name__ == "__main__":
    unittest.main()
