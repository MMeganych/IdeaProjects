from collections import namedtuple

jake = ('Jake', 'Smith', 19, 'male')
jim = ('Jim', 'Blade', 23, 'male')
jane = ('Jane', 'Morrison', 20, 'female')

print(jake[0])  # Jake
print(jim[3])   # male

# --------------------------------------------------------------------------------------------------------------

Person = namedtuple("Person", "name surname age gender")
jake = Person(name='Jake', surname='Smith', age=19, gender='male')
jim = Person(name='Jim', surname='Blade', age=23, gender='male')
jane = Person(name='Jane', surname='Morrison', age=20, gender='female')

print(jake.name)  # Jake
print(jake.surname)  # Smith
print(jane.age)  # 20

print(jane)      # Person(name='Jane', surname='Morrison', age=20, gender='female')
jane = jane._replace(surname='Blade')
print(jane)      # Person(name='Jane', surname='Blade', age=20, gender='female')

