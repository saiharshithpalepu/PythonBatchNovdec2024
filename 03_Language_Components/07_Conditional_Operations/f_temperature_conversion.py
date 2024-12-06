#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

value = str(input("enter the value you want to convert:"))

if value[-1].lower()=="c":
    result=celsius_to_fahrenheit(int(value[0:-1].strip()))
    print(f"the value of {value} is {result} F")
elif value[-1].lower()=="f":
    result=fahrenheit_to_celsius(int(value[0:-1].strip()))
    print(f"the value of {value} is {result} C")
else:
    print("enter valid temperature value")



