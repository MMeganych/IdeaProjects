#import random
# x = random.randint(1, 10)
# print(x)

from random import randint
x = randint(1, 10)
print(x)

from random import shuffle
my_list = [1, 2, 3]
shuffle(my_list)
print(my_list )

from random import shuffle as shuffle_my_list    # імпортуєм shuffle під своїм ім"ям shuffle_my_list
my_list = [1, 2, 3]
shuffle_my_list(my_list)
print(my_list )

import math
k = math.isqrt(123456789)
print(k)

f = math.factorial(987)
print(f)

s = math.pow(876, 54)
print(s)