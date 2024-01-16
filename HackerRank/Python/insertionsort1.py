try:
    from raw_input import input
except ImportError:
    pass


# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    """
    does not return anything, just prints out failed iterations
    """
    tmp_val = arr[-1]
    next_seq = n - 2
    while next_seq != -2:
        if next_seq > -1:
            if tmp_val < arr[next_seq]:
                arr[next_seq+1] = arr[next_seq]
                print(*arr, sep=" ")
                next_seq -= 1
            else:
                arr[next_seq+1] = tmp_val
                break
                next_seq -= 1
        else:
            arr[next_seq+1] = tmp_val
            next_seq -= 1
            break
    print(*arr, sep=" ")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
