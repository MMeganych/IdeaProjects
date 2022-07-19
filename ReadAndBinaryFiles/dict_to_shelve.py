import shelve

university = shelve.open('university_file')
#
# university['schedules'] = {
#         'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English language', 'Java'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Python'],
#         'friday_schedule': ['Running', 'Math', 'System programming', 'Python']
#     }             # тут при конвертації, кому не потрібно ставити. Тому що наш словник буде трактуватись як tuple
# university['tutors'] = {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }

print(university['schedules']['wednesday_schedule'])     # ['Physics', 'English language', 'Java']
print(university['tutors']['Math'])                      # ['Jack White', 'Jim Black']

university.close()

# university = {
#     'schedules': {
#         'monday_schedule': ['Math', 'English language', 'System programming', 'Python'],
#         'tuesday_schedule': ['English language', 'HTML', 'Python', 'Football'],
#         'wednesday_schedule': ['Physics', 'English language', 'Java'],
#         'thursday_schedule': ['Math', 'Chemistry', 'Python'],
#         'friday_schedule': ['Running', 'Math', 'System programming', 'Python']
#     },
#
#     'tutors': {
#         'Math': ['Jack White', 'Jim Black'],
#         'Python': ['YouRa Allakhverdov', 'Jane Smith']
#     }
# }
#
# print(university['schedules']['wednesday_schedule'])     # ['Physics', 'English language', 'Java']
# print(university['tutors']['Math'])                      # ['Jack White', 'Jim Black']

