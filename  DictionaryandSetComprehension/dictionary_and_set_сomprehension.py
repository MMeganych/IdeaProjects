# number_dict = {(ми поміщаємо 3) number ** 2 for (для 1)  number in (в 2) number_list}

number_dict = {'first': 1, 'second': 2, 'third': 3 }
new_dict = {key: value ** 3 for key, value in number_dict.items()}  # словник повертає лише ключі,
                                                                    #щоб він повернув все, добавляємо метод .items()
print(new_dict)    # {'first': 1, 'second': 8, 'third': 27}

number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
number_dict = {number: number ** 2 for number in number_list}
print(number_dict)         # {6: 36, 43: 1849, -2: 4, 11: 121, -55: 3025, -12: 144, 3: 9, 345: 119025, 0: 0}

number_dict = {number: 'positive' if number > 0 else 'negative'
               if number < 0 else 'zero' for number in number_list}
print(number_dict)     #{6: 'positive', 43: 'positive', -2: 'negative', 11: 'positive', -55: 'negative', -12: 'negative', 3: 'positive', 345: 'positive', 0: 'zero'}

    # Set Comprehension
number_list = [6, 43, -2, 11, -55, -12, 3, 345, 0]
number_set = {number ** 2 for number in number_list}
print(number_set)   # 0, 121, 36, 4, 9, 144, 3025, 119025, 1849} - неупорядковані елементи в 2-гій степені

number_set = {number ** 2 for number in range(3, 11)}
print(number_set)   # {64, 36, 100, 9, 16, 49, 81, 25} - неупорядковані елементи в 2-гій степені від 3 до 10

letter_set = {letter for letter in 'hello'}
print(letter_set)  # {'e', 'h', 'l', 'o'}

letter_set = {letter.upper() for letter in 'hello'}
print(letter_set)  # {'E', 'O', 'H', 'L'}


