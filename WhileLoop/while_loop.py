x = 5
while x > 1:
    print(x)
    x -= 1   # x = x - 1 - to came
# 5
# 4
# 3
# 2

while x < 10:
    print(x)
    x += 1  # x = x + 1 - to came
# 5
# 6
# 7
# 8
# 9

while x < 10:
    print(x)
    x += 1
# 5
# 7
# 9

x = 0
while x < 10:
    print(' x is less than 10')
    x += 1
else:
    print('x now is not less than 10')
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# x now is not less than 10

for x in  range(10):
     print('x is less than 10')
else:
    print('x now is not less than 10')
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# is less than 10
# x now is not less than 10

# break, continue, pass

my_list = [1, 2, 3]
#
# for item in my_list:
#     pass                 # ставить цикл на паузу, відокремлює  від іншого коду
# print('Another code')

for item in my_list:
    if item == 2:
        break
    print(item)
print('Another code')
# 1
# Another code

for item in my_list:
    if item == 2:
        continue  # перескакуэ в початок циклу
    print(item)
print('Another code')
# 1
# 3
# Another code