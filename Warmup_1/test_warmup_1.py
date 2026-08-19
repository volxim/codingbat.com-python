import unittest
from sqlite3.dbapi2 import paramstyle

from .warmup_1 import sleep_in, monkey_trouble, sum_double


class TestWarmup1(unittest.TestCase):
    def test_sleep_in(self):
        sleep = True
        cases_sleep_in = [
            (False, True, sleep),
            (True, False, not sleep),
            (False, False, sleep),
            (True, True, sleep)
        ]
        for weekday, vacation, sleep in cases_sleep_in:
            with self.subTest(f"weekday={weekday}, vacation={vacation}, expected={sleep}"):
                self.assertEqual(sleep_in(weekday=weekday, vacation=vacation),
                                 sleep,
                                 f"weekday={weekday}, vacation={vacation}, expected={sleep}")

    def test_monkey_trouble(self):
        in_trouble = True
        smiling_cases = [
            (True, True, in_trouble),
            (False, False, in_trouble),
            (True, False, not in_trouble),
            (False, True, not in_trouble)
        ]

        for a_smile, b_smile, in_trouble in smiling_cases:
            with self.subTest(a_smile=a_smile, b_smile=b_smile, expected=in_trouble):
                self.assertEqual(monkey_trouble(a_smile, b_smile), in_trouble)

    def test_sum_double(self):
        cases = [
            (0, 0, 0),
            (0, 1, 1),
            (1, 0, 1),
            (1, 1, 4),
            (1, 2, 3),
            (2, 1, 3),
            (-4, -3, -7),
            (-4, 3, -1),
            (-3, -3, -12),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b, c=expected):
                self.assertEqual(sum_double(a,b), expected)



if __name__ == "__main__":
    unittest.main()
