# Immutable
first_name = 'Jake'
print(first_name[2])

#first_name[2] = 'n'  # нічого не вийде
#print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters)
last_letter = first_name[-1:]
print(last_letter)

 # Concatenable
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

greeting = 'Hello'
greeting = greeting + ' Python!'
print(greeting)

  # Multiplication
yummy = 'Yum '
print(yummy * 3)        # (Yum Yum Yum )

print(yummy.upper())     # всі букви стають заголовками -(YUM ) \.upper()\
print(yummy.lower())     # всі букви стають малими - (yum ) \.lower()\

long_string = 'This is the long string'
print(long_string.split())  # строка розбивається по словам - ( ['This', 'is', 'the', 'long', 'string'] ) \.split()\ пробіл
print(long_string.split('s')) #  строка розбивається по словам без символу 's' - ( ['Thi', ' i', ' the long ', 'tring'] )


z = 'z'
print(z * 7)

print(z.upper())

