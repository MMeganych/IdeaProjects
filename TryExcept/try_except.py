# print('Some code')           # Some code
# print(my_variable)           # NameError: name 'my_variable' is not defined
# print('Code after error')

# ОБРОБКА ПОМИЛОК exceptions:
print('Some code')                   # Some code
try:
    print(my_variable)
except:
    print('Some error has happen')   # Some error has happen
print('Code after error')            # Code after error

# -------------------------------------------------------------------------

print('Some code')                   # Some code
try:
    print(my_variable)
except NameError:
    print('NameError has happen')    # NameError has happen
print('Code after error')            # Code after error

# ------------------------------------------------------------------------------------

print('Some code')                   # Some code
try:
    print(len(23))
    print(my_variable)
except NameError:
    print('NameError has happen')
except TypeError:
    print('TypeError has happen')    # TypeError has happen
print('Code after error')            # Code after error

# --------------------------------------------------------------------------

print('Some code')                   # Some code
try:
    print(my_variable)
    print(len(23))
except NameError:
    print('NameError has happen')   # NameError has happen
except TypeError:
    print('TypeError has happen')
print('Code after error')            # Code after error


# ------------------ НА ПРИКЛАДІ ФУНКЦІЇ -----------------------------------------------------------------
user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}

# print(user_dictionary['last_name'])  # White
# print(user_dictionary['name'])       # KeyError: 'name'

print(user_dictionary.get('last_name'))  # White
print(user_dictionary.get('name'))       # None

# ------------- створимо ф-цію схожу на .get() : ------------------------------------------------


def get_dictionary_value(dictionary, key):
    return dictionary[key]


# print(get_dictionary_value(user_dictionary, 'age'))   # 24
# print(get_dictionary_value(user_dictionary, 'a'))     # KeyError: 'a'

# --------------------------------------------------------------------------------


def get_dictionary_value_2(dictionary, key):
    '''
    if dictionary hasn't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        return None


print(get_dictionary_value_2(user_dictionary, 'age'))   # 24
print(get_dictionary_value_2(user_dictionary, 'a'))     # None