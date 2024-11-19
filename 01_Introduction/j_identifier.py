"""
Purpose: Identifiers in Python

    Variable:
        - Keyword --> Words which have some meaning in that language
        - Identifier --> Words which are defined by user (developers)
"""

# Loading a module, modules are libraries
import keyword

print(keyword.kwlist)


print(True) # True
# print(true) NameError: name 'true' is not defined.

my_val = "apple"
print(my_val) # identifier

# True = "Apple" # SyntaxError: cannot assign to True

# Rules
# Identifiers : User-defined variables
#   Naming convention
#       1. Keywords should not be used as identifiers
#       2. First character: a-z, A-Z, _
#       3. remaining charcters: a-z, A-Z, _, 0-9

#  -----Rule 1 ------
# True = 123         # SyntaxError: cannot assign to True
# None = 'Nothing'   # SyntaxError: cannot assign to None

# PEP 8 : Don't craete identifiers which are similar to keywords

# true = 123
# none = "Nothing"

# Instead use below
 
true_val = 123
none_res = "nothing"

# ------Rule 2 & 3-----
name = "apple"
my_name_is = "Harshi"
num_02_is = 123

# PEP 8 recommends to used Capitals for constants
PI = 3.1416
DOZEN = 12

# OOP --> name mangling
# variable   -> Public Variable
# _variable  -> Protected Variable
# __variable -> Private Variable

# __variable__  -> Built-in function
# Ex : __file__, __name__ , __doc__, __init__, __dict__

print("__name__ =", __name__)  # __main__
print("__file__=", __file__)

# __name__ = __main__
# __file__= /workspaces/PythonbatchNovDec2024/01_Introduction/j_identifiers.py