#!/usr/bin/env python3
Fahrenheit = 0
print("Fahrenheit Celsius")
while Fahrenheit <= 250:
    Celsius = (Fahrenheit - 32) / 1.8
    print("{:5d}{:7.2f}".format(Fahrenheit,Celsius))
    Fahrenheit = Fahrenheit + 25
