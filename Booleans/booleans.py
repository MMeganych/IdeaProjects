# print(1<2)
# print(type(True))
# print(type(False))
#
# # Comparison operators
#
# print(1 == 1)
# print(1 == 2)
# print('Hello' == 'Hello')
# print('Hello' == 'hello')

print(1 != 1)     # False
print(1 != 2)     # True
print('Hello' != 'Hello')   # False
print('Hello' != 'hello')    # True

print(1 > 2)    # False
print(1 < 2)    # True
print(2 >= 2)   # True
print(3 >= 2)   # True
print(2 <= 2)   # True
print(3 <= 2)   # False

print(ord('a'))   # 97 - kod ASCII
print(ord('b'))   # 98 - kod ASCII
print('a' > 'b')  # False - (97 > 98) - kod ASCII
print('hi' > 'hello')  # True - спочатку зрівнюються перші символи в двох словах : "h" і "h",
# вони одинакові, а потім порівнюються наступні
# символи в двох словах : "і" і "е" згідно таблиці ASCII

print(ord('i'))  # 105 - kod ASCII
print(ord('e'))  # 101 - kod ASCII

x = 10
y = 23

print(x > y)    # False
print(x < y)    # True
print(x == y)   # False
print(x != y)   # True

#age = input('Input your age')
#print('Your age is' + age)  # Input your age 45
                                 #  Your age is 45
#age = int(input('Input your age'))
#print('Access is permitted : ' + str(age >= 18))  # Input your age 45
                                                  # Access is permitted : True

print('f' > 'F')
print(ord('f'))
print(ord('F'))