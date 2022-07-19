import time
import random
import csv

# запис даних в csv файл
#
# with open('quiz_remastered.csv', 'w', newline='') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['Questions', 'Reply'])
#     csv_writer.writerow(['For Unix, the epoch is January 1, 1970, 00:00:00 (UTC)', 'T'])
#     csv_writer.writerow(['E.g. on most Unix systems, the clock “ticks” only 50 or 1000 times a second.', 'F'])
#     csv_writer.writerow(['To find out what the epoch is on a given platform, look at gmtime(0).', 'T'])
#     csv_writer.writerow(['time.altzone, Nonzero if a DST timezone is defined ?', 'F'])
#     csv_writer.writerow(['UTC is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part\
# of the year.', 'F'])

# Зчитування даних з csv файлу i поміщення їх в список
with open('quiz_remastered.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    list_of_questions = list(csv_reader)

# Перемішування запитань у списку в рандомному порядку
random.shuffle(list_of_questions)

# Логіка
while True:
    time.sleep(0.3)
    first_input_user = input('To start the game, press the "s" key.'
                             '\nTo end the game, press the "q" key: ').upper()
    if len(first_input_user) == 1:
        total_score = 0
        start_time = time.monotonic()
        if first_input_user == 'S':
            for x in list_of_questions:
                print('True or False: ' + x[0])
                print('__________________________________________________________')
                user_input = input('Please enter T or F if it is false: '
                                   '\nTo end the game, press the "q" key:').upper()
                print('__________________________________________________________')
                tuple_list = ('T', 'F', 'Q', 'R', '')
                if user_input == x[1]:
                    total_score += 1
                    print('Excellent!')
                elif user_input == 'Q':
                    print('__________________________________________________________')
                    print('Good bye!')
                    print('__________________________________________________________')
                    time.sleep(1)
                    break
                elif len(user_input) != 1 or user_input not in tuple_list:
                    print('Please enter the correct data!\n'
                          'Please enter only one character')
                    print('________________________________________________________________')
                    time.sleep(1.7)
                    pass
                else:
                    print('Not correct :( Maybe you will be lucky next time!')
                    print('________________________________________________________________')
        elif first_input_user == 'Q':
            print('Good bye!')
            quit()
        else:
            continue
        end_time = time.monotonic()
        print(f'Congratulations! You total score is: {total_score}, total time is {end_time - start_time} second.')
        print('______________________________________________________________________________')

    else:
        continue