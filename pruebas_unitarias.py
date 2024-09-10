import unittest
from main import Geometria

class TestGeometria(unittest.TestCase):

    def setUp(self):
        self.geo = Geometria()

    def test_area_rectangulo(self):
        self.assertEqual(self.geo.area_rectangulo(5, 3), 15)
        self.assertEqual(self.geo.area_rectangulo(7, 2), 14)

    def test_perimetro_rectangulo(self):
        self.assertEqual(self.geo.perimetro_rectangulo(5, 3), 16)
        self.assertEqual(self.geo.perimetro_rectangulo(7, 2), 18)

    def test_area_cuadrado(self):
        self.assertEqual(self.geo.area_cuadrado(4), 16)
        self.assertEqual(self.geo.area_cuadrado(7), 49)

    def test_perimetro_cuadrado(self):
        self.assertEqual(self.geo.perimetro_cuadrado(4), 16)
        self.assertEqual(self.geo.perimetro_cuadrado(7), 28)

if __name__ == "__main__":
    unittest.main()
