# # Special (magic) methods __method_name__
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#     # Викликається за str(object)допомогою вбудованих функцій format()і print()для обчислення
#     # "неформального" або добре друкованого рядкового представлення об'єкта. Повернене значення має бути рядковим об'єктом.
#
#     def __len__(self):
#         return self.age
#     #Покликаний реалізувати вбудовану функцію len(). Повинно повертати довжину об'єкта, ціле число >=0.
#     # Крім того, об'єкт, який не визначає __bool__()метод і __len__()метод якого повертає нуль,
#     # вважається хибним у булевому контексті.
#
#     def __del__(self):
#         print('Person object with name ' + self.first_name + ' is deleted from memory')
#     #Викликається, коли екземпляр збирається знищити. Це також називають фіналізатором
#     # або (неналежним чином) деструктором. Якщо базовий клас має __del__()метод,
#     # метод похідного класу __del__(), якщо такий є, повинен явно викликати його,
#     # щоб забезпечити належне видалення частини екземпляра базового класу
#
#     def __add__(self, other):
#         return self.age + other.age
#
#
# jack = Person('Jack', 'White', 45)
# jane = Person('Jane', 'Eyre', 23)
# print(jack + jane)   # 68
# print(jack)          # Jack White
# print(len(jack))     # 45
# del (jack)           # Person object with name Jack is deleted from memory
#
# x = 5 + 5
# y = '5' + '5'
# print(x, y)                      # 10, 55
# print(type(x), type(y))          # <class 'int'> <class 'str'>
#
#
# x = 5
# y = 3
#
# a = '5'
# b = '3'
#
# print(x + y)      # 8
# print(a + b)      # 53
# print(x.__add__(y))      # 8
# print(a.__add__(b))      # 53
#

class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return 'Chain with ' + self.number_of_items + ' items'

    def __len__(self):
        return int(self.number_of_items)


object_for_class = Chain('104')
chain_2 = Chain('45')
print(object_for_class)
print(len(object_for_class))

print(chain_2)
print(len(chain_2))