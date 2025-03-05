#unit testing
import unittest
import Actividad7_1_numeros

class TestRacionales(unittest.TestCase):

    def test_print_hello(self):
        #crear clase
        self.assertEqual('Hello Adrian')

if __name__ == '__main__':
    unittest.main()