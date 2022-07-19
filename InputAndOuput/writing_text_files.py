# colors_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# with open('C:\\Users\\Volodymyr\\Desktop\\rainbow_colors.txt', 'w') as rainbow_colors:
#     for color in colors_list:
#         print(color, file=rainbow_colors)  # ми створили текстовий файл rainbow_colors на робочому столі комп"ютера

colors_list = []
with open('C:\\Users\\Volodymyr\\Desktop\\rainbow_colors.txt', 'r') as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color)
print(colors_list)   #['red\n', 'orange\n', 'yellow\n', 'green\n', 'blue\n', 'indigo\n', 'violet\n']
# ми відкрили текстовий файл rainbow_colors  в списку colors_list

with open('C:\\Users\\Volodymyr\\Desktop\\rainbow_colors.txt', 'r') as rainbow_colors:
    for color in rainbow_colors:
        colors_list.append(color.strip('\n'))
print(colors_list)          # ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

with open('C:\\Users\\Volodymyr\\Desktop\\rainbow_colors.txt', 'a') as rainbow_colors:
    print('dark green', file=rainbow_colors)
    print('dark blue', file=rainbow_colors)  # добавляємо новий текст в уже існуючий текстовий файл