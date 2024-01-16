try:
    from raw_input import input
except ImportError:
    pass



def permutationEquation(p):
    values = list()
    for i in range(1, max(p)+1):
        values.append(p.index(p.index(i)+1)+1)
    return values

if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    print(*result, sep="\n")

