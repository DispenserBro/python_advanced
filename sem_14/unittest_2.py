# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest

from rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_rect = Rectangle(12, 6)
        self.test_square = Rectangle(4)
    
    def test_rect_creation(self):
        self.assertEqual(self.test_rect, Rectangle(12, 6))

    def test_square_creation(self):
        self.assertEqual(self.test_square, Rectangle(4))

    def test_addtion(self):
        self.assertEqual(self.test_rect + self.test_rect, Rectangle(24, 12))

    def test_compare(self):
        self.assertTrue(self.test_rect > self.test_square)

    def test_negative_value(self):
        with self.assertRaises(ValueError):
            rect_1 = Rectangle(-1, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)