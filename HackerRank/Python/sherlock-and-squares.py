try:
    from raw_input import input
except ImportError:
    pass


# Complete the squares function below.
def squares(a, b):
    count = 0
    idx = 1
    while (idx * idx) <= b:
        square = idx * idx
        if square >= a and square <=b:
            count +=1
        idx += 1
    return count

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)
        print(result)
