try:
    from raw_input import input
except ImportError:
    pass



# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    while arr:
        print(len(arr))
        tmp = arr.pop(0)
        for x in range(len(arr)):
            arr[x] = arr[x] - tmp
        while 0 in arr: arr.remove(0)
if __name__ == '__main__':

    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    cutTheSticks(arr)