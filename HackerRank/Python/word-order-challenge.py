try:
    from raw_input import input
except ImportError:
    pass

from collections import OrderedDict

num_words = int(input())
words = OrderedDict()

for _ in range(num_words):
    word = input()
    if word in words.keys():
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values(),sep=" ")