from collections import Counter
# example input
# 5 #number of shoes
# 5 3 4 2 5 #size of shoes
# 2 #number of customers
# 5 22 #size and price willing to pay (goes # of customers there are)
# 7 60 #2nd customer
num_shoes = int(input())
shoes = Counter(map(int, input().split()))
num_customer = int(input())
income = 0
for x in range(num_customer):
    size, price = map(int,input().split())
    if size in shoes.keys():
        if shoes[size] > 0:
            income += price
            shoes[size] -= 1

print(income)