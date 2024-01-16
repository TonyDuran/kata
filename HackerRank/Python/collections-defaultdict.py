# Enter your code here. Read input from STDIN. Print output to STDOUT

# Example input
# 5 2
# a
# a
# b
# a
# b
# a
# b
# Example Output
# 1 2 4
# 3 5

# Explanation

# 'a' appeared  times in positions ,  and .
# 'b' appeared  times in positions  and .
# In the sample problem, if 'c' also appeared in word group , you would print .

# Note: the commented out code didn't work with half the test cases.
# Probably had to do with poor management of constraints

from collections import defaultdict
m_list = list()
d = defaultdict(list)
n, m = map(int, input().split())
for x in range(0, n):
    d[input()].append(x + 1)

for x in range(0, m):
    m_list.append(input())
    # d[key].remove(-1)

for letter in m_list:
    if letter in d:
        print(*d[letter], sep=' ')
    else:
        print(-1)

# for k, v in d.items():
#     if v[0] == -1:
#         print(-1)
#         continue

#     print(*v, sep=' ')
