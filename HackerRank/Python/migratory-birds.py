try:
    from raw_input import input
except ImportError:
    pass

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    highest_type = 0
    highest_count = 0 
    for _ in range(1,6):
        count = arr.count(_)
        if count > highest_count:
            highest_type = _
            highest_count = count
    return highest_type


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)


