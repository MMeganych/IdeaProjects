import shelve

# monday_schedule = ['Math', 'English language', 'System programming', 'Python']
# tuesday_schedule = ['English language', 'HTML', 'Python', 'Football']
# wednesday_schedule = ['Physics', 'English language', 'Java']
# thursday_schedule = ['Math', 'Chemistry', 'Python']
# friday_schedule = ['Running', 'Math', 'System programming', 'Python']

with shelve.open('schedules', writeback=True) as schedules:
    # schedules['monday_schedule'] = monday_schedule
    # schedules['tuesday_schedule'] = tuesday_schedule
    # schedules['wednesday_schedule'] = wednesday_schedule
    # schedules['thursday_schedule'] = thursday_schedule
    # schedules['friday_schedule'] = friday_schedule

   # temp_list = schedules['thursday_schedule']              # Таким дивним способом/
   # temp_list.append('Swimming')                            # /добавляємо/
   # schedules['thursday_schedule'] = temp_list              # /'Swimming' в список бази даних

    schedules['thursday_schedule'].append('Tennis')   # ще один спосіб добавлення, але на початку
    # треба записати так :  with shelve.open('schedules', writeback=True) as schedules:



    for key in schedules:
        print(key, schedules[key])
# monday_schedule ['Math', 'English language', 'System programming', 'Python']
# tuesday_schedule ['English language', 'HTML', 'Python', 'Football']
# wednesday_schedule ['Physics', 'English language', 'Java']
# thursday_schedule ['Math', 'Chemistry', 'Python']
# friday_schedule ['Running', 'Math', 'System programming', 'Python']






