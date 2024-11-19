
"""
Purpose: Multiline statements in same line
    , logic separator
    ; statement completion operator

"""
print("Hello" "world") # Helloworld
print("Hello", "world") # Hello world

print("Hello", 9876) # Hello 9876
# print("Hello"  987) # SyntaxError: invalid syntax. Perhaps you forgot a comma?

# Semicolon operator
# Method 1
num1 = 100
num2 = 200
sum_of_numbers = num1 + num2
print("Sum of numbers is:" , sum_of_numbers)

# Method 2 Using ; operator
num1 = 100; num2 = 200; sum_of_numbers = num1 + num2; print("Sum of numbers is:" , sum_of_numbers)

# Python is both scripting and general purpose programming language
