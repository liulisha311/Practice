#!/usr/bin/env python3
fathrenheit = 0
print("fathrenhit celsius")
while fathrenheit <= 250:
    celsius = (fathrenheit - 32) / 1.8 #轉換爲攝氏度
    print("{:5d} {:7.2f}".format(fathrenheit,celsius))
    fathrenheit = fathrenheit + 25
