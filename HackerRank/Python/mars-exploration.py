try:
    from raw_input import input
except ImportError:
    pass


from collections import Counter
#!/bin/python3
def marsExploration(s):
    n = len(s)
    error = 0;
    sos = "SOS"
    for i in range(n):
        if(s[i] != sos[i%3]):
            error += 1
    return(error);

if __name__ == '__main__':

    s = str(input())

    result = marsExploration(s)
    print(result)
