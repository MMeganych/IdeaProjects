import pickle

honda = (
    'civic',
    'grey',
    '2009',
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jake Green')
    )
)
# запис файлу
with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)


# вилучення
with open('honda.pickle', 'rb') as honda_retrieved:
    honda_from_file = pickle.load(honda_retrieved)

print(honda_from_file)    # ('civic', 'grey', '2009', ((1, 'James Brown'), (2, 'Jane White'), (3, 'Jake Green')))

model, color, year, owner_list = honda_from_file

print(model)               # civic
print(color)               # grey
print(year)                # 2009

for owner in owner_list:
    owner_number, owner_name = owner
    print((owner_number, owner_name))
# (1, 'James Brown')
# (2, 'Jane White')
# (3, 'Jake Green')



# Moжемо поміщати декілька обєктів в файл і вилучати також з нього декілька обєктів. Порядок вилучення повинен
# співпадати з порядком запису обєктів

honda = (
    'civic',
    'grey',
    '2009',
    (
        (1, 'James Brown'),
        (2, 'Jane White'),
        (3, 'Jake Green')
    )
)
# запис файлу
models = ['civic', 'accord', 'pilot']
owners = ['James Brown', 'Jane White',  'Jake Green']

with open('honda.pickle', 'wb') as honda_file:
    pickle.dump(honda, honda_file)
    pickle.dump(models, honda_file)
    pickle.dump(owners, honda_file)
    pickle.dump(4553535, honda_file)


# вилучення
with open('honda.pickle', 'rb') as honda_retrieved:
    honda_from_file = pickle.load(honda_retrieved)
    models = pickle.load(honda_retrieved)
    owners = pickle.load(honda_retrieved)
    a = pickle.load(honda_retrieved)

print(honda_from_file)    # ('civic', 'grey', '2009', ((1, 'James Brown'), (2, 'Jane White'), (3, 'Jake Green')))
print(models)
print(owners)
print(a)
