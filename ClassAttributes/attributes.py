class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)

print(mazda_car.name)    # Mazda CX7
print(mazda_car.is_crashed)  # True
print(mazda_car.wheels_number)  # 4

bmw_car = Car(name='BMW', color='black', year=2019, is_crashed=False)

print(bmw_car.name)          # BMW
print(bmw_car.year)          # 2019
print(bmw_car.wheels_number)  # 4

number_of_wheels_of_3_cars = Car.wheels_number * 3
print(number_of_wheels_of_3_cars)  # 12


# ----------------------------------------------------------------------------------------------------
class BlogPost:

    def __init__(self, user_name, text, number_of_likes):
        self.user_name = user_name
        self.text = text
        self.number_of_likes = number_of_likes


jack_post = BlogPost(user_name='Jack', text='Welcome to Python, Jack!', number_of_likes=45)
tom_post = BlogPost(user_name='Tom', text='Welcome to Python, Tom!', number_of_likes=105)

print(jack_post.number_of_likes)      # 45

jack_post.number_of_likes = 500

print(jack_post.number_of_likes)      # 500
print(tom_post.number_of_likes)       # 105

