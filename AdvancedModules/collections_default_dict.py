from collections import defaultdict

# my_dict = {1: 'a'}
# print(my_dict[1])   # a

my_dict = defaultdict()
my_dict[1] = 'a'
print(my_dict[1])   # a

s = 'Hello'
d = defaultdict(int)
for k in s:
    d[k] += 1
print(sorted(d.items()))  # [('H', 1), ('e', 1), ('l', 2), ('o', 1)]
