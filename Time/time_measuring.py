import time

# not recommended
input('Press enter to start')
start_time = time.time()
for i in range(10000000):
    x = i * i
end_time = time.time()
print(end_time - start_time)  # 1.0740795135498047

# recommended
input('Press enter to start')
start_time = time.monotonic()
for i in range(10000000):
    x = i * i
end_time = time.monotonic()
print(end_time - start_time)  # 1.014999999999418


input('Press enter to start')
start_time = time.perf_counter()
for i in range(10000000):
    x = i * i
end_time = time.perf_counter()
print(end_time - start_time)  # 0.9864888
