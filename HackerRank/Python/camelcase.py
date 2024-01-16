try:
    from raw_input import input
except ImportError:
    pass


import re

def camelcase(s):
    return (len(re.findall('[A-Z][^A-Z]*',s)) + 1)

if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    print(result)