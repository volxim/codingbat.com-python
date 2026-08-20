import unittest


def sleep_in(weekday, vacation):
    return not weekday or vacation


def monkey_trouble(a_smile, b_smile):
    return True if a_smile == b_smile else False


def sum_double(a, b):
    c = a + b
    return c if a != b else c << 1


def diff21(n):
    if n > 21:
        return (n - 21) << 1
    else:
        # n <= 21
        return 21 - n


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


def makes10(a, b):
    return True if a == 10 or b == 10 or a + b == 10 else False


def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


def not_string(s: str) -> str:
    return s if s.startswith("not") else "not " + s


def missing_char(s: str, n: int):
    return s[:n] + s[n+1:]

def front_back(s):
  if len(s) <= 1:
    return s
  else:
    return s[-1:]+s[1:-1]+s[0]
