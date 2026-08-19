import unittest

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
                self.assertEqual(sum_double(a, b), expected)

    def test_diff21(self):
        diff_target = 21
        cases = [
            # (n, expected)
            (-21, 42),
            (-5, 26),
            (-1, 22),
            (0, 21),
            (1, 20),
            (7, 14),
            (20, 1),
            (21, 0),
            (22, 2),
            (25, 8),
            (42, 42),

        ]

        for n, expected in cases:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(diff21(n), expected)

    def test_makes10(self):
        cases_makes10 = [
            (2,8, True),
            (8,2, True),
            (10,0, True),
            (0,10, True),
            (5,5, True),
            (11,-1, True),
            (-1, 11, True),
            (12, -2, True),
            (-2, 12, True),
        ]

        cases_makes_not_10 = [
            (0, 0, False),
            (2, 9, False),
            (9, 2, False),
            (9, 0, False),
            (0, 9, False),
            (6, 6, False),
            (17, -8, False),
            (-8, 17, False),
            (12, -3, False),
            (-3, 12, False),
            (-10, 0, False),
            (0, -10, False),
        ]

        for a, b, expected in cases_makes10:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertIs(makes10(a, b), expected)

        for a, b, expected in cases_makes_not_10:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertIs(makes10(a, b), expected)



import os
import sys
if __name__ == "__main__":
    # Running directly as a script — add repo root to sys.path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from Warmup_1.solutions import sleep_in, monkey_trouble, sum_double, diff21, makes10

    unittest.main()
else:
    # Running as a module (python -m unittest ...) — relative import works
    from .solutions import sleep_in, monkey_trouble, sum_double, diff21, makes10

