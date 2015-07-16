#!/usr/bin/env python
import unittest
from convertcelcius.Convert import celsius2fahren

class TestConvertFunction(unittest.TestCase):
    """
    For testing Convert.py module
    """
    def testString(self):
        """
        testing celsius2fahren func with string parameters
        """
        self.assertFalse(celsius2fahren("fourteen"))
        self.assertEqual(0, celsius2fahren('-273'))
        self.assertEqual(273, celsius2fahren('0'))
        self.assertEqual(300, celsius2fahren('27'))

    def testInt(self):
        """
        testing celsius2fahren func with int parameters
        """
        self.assertEqual(False, celsius2fahren(-500))
        self.assertEqual(False, celsius2fahren(-274))
        self.assertEqual(0, celsius2fahren(-273))
        self.assertEqual(272, celsius2fahren(-1))
        self.assertEqual(273, celsius2fahren(0))
        self.assertEqual(500, celsius2fahren(227))

if __name__ == '__main__':
    unittest.main()
