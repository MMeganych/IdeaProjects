from collections import Counter

number_list = [1, 1, 1, 4, 4, 5, 77, 77, 3, 3, 3, 3, 3]
string = 'dddddddddrrrrrrrrrrttttttttttyyyyyyyiiiiii'
sentence = "Hello how are you doing ? Hello I'm fine. How do you do? Hey Hey Hey !"

print(Counter(number_list))    # Counter({3: 5, 1: 3, 4: 2, 77: 2, 5: 1})
print(Counter(string))         # Counter({'r': 10, 't': 10, 'd': 9, 'y': 7, 'i': 6})
print(Counter(sentence.split(' '))) # Counter({'Hey': 3, 'Hello': 2, 'you': 2, 'how': 1, 'are': 1, 'doing': 1, '?': 1,
# "I'm": 1, 'fine.': 1, 'How': 1, 'do': 1, 'do?'

c = Counter(sentence.split(' '))
# c.clear()   # 0 , обнулення лічильника
print(sum(c.values()))   # 17
print(list(c))   # ['Hello', 'how', 'are', 'you', 'doing', '?', "I'm", 'fine.', 'How', 'do', 'do?', 'Hey', '!']
print(set(c))    # {'?', 'you', 'do?', 'are', 'fine.', 'do', 'Hey', 'Hello', '!', "I'm", 'how', 'How', 'doing'}

print(dict(c))   # {'Hello': 2, 'how': 1, 'are': 1, 'you': 2, 'doing': 1, '?': 1, "I'm": 1, 'fine.': 1, 'How': 1,
# 'do': 1, 'do?': 1, 'Hey': 3, '!': 1}

print(c.items())  # dict_items([('Hello', 2), ('how', 1), ('are', 1), ('you', 2), ('doing', 1), ('?', 1), ("I'm", 1),
# ('fine.', 1), ('How', 1), ('do', 1), ('do?', 1), ('Hey', 3), ('!', 1)])

c = Counter(dict(c))
print(c)    # Counter({'Hey': 3, 'Hello': 2, 'you': 2, 'how': 1, 'are': 1, 'doing': 1, '?': 1, "I'm": 1, 'fine.': 1,
# 'How': 1, 'do': 1, 'do?': 1, '!': 1})

print(c.most_common(3))  # [('Hey', 3), ('Hello', 2), ('you', 2)] ,наприклад вказуємо 3 елементи які найчастіше
# зустрічаються

print(c.most_common()[:-3-1:-1])  # [('!', 1), ('do?', 1), ('do', 1)] ,наприклад вказуємо 3 елементи які найрідше
# зустрічаються



