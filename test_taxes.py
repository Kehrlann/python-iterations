import unittest
from taxes import taxes


class TestTaxes(unittest.TestCase):

    def test_taxes(self):
        expected = [
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
        errors = 0
        for income, tax in expected:
            if taxes(income) == tax:
                print(f"OK    : income {income} -> tax {tax}")
            else:
                print(
                    f"ERROR : income {income} -> should be {tax}, but was {taxes(income)}")
                errors += 1

        if errors:
            self.fail(f"{errors} errors / {len(expected)} total")


if __name__ == '__main__':
    unittest.main()