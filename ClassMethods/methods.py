# class Car:
#     wheels_number = 4
#     def __init__(self, name, color, year, is_crashed ):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self):
#         print("Car is driving")
#
# opel_car = Car('Opel Tigra', 'grey', 1999, True)
# opel_car.drive()    # Car is driving
#





# class Car:
#     wheels_number = 4
#     def __init__(self, name, color, year, is_crashed ):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self):
#         print(self.name + " is driving")
#
#
# opel_car = Car('Opel Tigra', 'grey', 1999, True)
# opel_car.drive()    # Opel Tigra is driving
# mazda_car = Car('Mazda CX7', 'black', 2014, False )
# mazda_car.drive()    # Mazda CX7 is driving



# class Car:
#     wheels_number = 4
#     def __init__(self, name, color, year, is_crashed ):
#         self.name = name
#         self.color = color
#         self.year = year
#         self.is_crashed = is_crashed
#
#     def drive(self, city):
#         print(self.name + " is driving to " + city )
#
#
# opel_car = Car('Opel Tigra', 'grey', 1999, True)
# opel_car.drive('London')    # Opel Tigra is driving to London
# mazda_car = Car('Mazda CX7', 'black', 2014, False )
# mazda_car.drive('Paris')    # Mazda CX7 is driving to Paris




class Car:
    wheels_number = 4
    def __init__(self, name, color, year, is_crashed ):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def drive(self, city):
        print(self.name + " is driving to " + city)

    def change_color(self, new_color):
        self.color = new_color


opel_car = Car('Opel Tigra', 'grey', 1999, True)
opel_car.drive('London')    # Opel Tigra is driving to London
mazda_car = Car('Mazda CX7', 'black', 2014, False )
mazda_car.drive('Paris')    # Mazda CX7 is driving to Paris

mazda_car.change_color('yellow')
print(mazda_car.color)   # yellow


# class Circle:
#     pi = 3.14
#
#     def __init__(self,  radius=1):
#         self.radius = radius
#
#     def get_area(self):
#         return self.pi * (self.radius ** 2)
#
#
#
# circle_1 = Circle()
# print(circle_1.get_area())  # 3.14
# circle_2 = Circle(3)
# print(circle_2.get_area())  # 28.26
# circle_3 = Circle(5)
# circle_area = circle_3.get_area()
# print(circle_area)           # 78.5




class Circle:
    pi = 3.14

    def __init__(self,  radius=1):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * self.pi * self.radius

circle_1 = Circle()
print(circle_1.get_area())  # 3.14
print(circle_1.get_circumference())   # 6.28
circle_2 = Circle(3)
print(circle_2.get_area())  # 28.26
print(circle_2.get_circumference())   # 18.84
circle_3 = Circle(5)
circle_area = circle_3.get_area()
print(circle_area)           # 78.5
print(circle_3.get_circumference())   # 31.400000000000002





class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, amount):
        self.balance += amount

    def withdraw(self, minus):
        self.balance -= minus


client_1 = BankAccount('id45652', 'Jonny', 'Smith', 1256)
client_2 = BankAccount('id13252', 'Elon', 'Musk')

client_1.add(45692)
print(client_1.balance)
client_1.withdraw(1258.45)
print(client_1.balance)
print(client_2.balance)
