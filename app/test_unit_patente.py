import unittest
from model.patente import Patente

class TestUnitarios(unittest.TestCase):
    def setUp(self):
        self.patente = Patente()

    def test_crear_patente(self):
        self.assertEqual(self.patente.crear_patente_ser(42), 'AAAA041')
        self.assertEqual(self.patente.crear_patente_ser(1000), 'AAAA999')

    def test_crear_patente_param(self):
        self.assertRaises(Exception,self.patente.crear_patente_ser, 500000000)

    def test_llenar_num(self):
        self.assertEqual(self.patente.llenar_num(0), ['0','0','0'])
        self.assertListEqual(self.patente.llenar_num(52), ['0','5','2'])
        self.assertIs(type(self.patente.llenar_num(001)), list)

    def test_llenar_num_exc(self):
        self.assertRaises(Exception,self.patente.llenar_num,'001')

    def test_crear_patente_exc(self):
        self.assertRaises(Exception,self.patente.llenar_num,'874434j')

if __name__ == "__main__":
    unittest.main()
