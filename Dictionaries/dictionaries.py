car_prices = {'opel': 5000, 'toyota': 7000, 'bmw': 10000 } # cловник з ключами
print(car_prices)              # {'opel': 5000, 'toyota': 7000, 'bmw': 10000}
print(car_prices['toyota'])    # 7000
car_prices['mazda'] = 4000     # добавлення нового ключа 'mazda' зі значенням 4000 у словник
print(car_prices)              # {'opel': 5000, 'toyota': 7000, 'bmw': 10000, 'mazda': 4000}
car_prices['opel'] = 2000      #  змінили значення у ключа 'opel'
print(car_prices)              # {'opel': 2000, 'toyota': 7000, 'bmw': 10000, 'mazda': 4000}
del car_prices['toyota']       # видалити ключ 'toyota' і його елемент
print(car_prices)              # {'opel': 2000, 'bmw': 10000, 'mazda': 4000}
car_prices.clear()             # видалити всі елементи зі словника
print(car_prices)              # {}

person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'children': {'son': 'Michael', 'daugter': 'Pamela'}
}                             # cловник зі списком  і словником усередині

print(person['age'])          # 43
print(person['hobbies'])      # ['football', 'singing', 'photo']

hobbies = person['hobbies']
print(hobbies[2])             # photo

print(person['hobbies'][2])   # photo


children = person['children']
print(children['son'])            # Michael

print(person['children']['son'])  # Michael

person['car'] = 'Mazda'
person['hobbies'][0] = 'basketball'
print(person)    # {'first name': 'Jack', 'last name': 'Brown', 'age': 43,
                 # 'hobbies': ['basketball', 'singing', 'photo'],
                 # 'children': {'son': 'Michael', 'daugter': 'Pamela'},
                 # 'car': 'Mazda'}

print(person.keys())  #  dict_keys(['first name', 'last name', 'age', 'hobbies', 'children', 'car'])
print(person.values()) # dict_values(['Jack', 'Brown', 43, ['basketball', 'singing', 'photo'],
# {'son': 'Michael', 'daugter': 'Pamela'}, 'Mazda'])

print(person.items()) # dict_items([('first name', 'Jack'), ('last name', 'Brown'), ('age', 43),
# ('hobbies', ['basketball', 'singing', 'photo']),
# ('children', {'son': 'Michael', 'daugter': 'Pamela'}), ('car', 'Mazda')])


my_personl_computer = { 'brand': 'lenovo',
                        'model': 'ideapad s 340',
    'Specifications': {'processor': 'AMD Ryzen 5 3500U with Radeon Vega Mobile Gfx 2.10 GHz',
                       'name computer': 'DESKTOP-JSPG6HC',
                       'RAM is installed': '20,0 Gb',
                       'system type': '64-bit operating system based on x64 processor' }
}


