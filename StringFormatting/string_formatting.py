print(1 + 1)   # сконкатенуэться(2)
print('1'+'1')   # сконкатенуэться(11)
age = 23
#print('Jack is ' + age + ' years old.')  # не сконкатенуэться , бо конкатенувати можна тільки строки зі строками а не з типом int
print('Jack is ' + str(age) + ' years old.')  # сконкатенуэться (Jack is 23 years old.)
print('Jack is ' + str(23) + ' years old.')   # сконкатенуэться (Jack is 23 years old.)

name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age) # виведеться "My name is Jack. I'm 23 years old." В фігурних скобках індексація слів, що прописані в .format(name, age)
name_and_age = 'My name is {0}. I\'m {1} years old.'.format('Jack', 23)
print(name_and_age)   # виведеться "My name is Jack. I'm 23 years old."
name_and_age = 'My name is {}. I\'m {} years old.'.format(23,'Jack')
print(name_and_age)  # виведеться "My name is 23. I'm Jack years old." Якщо ми в фігурних скобках не вказуємо індексацію , то параметри добавляються автоматичо як вони стоять по порядку.

week_days = 'There are 7 days in a week: {}, {}, {}, {}, {}, {}, {}. '\
    .format('Monday', 'Tuesday',  'Wednesday',  'Thursday', 'Friday', 'Saturday', 'Sunday')
print(week_days)  # виведеться "There are 7 days in a week: Monday, Tuesday, Wednesday, Thursday, Friday,
                  # Saturday, Sunday."

week_days = 'There are 7 days in a week: {5}, {0}, {3}, {1}, {2}, {4}, {6}. ' \
    .format('Monday', 'Wednesday', 'Thursday', 'Tuesday', 'Friday', 'Sunday', 'Saturday')
print(week_days) # змішали дні тижня і за  упорядкували ці дні

week_days = 'There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}. ' \
    .format( mo = 'Monday', we = 'Wednesday', th = 'Thursday', tu = 'Tuesday',
             fr = 'Friday', su = 'Sunday', sa = 'Saturday')
print(week_days)  # змішали дні тижня і за допомогою ключiв упорядкували ці дні

week_days = 'There are 7 days in a week: {su}, {su}, {su}, {su}, {su}, {su}, {su}. ' \
    .format( mo = 'Monday', we = 'Wednesday', th = 'Thursday', tu = 'Tuesday',
             fr = 'Friday', su = 'Sunday', sa = 'Saturday')
print(week_days)  # виведеться "There are 7 days in a week: Sunday, Sunday, Sunday,
                 # Sunday, Sunday, Sunday, Sunday."
                  # змішали дні тижня і за допомогою ключa "su" створили всі одинакові дні


float_result = 1000 / 7
print(float_result)    # виведеться(142.85714285714286)
print('The result of division is {0}'.format(float_result))  # виведеться(142.85714285714286)
print('The result of division is {0:1.3f}'.format(float_result))  # виведеться (142.857)
# {0:1.3f} - де "0" ,означає індекс  .format(float_result))
#          - де "3f",означає к-сть цифр що виведуться після крапки тобто .857
#          - де "1" ,означає к-сть всіх цифр що виведуться (142.857) їх тут шість.
# Можемо сміло вводити там число від 1 до 6 і буде той самий результат (142.857).
# Якщо введемо число більше 6 тобто більше загальної к-сті всіх цифр що будуть виводитись {0:1.10f}  ,
# то веведуться числа з пробідом спереду (  142.857)

print('''
{} {} {}
{} {} {}
{} {} {}
'''.format(1.45778, 345.232352, 34.2344, 1234.23,
           1.45778, 345.232352, 34.2344, 1234.23, 456.43234))
# виведеться 1.45778345.23235234.2344
#            1234.231.45778345.232352
#            34.23441234.23456.43234

print('''
{0:10.2f} {1:10.2f} {2:10.2f}
{3:10.2f} {4:10.2f} {5:10.2f}
{6:10.2f} {7:10.2f} {8:10.2f}
'''.format(1.45778, 345.232352, 34.2344, 1234.23,
           1.45778, 345.232352, 34.2344, 1234.23, 456.43234))
# виведеться      1.46     345.23      34.23
#              1234.23       1.46     345.23
#                34.23    1234.23     456.43
#     Числа гарно вирівняні за правим краєм, як в таблиці


name = 'Jack'
age = 23
name_and_age = 'My name is {0}. I\'m {1} years old.'.format(name, age)
print(name_and_age)      # виведеться "My name is Jack. I'm 23 years old."

name_and_age =  f'My name is {name}. I\'m {age} years old.'
print(name_and_age)      # виведеться "My name is Jack. I'm 23 years old."
print('My name is %s. I\'m %d years old. ' % (name, age))  # виведеться "My name is Jack. I'm 23 years old."
# %s-строка, %d-число
print('My name is %s. %s %d years old.' % (name, "I\'m", age)) # виведеться "My name is Jack. I'm 23 years old."

print('''
{0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f}
{4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
'''.format(101.52682, 62.125478, 025.201468, 45.654735,
           14.566571, 325.4556, 101.456652, 857.76145))

