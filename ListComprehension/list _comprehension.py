# number_dict = {(ми поміщаємо 3) number ** 2 for (для 1)  number in (в 2) number_list}

greeting = 'hello!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)    # ['h', 'e', 'l', 'l', 'o', '!']

letter_list = [letter for letter in greeting]
print(letter_list)      # ['h', 'e', 'l', 'l', 'o', '!']

number_list = [number for number in '0123456789']
print(number_list)      # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

number_list_1 = [num for num in range(0, 10)]
print(number_list_1)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number_list_2 = [num ** 2 for num in range(0, 10)]  # піднімаєм числа в квадрат
print(number_list_2)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

number_list_3 = [(num - 3) / 2 ** 2 for num in range(0, 10)]
print(number_list_3)    # [0.75, 0.5, 0.25, 0.0, -0.25, -0.5, -0.75, -1.0, -1.25, -1.5]

number_list_4 = [6, 43, -2, 11, -55, -12, 3, 345, 0]
new_list = [number for number in number_list_4 if number > 0]
print(new_list)         # [6, 43, 11, 3, 345]

new_list = [number ** 3 / 2 for number in number_list_4 if number > 0]
print(new_list)         # [108.0, 39753.5, 665.5, 13.5, 20531812.5]

new_list_1 = ['+' if number > 0 else '-' if number < 0 else 'zero' for number in number_list_4]
print(new_list_1)       # ['+', '+', '-', '+', '-', '-', '+', '+', 'zero']


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_digits = [number for number in digits if number % 2 != 0]
print(new_digits)

new_digits_1 = []
for number in digits:
    if number % 2 != 0:
        new_digits_1.append(number)
print(new_digits_1)

# With List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = [greeting[1] for greeting in greetings]
print(letter_list)

# # Without List Comprehension
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = []
for greeting in greetings:
    letter_list.append(greeting[1])
print(letter_list)