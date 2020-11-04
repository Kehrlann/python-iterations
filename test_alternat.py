import unittest
from comprehensions import alternat
from testing_utils import BaseTestCase


class TestAlternat(BaseTestCase):

    def test_alternat(self):
        test_cases = [
            ((1, 2), ('a', 'b'), [1, 'a', 2, 'b']),
            ((1, 2, 3), ('a', 'b', 'c'), [1, 'a', 2, 'b', 3, 'c']),
            ((1, (2, 3)), ('a', ['b', 'c']), [1, 'a', (2, 3), ['b', 'c']])
        ]
        self.run_tests(test_cases, alternat)

    def ok_message(self, args, expected):
        print(f"OK    : input {args[0]} + {args[1]} -> output {expected}")

    def error_message(self, args, expected, result):
        print(
            f"ERROR : input {args[0]} + {args[1]} -> should be {expected}, but was {result}")


if __name__ == '__main__':
    unittest.main()

    ((1, 2), ('a', 'b'), ),
    ((1, 2, 3), ('a', 'b', 'c'), ),
    ((1, (2, 3)), ('a', ['b', 'c']), ),
