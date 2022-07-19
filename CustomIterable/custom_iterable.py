# for number in range(1, 10):
#    print(number)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

# Клас, маємо зробити його iterable:

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            self.number = self.current
            self.current += 1
            return self.number
        raise StopIteration


firs_range = MyRange(1, 10)

for number in firs_range:
    print(number)



