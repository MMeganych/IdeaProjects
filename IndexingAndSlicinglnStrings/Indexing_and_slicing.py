greeting = "Hello Python!"
greeting_length = len(greeting)
print(len(greeting))     # вивести кількість символів в строці - (13)

      # Indexing (індексація елементів строки)
print(greeting[1])          # вивести перший символ зі строки - (e)
print(greeting[6])          # вивести шостий символ зі строки - (P)
print(greeting[-1])         # вивести перший символ з кінця строки - (!)
print(greeting[12])         # вивести останній символ в кінці строки\0-13\ - (!)
print(greeting[-4])         # вивести четвертий символ з кінця строки - (h)

         # Slicing (кусочок)
print(greeting[2:5])    # вивести фрагмент символів строки з 2-го до 5-го елемента, не включаючи 5-й елемент - (llo)
print(greeting[6:10])   # вивести фрагмент символів строки з 6-го до 10-го елемента, не включаючи 10-й елемент - (Pyth)
print(greeting[-5:-2])  # вивести фрагмент символів строки між 5-м і 2-м елементом, включно з 5-м і 2-м елементом  - (tho)
print(greeting[2:])     # вивести фрагмент символів від 2-го елемента до кінця строки,включно з 2-м елементом  - (llo Python!)
print(greeting[:5])     # вивести фрагмент символів які ідуть до 5-го елемента строки, не включаючи 5-й елемент - (Hello)
print(greeting[:])      # вивести всі символи зі строки - (Hello Python!)
print(greeting[::2])    # перескакуємо через один символ, не виводиться кожний другий символ - (HloPto!)
print(greeting[::1])    # вивести всі символи зі строки, виводиться кожна буква - (Hello Python!)
print(greeting[::3])    # виводиться кожна третя буква, починаючи з першої - (HlPh!)
print(greeting[1::3])   # перескакуємо через кожні два символи, починаючи з 1-го елементу - (eoyo)
print(greeting[::-1])   # відзеркалення (перевернення) всієї строки - (!nohtyP olleH)

greeting = "Hello Python!"
print(greeting[3])

print("Hello Python!"[3])

greeting = "Hello Python!"
print(greeting[:2])
print(greeting[:-11])
print("Hello Python!"[:2])
print("Hello Python!"[:-11])

greeting = "Hello Python!"
new_string = greeting[6] + "a" + greeting[8:10]
print(new_string)


