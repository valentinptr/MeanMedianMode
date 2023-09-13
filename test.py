import unittest
from MeanMedianMode import moyenne, mode, meadian

list_input = [3, 12, 11, 7, 5, 5, 6, 4, 10]
correction = [5, 6, 7]

class Test(unittest.TestCase):

    def test_mode(self):
        self.assertEqual(mode(list_input), correction[0])

    def test_meadian(self):
        self.assertEqual(meadian(list_input), correction[1])

    def test_moyenne(self):
        self.assertEqual(moyenne(list_input), correction[2])


if __name__ == '__main__':
    unittest.main()
