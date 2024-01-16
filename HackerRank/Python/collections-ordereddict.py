try:
    from raw_input import input
except ImportError:
    pass

from collections import OrderedDict
import re

num_of_items = int(input())
food_items = OrderedDict()
for x in range(num_of_items):
    food, space, price = input().rpartition(' ')
    if food in food_items.keys():
        food_items[food] += int(price)
    else:
        food_items[food] = int(price)

for x in food_items:
    print("{} {}".format(x, food_items[x])) 
