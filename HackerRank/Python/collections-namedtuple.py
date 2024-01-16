try:
    from raw_input import input
except ImportError:
    pass

# Test case 1
# 5
# ID         MARKS      NAME       CLASS
# 1          97         Raymond    7
# 2          50         Steven     4
# 3          91         Adrian     9
# 4          72         Stewart    5
# 5          80         Peter      6

# Test case 2
# 5
# MARKS      CLASS      NAME       ID
# 92         2          Calum      1
# 82         5          Scott      2
# 94         2          Jason      3
# 55         8          Glenn      4
# 82         2          Fergus     5

# TESTCASE 01
# 78.00
# TESTCASE 02
# 81.00

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

num_students = int(input())
column_headers = list(input().split())
Scores = namedtuple('Scores',column_headers)
grades = list()
for x in range(num_students):
    grades.append(int(Scores._make(input().split()).MARKS))
print((sum(grades)/ num_students))