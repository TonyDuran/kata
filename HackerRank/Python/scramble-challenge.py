#this is a working solution, but it is too slow
def scramble(s1, s2):
    arr1 = list(s1)
    arr2 = list(s2)
    value = True
    for x in range(len(arr2)):
    try:
        if not arr2:
            break
        arr1.remove(arr2[0])
        arr2.pop(0)
    except ValueError:
        value = False
    return value
# Original idea (couldn't work because it is a set and there are duplicates)
#return not bool(set(s2) - (set(s1) & set(s2)))

#this is a second working solution. Also too slow
from collections import Counter
def scramble(s1, s2):
    words = Counter(s2)
    for x in s1:
        if not words:
            break
        if words[x]:
            if words[x] > 1:
                words[x] -= 1
            else:
                words.pop(x)
    return not bool(words)