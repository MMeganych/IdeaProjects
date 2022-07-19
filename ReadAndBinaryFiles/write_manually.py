# запис двійкових файлів :
with open('test_binary', 'bw') as test_file:
    for number in range(21):
        test_file.write(bytes([number]))   # мусимо зробити конвертацію в двійковий код bytes() і передаємо у форматі списку [] для коректної роботи


# зчитання двійкових файлів :
with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)