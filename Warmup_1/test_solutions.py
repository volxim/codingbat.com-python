import unittest

from .solutions import sleep_in, monkey_trouble, sum_double, diff21

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


if __name__ == "__main__":
    unittest.main()
