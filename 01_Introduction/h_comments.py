"""
Purpose: Working with comment operator
    - Once # is encountered, complete line from that position is ignored
    - PEP 8 Guidelines recommends one white space after # operator
    - comments
        - For single line comment use #
        - For multiline comment - python doesn't support

Question: Why python dont have multi-line comment operator
Answer  : Python is an interpreter based language means each line executes separately

Python doesn't run on Machine directly, so it uses C compiler to execute the code
Python code--> Line by Line --> C code --> Assembly level language --> Machine

ctrl + / - multi-line comment/uncommet

"""

print("Python Language 1")
# print("Python Language 2")

# any operator within quotes will be treated as ordinary
print("Python #Language 3")
print("Python" , "Language" , sep="#")

print(" Python Language 5")  #
# print('python' #)  Gives syntax error because # is not enclosed in quotes

'''
Used to handle multi-line strings
or 
incase where multiple single and double quotes

'''

"""
Used for 
doc strings

"""