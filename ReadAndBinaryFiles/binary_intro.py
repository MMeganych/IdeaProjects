print(pow(10, 2))   # 100
print(pow(10, 3))   # 1000
print(pow(10, 0))   # 1 -  любе число в степені 0, дає 1
print(pow(10, 1))   # 10 -  любе число в степені 1, дає перше основне число

# pow(10, 3) pow(10, 2)  pow(10, 1)  pow(10, 0)

x = 127
print(1 * pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))  # 127

y = 1035
print(1 * pow(10, 3) + 0 * pow(10, 2) + 3 * pow(10, 1) + 5 * pow(10, 0))  # 1035

# pow(2, 3) pow(2, 2)  pow(2, 1)  pow(2, 0)

x = 0b101
print(1 * pow(2, 2) + 0 * pow(2, 1) + 1 * pow(2, 0))  # 5

y = 0b0110             # щоб не було помилки добавляєм спереду "0b" - означає, що записано в двійковій системі обчислення
print(0 * pow(2, 3) + 1 * pow(2, 2) + 1 * pow(2, 1) + 0 * pow(2, 0))  # 6

z = 0x11
print(z)
print(1 * pow(16, 1) + 1 * pow(16, 0))  # 17

z_1 = 0x2cf1
print(z_1)
print(2 * pow(16, 3) + 12 * pow(16, 2) + 15 * pow(16, 1) + 1 * pow(16, 0))  # 11505

z_2 = 0xffff
print(z_2)
print(15 * pow(16, 3) + 15 * pow(16, 2) + 15 * pow(16, 1) + 15 * pow(16, 0))   # 65535

print(format(z_2, '0>42b'))    # 000000000000000000000000001111111111111111
print(0b0000000000000000000000000001111111111111111)   # 65535