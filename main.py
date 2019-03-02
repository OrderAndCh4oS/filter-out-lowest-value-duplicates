import time
from itertools import groupby
from operator import itemgetter
from random import random, randint


def timer(f, param, iterations = 1000):
    start = time.time()
    r = False
    for i in range(iterations):
        r = f(param)
        if isinstance(r, int) and r == -1:
            return -1

    return "%.9f" % ((time.time() - start) / iterations) if r is not False else -1


def sarcoma(arr):
    t_v = {}
    result = []
    for row in arr:
        if not t_v.get(row['T']):
            t_v[row['T']] = (row['V'], len(result))
            result.append(row)
            continue

        if row['V'] > t_v[row['T']][0]:
            t_v[row['T']] = (row['V'], t_v[row['T']][1])
            result[t_v[row['T']][1]] = row

    return result


def DeepSpace(arr):
    arr.sort(key=lambda val: val['T'])
    return [max(group, key=lambda d: d['V']) for _, group in groupby(arr, key=lambda d: d['T'])]


def RoadRunner(arr):
    unique = {}
    arr = sorted(arr, key=itemgetter('T'))
    for dic in arr:
        key = dic['T']
        found = unique.get(key)

        # If value found and doesn't exceed current maximum, just ignore
        if found and dic['V'] <= found['V']:
            continue

        # otherwise just update normally
        unique[key] = dic

    return list(unique.values())


def Patrick_Artner(arr):
    arr = sorted(arr, key=lambda x: x["T"])
    arr2 = []
    for e in arr:
        t, v, o = e["T"], e["V"], e["O"]

        # we already stored something and same T
        if arr2 and arr2[-1]["T"] == t:

            # smaller V ?
            if arr2[-1]["V"] < v:
                # overwrite dict elements
                arr2[-1]["V"] = v
                arr2[-1]["O"] = o

        # did not store anything or other T
        else:
            arr2.append(e)

    return arr2


arr = [
    {'T': 2345, 'V': 50, 'O': 5},
    {'T': 1234, 'V': 10, 'O': 1},
    {'T': 2345, 'V': 30, 'O': 3},
    {'T': 3456, 'V': 40, 'O': 91},
]


def gen_lrg_arr(n):
    for _ in range(n):
        yield {'T': randint(1000, 9999), 'V': randint(0, 100), 'O': randint(0, 100)}


print(timer(sarcoma, arr), '@sarcoma', sarcoma(arr))
print(timer(DeepSpace, arr), '@DeepSpace', DeepSpace(arr))
print(timer(RoadRunner, arr), '@RoadRunner', RoadRunner(arr))
print(timer(Patrick_Artner, arr), '@Patrick_Artner', Patrick_Artner(arr))


def gen_lrg_arr(n):
    for _ in range(n):
        yield {'T': randint(1000, 9999), 'V': randint(0, 100), 'O': randint(0, 100)}


rand_small_arr = list(gen_lrg_arr(10))

print('\nSarcoma Proof:')
print(sorted(sarcoma(rand_small_arr), key=lambda val: val['T']), '\n')
print('DeepSpace Proof:')
print(DeepSpace(rand_small_arr), '\n')
print('RoadRunner Proof:')
print(RoadRunner(rand_small_arr), '\n')
print('Patrick_Artner Proof:')
print(Patrick_Artner(rand_small_arr), '\n')

lrg_arr = list(gen_lrg_arr(100000))

print(timer(sarcoma, lrg_arr, 100), '@sarcoma')
print(timer(DeepSpace, lrg_arr, 100), '@DeepSpace')
print(timer(RoadRunner, lrg_arr, 100), '@RoadRunner')
print(timer(Patrick_Artner, lrg_arr, 100), '@Patrick_Artner')
