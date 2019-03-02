def filter_out_lowest_values(iterable, key, value):
    lookup = {}
    result = []
    for row in iterable:
        if not lookup.get(row[key]):
            lookup[row[key]] = (row[value], len(result))
            result.append(row)
            continue

        if row[value] > lookup[row[key]][0]:
            lookup[row[key]] = (row[value], lookup[row[key]][1])
            result[lookup[row[key]][1]] = row

    return result


if __name__ == '__main__':
    arr = [
        {'T': 2345, 'V': 50, 'O': 5},
        {'T': 1234, 'V': 10, 'O': 1},
        {'T': 2345, 'V': 30, 'O': 3},
        {'T': 3456, 'V': 40, 'O': 91}
    ]

    print(filter_out_lowest_values(arr, 'T', 'V'))
