import unittest
from comprehensions import aplatir
from testing_utils import BaseTestCase


class TestAplatir(BaseTestCase):

    def test_aplatir(self):
        test_cases = [
            ([], []),
            ([(1,)], [1]),
            (([1],), [1]),
            ([(0, 6, 2), [1, ('a', 4), 5]], [0, 6, 2, 1, ('a', 4), 5]),
            (([1, [2, 3]], ('a', 'b', 'c')), [1, [2, 3], 'a', 'b', 'c']),
            (([1, 6], ('c', 'b'), [2, 3]), [1, 6, 'c', 'b', 2, 3]),
            (((1, [2, 3]), [], 'a', ['b', 'c']), [1, [2, 3], 'a', 'b', 'c'])
        ]
        self.run_tests(test_cases, aplatir)

    def ok_message(self, args, expected):
        print(f"OK    : input {args[0]} -> output {expected}")

    def error_message(self, args, expected, result):
        print(
            f"ERROR : input {args[0]} -> should be {expected}, but was {result}")


if __name__ == '__main__':
    unittest.main()
