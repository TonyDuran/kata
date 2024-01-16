import string
alphabet = string.ascii_lowercase


def print_rangoli(size):
    if size > 27:
        raise ValueError("size cannot exceed 26!")
    if size <= 0:
        raise ValueError("Cannot be less than 0")
    word_list = list()
    for i in range(size):
        s = '-'.join(alphabet[i:size])
        word_list.append((s[::-1][:- 1] + s).center(4*size - 3, '-'))

    print(*word_list[::-1], sep="\n")
    print(*word_list[1:], sep="\n")


if __name__ == '__main__':
    n = int(input("Size of rangoli: "))
    print_rangoli(n)
