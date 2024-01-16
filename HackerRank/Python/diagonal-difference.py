try:
    from raw_input import input
except ImportError:
    pass

def diagonalDifference(arr):

    left_diag = 0
    right_diag = 0
    #construct left diag
    for _ in range(len(arr)):
        left_diag += arr[_][_]
    #constrcut right diag
    for _ in range(len(arr)):
        right_diag += arr[_][-(_ + 1)]
    return (abs(left_diag - right_diag))



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
