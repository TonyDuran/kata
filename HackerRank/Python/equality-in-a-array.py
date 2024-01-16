try:
    from raw_input import input
except ImportError:
    pass

from collections import Counter
def get_mode(xs):
    arr_count = Counter(xs)
    dict_mode = dict(arr_count)
    mode = [k for k, v in dict_mode.items() if v == max(dict_mode.values())]
    return mode[0]
    # return max(arr_count.values())

# import numpy as np
# def get_mode(xs):
#     values, counts = np.unique(xs, return_counts=True)
#     max_count_index = np.argmax(counts) #return the index with max value counts
#     return values[max_count_index]


# Complete the equalizeArray function below.
def equalizeArray(arr):
    max_val = get_mode(arr)
    return len(arr) - arr.count(max_val)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)

    # print(get_mode([1,7,2,5,3,3,8,3,2]))