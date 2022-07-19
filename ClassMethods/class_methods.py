class Gamer:

    active_gamers = 0

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')


gamer_1 = Gamer('hell_boy', 23, 5, 13)
gamer_2 = Gamer('harry_potter', 13, 7, 34)

print(gamer_1.get_age())                 # 23
gamer_1.get_adult_level_permission()     # You can go to adult level

print(gamer_2.get_age())                 # 13
gamer_2.get_adult_level_permission()     # You can't go to adult level

