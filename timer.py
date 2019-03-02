import time


def timer(f, param, iterations = 1000):
    start = time.time()
    r = False
    for i in range(iterations):
        r = f(param)
        if isinstance(r, int) and r == -1:
            return -1

    return "%.9f" % ((time.time() - start) / iterations) if r is not False else -1
