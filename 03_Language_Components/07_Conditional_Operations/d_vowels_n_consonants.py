#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""

char = str(input("Please enter the character:"))

if not char:
    print("you have not entered  valid character")
elif not char.isalpha():
    print("You have not entered valid alphabet")
elif char in 'aeiou':
    print("You have entered vowel")
else:
    print("you have entered consonant")
