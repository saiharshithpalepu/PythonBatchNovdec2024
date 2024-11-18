"""
Importance of Indentation

"""

print("Hello1")
print("Hello2")
# print("Hello3") -->indentation error: unexpected error

#block code -> if,else,elif,for,while,def,class
#if 12>3:
#print("12 is greater") #IndentationError: expected an indented block after 'if' statement on line 11

if 12>3:
    print("12 is greater")

if 10>2:
    print("greater")
else:
    print("lesser")

if 10<20:
    print("case 1")
elif 20>10:
    print("Case 2")
else:
    print("case 3")

if 10<20:
    if 20<30:
        if 30<40:
            if 40<50:
                print("lesser")
            else:
                print("other")
        else:
            print("something")
    else:
        print("another")

for i in range(9):
    print(i)

i=0
while i < 10:
    print(i)
    i += 1

i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, "*" , j , "=", i * j)
        j +=1
    print()
    i += 1

def my_func():
    return "Hello"

class MyClass:
    def __init__(self):
        pass

# tabs vs White spaces
# PEP 8 -> code style guide
# prefer white-spaces, to tabs, four white spaces