import unittest
from comprehensions import intersect
from testing_utils import BaseTestCase


class TestIntersect(BaseTestCase):

    def test_intersect(self):
        test_cases = [
            (
                {(12, 'douze'), (10, 'dixA'), (8, 'huit'), },
                {(5, 'cinq'), (10, 'dixB'), (15, 'quinze'), },
                {'dixA', 'dixB'}
            ),
            (
                {(1, 'unA'), (2, 'deux'), (3, 'troisA')},
                {(1, 'unB'), (2, 'deux'), (4, 'quatreB')},
                {'unA', 'unB', 'deux'}
            )
        ]
        self.run_tests(test_cases, intersect)

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


[
    (
        {(12, 'douze'), (10, 'dixA'), (8, 'huit'), },
        {(5, 'cinq'), (10, 'dixB'), (15, 'quinze'), },
        {'dixA', 'dixB'}
    ),
    (
        {(1, 'unA'), (2, 'deux'), (3, 'troisA')},
        {(1, 'unB'), (2, 'deux'), (4, 'quatreB')},
        {'unA', 'unB', 'deux'}
    )
]
