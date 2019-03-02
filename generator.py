from random import randint


def gen_arr(n):
    for _ in range(n):
        yield {'T': randint(1000, 9999), 'V': randint(0, 100), 'O': randint(0, 100)}
