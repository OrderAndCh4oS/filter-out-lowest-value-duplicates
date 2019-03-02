from generator import gen_arr
from scripts import Patrick_Artner, RoadRunner, DeepSpace, sarcoma
from timer import timer

arr = [
    {'T': 2345, 'V': 50, 'O': 5},
    {'T': 1234, 'V': 10, 'O': 1},
    {'T': 2345, 'V': 30, 'O': 3},
    {'T': 3456, 'V': 40, 'O': 91},
]

print(timer(sarcoma, arr), '@sarcoma', sarcoma(arr))
print(timer(DeepSpace, arr), '@DeepSpace', DeepSpace(arr))
print(timer(RoadRunner, arr), '@RoadRunner', RoadRunner(arr))
print(timer(Patrick_Artner, arr), '@Patrick_Artner', Patrick_Artner(arr))

rand_small_arr = list(gen_arr(10))

print('\nSarcoma Proof:')
print(sorted(sarcoma(rand_small_arr), key=lambda val: val['T']), '\n')
print('DeepSpace Proof:')
print(DeepSpace(rand_small_arr), '\n')
print('RoadRunner Proof:')
print(RoadRunner(rand_small_arr), '\n')
print('Patrick_Artner Proof:')
print(Patrick_Artner(rand_small_arr), '\n')

lrg_arr = list(gen_arr(100000))

print(timer(sarcoma, lrg_arr, 100), '@sarcoma')
print(timer(DeepSpace, lrg_arr, 100), '@DeepSpace')
print(timer(RoadRunner, lrg_arr, 100), '@RoadRunner')
print(timer(Patrick_Artner, lrg_arr, 100), '@Patrick_Artner')
