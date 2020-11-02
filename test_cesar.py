import unittest
from vigenere import cesar
from testing_utils import BaseTestCase


class TestCesar(BaseTestCase):

    def test_cesar(self):
        test_cases = [
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

        self.run_tests(test_cases, cesar)

    def ok_message(self, args, expected):
        decode_encode = "encoding" if args[2] else "decoding"
        print(
            f"OK    : {decode_encode} \"{args[0]}\" with key \"{args[1]}\", "
            f"result is \"{expected}\"")

    def error_message(self, args, expected, result):
        decode_encode = "encoding" if args[2] else "decoding"
        print(
            f"ERROR : {decode_encode} \"{args[0]}\" with key \"{args[1]}\", "
            f"result should be \"{expected}\" but was \"{result}\"")


if __name__ == '__main__':
    unittest.main()
