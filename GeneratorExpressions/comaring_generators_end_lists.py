import time

print(sum([number for number in range(10)]))  # 45
print(sum(number for number in range(10)))    # 45

list_start_time = time.time()
print(sum([number for number in range(1000000)]))
list_processing_time = time.time() - list_start_time


gen_start_time = time.time()
print(sum(number for number in range(1000000)))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')         # Processing with list is 0.07815098762512207
print(f'Processing with generator is {gen_processing_time}')     # Processing with generator is 0.07814884185791016

