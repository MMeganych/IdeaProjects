import time

print(time.gmtime(0))  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3,
# tm_yday=1, tm_isdst=0

print(time.gmtime())   # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=11, tm_hour=10, tm_min=42, tm_sec=2,
# tm_wday=1, tm_yday=11, tm_isdst=0) , теперішній час

print(time.localtime())  # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=11, tm_hour=11, tm_min=54, tm_sec=21,
# tm_wday=1, tm_yday=11, tm_isdst=0) , місцевий час

print(time.time())   # 1641898197.3105137 , к-сть секунд що пройшли з моменту початку епохи (1 січня 1970 року)

epoch_start_time = time.gmtime(0)

print('Year:', epoch_start_time[0])    # Year: 1970
print('Month:', epoch_start_time[1])   # Month: 1
print('Day:', epoch_start_time[2])     # Day: 1

print('Year:', epoch_start_time.tm_year)   # Year: 1970
print('Month:', epoch_start_time.tm_mon)   # Month: 1
print('Day:', epoch_start_time.tm_mday)    # Day: 1

# -----------------------------------------------------------------------------------------------------
print(time.ctime(time.time()))   # Local time # Mon Jan 17 08:22:39 2022
print(time.ctime(11111111111))   # Sun Feb  5 20:45:11 2322

print('Text before delay')
time.sleep(3.2)
print('Text after 3.2 seconds')

local_time = time.localtime(time.time())
print(local_time)  # time.struct_time(tm_year=2022, tm_mon=1, tm_mday=17, tm_hour=8, tm_min=33, tm_sec=42, tm_wday=0,
# tm_yday=17, tm_isdst=0)
print(time.mktime(local_time))  # 1642404822.0

print(time.asctime(local_time))  # Mon Jan 17 08:36:49 2022
print(time.strftime('%X', local_time))  # 08:39:34
print(time.strftime('%x %X', local_time))  # 01/17/22 08:40:32
print(time.strftime('%m/%d/%Y, %H:%M:%S', local_time))  # 01/17/2022, 08:44:31

time_string = '21 December, 2022'
struct_time = time.strptime(time_string, '%d %B, %Y')
print(struct_time)  # time.struct_time(tm_year=2022, tm_mon=12, tm_mday=21, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2,
# tm_yday=355, tm_isdst=-1)

# --------------------------------------------------------------------------------------------------------------------
