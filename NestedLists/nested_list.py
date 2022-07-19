nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
print(nested_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13]]
print(len(nested_list)) # 4 / к-сть вложених списків у списку
print(len(nested_list[1])) # 3 / к-сть елементів у другому вложеному списку
print(len(nested_list[-1])) # 4
print(nested_list[1][1])  # 5 / звернення до 2-го елемента у другому вложеному списку
print(nested_list[1][2])  # 6

 # GET number 12 :
print(nested_list[3][2]) # 12
print(nested_list[-1][2]) # 12
print(nested_list[3][-2]) # 12
print(nested_list[-1][-2]) # 12

 # print nested list
for inner_list in nested_list:
    print(inner_list)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [10, 11, 12, 13]

for inner_list in nested_list:
    for number in inner_list:
        print(number)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13

[[print(number) for number in inner_list] for inner_list in nested_list]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13








