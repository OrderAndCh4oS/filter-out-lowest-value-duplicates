from itertools import groupby
from operator import itemgetter


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
