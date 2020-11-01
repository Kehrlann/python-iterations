import unittest
from vigenere import cesar

class TestCesar(unittest.TestCase):

    def test_cesar(self):
        expected = [
                ('=', 'C', True, '='),
                ('A', 'C', True, 'D'),
                ('a', 'C', True, 'd'),
                ('A', 'c', True, 'D'),
                ('D', 'C', False, 'A'),
                ('A', 'L', True, 'M'),
                ('Z', 'L', True, 'L'),
                ('a', 'c', True, 'd'),
                ('N', 'L', True, 'Z'),
                ('O', 'L', True, 'A'),
                ('D', 'C', False, 'A'),
                ('D', 'c', False, 'A'),
                ('D', 'c', False, 'A'),
                ('a', 'c', True, 'd'),
                ('a', 'c', False, 'x'),
                ('a', 'J', True, 'k'),
                ('a', 'J', False, 'q'),
                ('a', 'T', True, 'u'),
                ('a', 'T', False, 'g'),
                ('a', 'x', True, 'y'),
                ('a', 'x', False, 'c'),
                ('N', 'c', True, 'Q'),
                ('N', 'c', False, 'K'),
                ('N', 'J', True, 'X'),
                ('N', 'J', False, 'D'),
                ('N', 'T', True, 'H'),
                ('N', 'T', False, 'T'),
                ('N', 'x', True, 'L'),
                ('N', 'x', False, 'P'),
                ('z', 'c', True, 'c'),
                ('z', 'c', False, 'w'),
                ('z', 'J', True, 'j'),
                ('z', 'J', False, 'p'),
                ('z', 'T', True, 't'),
                ('z', 'T', False, 'f'),
                ('z', 'x', True, 'x'),
                ('z', 'x', False, 'b')
            ]
        for *args, result in expected:
            self.assertEqual(cesar(*args), result)

if __name__ == '__main__':
    unittest.main()
