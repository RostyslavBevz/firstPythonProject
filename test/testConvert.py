import unittest

from convertcelcius.Convert import celsius2fahren


class TestConvertFunction(unittest.TestCase):
    def testString(self):
        self.assertFalse(celsius2fahren("fourteen"))
        self.assertEqual(0, celsius2fahren('-273'))
        self.assertEqual(273, celsius2fahren('0'))
        self.assertEqual(300, celsius2fahren('27'))

    def testInt(self):
        self.assertEqual(False, celsius2fahren(-500))
        self.assertEqual(False, celsius2fahren(-274))
        self.assertEqual(0, celsius2fahren(-273))
        self.assertEqual(272, celsius2fahren(-1))
        self.assertEqual(273, celsius2fahren(0))
        self.assertEqual(500, celsius2fahren(227))

if __name__ == '__main__':
    unittest.main()