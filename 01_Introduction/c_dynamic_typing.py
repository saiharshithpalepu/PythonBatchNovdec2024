"""
Purpose: Python is dynamic typed language.
    Programming Languages
        Classification
            1. Static typed languages
                - first declare the variable and 
                - then use them
                  int a, float b #Declaration
                  a = 10         #Initialization

            2. Dynamic typed languages
                - Create when you need, no declaration is needed
                  num = 12
                - line by line or block by block based execution

Python code -> Python Byte code -> Working as a PythonVM/PythonInterpreter ->C compiler -> Machine
So, Python is slower compared to compiler based languages
"""

num1 =10
type(num1)

print(num1)
print(type(num1))
print("num1", num1)

#values can be changed whether it is satistically typed or dynamically typed language
num1 = 20
print("num1=", num1, "type=" , type(num1))  #int

#Python is Dynamically typed language

num1 = 20.0
print("num1=", num1, "type=" , type(num1))  #float

num1 = 20.
print("num1=", num1, "type=" , type(num1))  #float

num1 = 20,
print("num1=", num1, "type=" , type(num1))  #tuple

num1 = (20,)
print("num1=", num1, "type=" , type(num1))  #tuple

num1 = -200.09
print("num1=", num1, "type=" , type(num1))  #float

num1 = -20.1j
print("num1=", num1, "type=" , type(num1))  #Complex

num1 = "20"
print("num1=", num1, "type=" , type(num1))  #string

num1 = True # Python is a case-sensitive language
#num1 = true gives name error
print("num1=", num1, "type=" , type(num1))  #Boolean

num1 = False
print("num1=", num1, "type=" , type(num1))  #Boolean

num1 = None
print("num1=", num1, "type=" , type(num1))  #None

# Note : Strings need to declared inside quotes