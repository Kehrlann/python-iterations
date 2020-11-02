import unittest
from taxes import taxes
from testing_utils import BaseTestCase


class TestTaxes(BaseTestCase):

    def test_taxes(self):
        test_cases = [
            (0, 0),
            (50000, 7500),
            (12500, 0),
            (5000, 0),
            (16500, 800),
            (30000, 3500),
            (100000, 27500),
            (150000, 47500),
            (200000, 70000),
            (12504, 0)
        ]
        self.run_tests(test_cases, taxes)

    def ok_message(self, args, expected):
        print(f"OK    : income {args[0]} -> tax {expected}")

    def error_message(self, args, expected, result):
        print(
            f"ERROR : income {args[0]} -> should be {expected}, but was {result}")


if __name__ == '__main__':
    unittest.main()
