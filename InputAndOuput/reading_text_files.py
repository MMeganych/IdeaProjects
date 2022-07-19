# # Input
# x = input('Input something ')
#
# # Output
# print('Output something ' + x)

# lorem_ipsum_text = open('C:\\Users\\Volodymyr\\Desktop\\sample.txt')
# for line in lorem_ipsum_text:
#     print(line, end='')
# lorem_ipsum_text.close()
# When I find myself in times of trouble, Mother Mary comes to me
# Speaking words of wisdom, let it be
# And in my hour of darkness she is standing right in front of me
# Speaking words of wisdom, let it be
# Let it be, let it be, let it be, let it be
# Whisper words of wisdom, let it be
# And when the broken-hearted people living in the world agree
# There will be an answer, let it be
# For though they may be parted, there is still a chance that they will see
# There will be an answer, let it be
# Let it be, let it be, let it be, let it be
# Yeah, there will be an answer, let it be
# Let it be, let it be, let it be, let it be
# Whisper words of wisdom, let it be
# Let it be, let it be, let it be, yeah, let it be
# Whisper words of wisdom, let it be
# And when the night is cloudy there is still a light that shines on me
# Shine until tomorrow, let it be
# I wake up to the sound of music, Mother Mary comes to me
# Speaking words of wisdom, let it be
# Let it be, let it be, let it be, yeah, let it be
# There will be an answer, let it be
# Let it be, let it be, let it be, yeah, let it be
# There will be an answer, let it be
# Let it be, let it be, let it be, yeah, let it be
# Whisper words of wisdom, let it be

lorem_ipsum_text = open('C:\\Users\\Volodymyr\\Desktop\\sample.txt')
for line in lorem_ipsum_text:
    if 'mary' in line.lower():
        print(line, end='')
lorem_ipsum_text.close()
# When I find myself in times of trouble, Mother Mary comes to me
# I wake up to the sound of music, Mother Mary comes to me

# тут текстовий файл закриється автоматично
with open('C:\\Users\\Volodymyr\\Desktop\\sample.txt') as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        if 'mary' in line.lower():
            print(line, end='')

with open('C:\\Users\\Volodymyr\\Desktop\\sample.txt') as lorem_ipsum_text:
    line = lorem_ipsum_text.readline()
    print(line)  # получаємо тільки першу строку тексту # When I find myself in times of trouble, Mother Mary comes to me

with open('C:\\Users\\Volodymyr\\Desktop\\sample.txt') as lorem_ipsum_text:
    line = lorem_ipsum_text.readline()
    while line:
        print(line, end='')
        line = lorem_ipsum_text.readline()   # получаємо весь текст построково за допомогою циклу while,
        #  закінчуюмо цикл строкою line = lorem_ipsum_text.readline()

with open('C:\\Users\\Volodymyr\\Desktop\\sample.txt') as lorem_ipsum_text:
    lines = lorem_ipsum_text.readlines()
print(lines)  # текст буде у форматі списку

for line in lines:
    print(line, end='')    # получаємо знову весь текст построково

for line in lines[::-1]:
    print(line, end='')    # получаємо всі строки в зворотньому порядку


with open('C:\\Users\\Volodymyr\\Desktop\\sample.txt') as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)                # получаємо весь текст як одну велику строку

