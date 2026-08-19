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
