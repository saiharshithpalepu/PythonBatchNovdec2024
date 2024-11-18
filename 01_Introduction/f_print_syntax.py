"""
Purpose: print() function syntax and usage

"""
name = "Almighty"  #str

print("name" , name)

# string concatenation

print("name of student is" +  name)
print("name of student is " +  name)
print()

# using separator

print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="-")
print(1, 2, 3, 4, 5, 6, sep=":")

# Note: Python is strictly typed language
print("1 + 2     =", 1 + 2) #addition
print("'1' + '2'    =", "1" + "2") #string concatenation

#1 + '2'  TypeError: unsupported operand type(s) for +: 'int' and 'str' (cannot concatenate integer and string)

# Type converters - str(), int(), float()

print("1 + int('3') =", 1 + int("3"))
print("str(1) + '2' =", str(1) + "2")
print()

print("int('123')    =", int("123"))

# print("int('1.2')   =", int('1.2'))
# print("int('two')   =", int('two'))
# ValueError: invalid literal for int() with base 10: '1.2'