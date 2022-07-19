import time
import random

list_of_questions = []
list_of_questions.append(["For Unix, the epoch is January 1, 1970, 00:00:00 (UTC)", 'T'])
list_of_questions.append(["E.g. on most Unix systems, the clock “ticks” only 50 or 1000 times a second.", 'F'])
list_of_questions.append(["To find out what the epoch is on a given platform, look at gmtime(0).", 'T'])
list_of_questions.append(["time.altzone, Nonzero if a DST timezone is defined ?", 'F'])
list_of_questions.append(["UTC is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part\
 of the year.", 'F'])
random.shuffle(list_of_questions)
total_score = 0
start_time = time.monotonic()
for x in list_of_questions:
    print('True or False: ' + x[0])
    user_input = input('Please enter T or F if it is false: ').upper()
    if user_input == x[1]:
        total_score += 1
        print('Excellent!')
    else:
        print('Not correct :( Maybe you will be lucky next time!')
end_time = time.monotonic()
print(f'Congratulations! You total score is: {total_score}, total time is {end_time - start_time} second.')








