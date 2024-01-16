try:
    from raw_input import input
except ImportError:
    pass

import itertools
def get_indexes(arr, num):
    """
        return list of index values
    """
    result = list()
    for i, x in enumerate(arr):
        if x == num:
            result.append(i)
    return result

def minimumDistances(arr):
    values = {element for element in arr if arr.count(element) > 1}
    results= list()
    while values:
        res = list(itertools.combinations(get_indexes(arr,values.pop()),2))
        while res:
            coords = res.pop()
            results.append(abs(coords[0] - coords[1]))

        # results.append(abs(x - y))

    if results:
        return min(results)
    else:
        return -1

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)
    print(result)