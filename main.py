def filter_out_lowest_values_by_key(iterable, key, value):
    t_v = {}
    result = []
    for row in iterable:
        if not t_v.get(row[key]):
            t_v[row[key]] = (row[value], len(result))
            result.append(row)
            continue

        if row[value] > t_v[row[key]][0]:
            t_v[row[key]] = (row[value], t_v[row[key]][1])
            result[t_v[row[key]][1]] = row

    return result


if __name__ == '__main__':
    arr = [
        {'T': 2345, 'V': 50, 'O': 5},
        {'T': 1234, 'V': 10, 'O': 1},
        {'T': 2345, 'V': 30, 'O': 3},
        {'T': 3456, 'V': 40, 'O': 91}
    ]

    print(filter_out_lowest_values_by_key(arr, 'T', 'V'))
