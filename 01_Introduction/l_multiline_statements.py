"""
Purpose: Working with Multi-line statements

    Python is a interpreter-based language
        - Each line excecutes separates
        - \ -> Line continuation operator or reverse division operator
        - Will join more than one line to a single statement


Brace
    ()  Paranthesis
    {}  Curly braces
    []  square braces

PEP 8

    a) Lines should be 79 characters in length or less
    b) Continuation of long expressions onto additional lines should be intended by four extra spaces
       from their normal indentation level
    
"""

sum_of_values = 12 + 98 - 8 * 5
print(sum_of_values)

sum_of_values = 12 + 98 - 8 * 5 / 2 \
    + 12 + 98 - 8 * 5 \
    + 12 + 98 - 8 * 5

print(sum_of_values)

# braces alongside line continuation operator
sum_of_values = (12 + 98 - 8 * 5 / 2 \
    + 12 + 98 - 8 * 5 \
    + 12 + 98 - 8 * 5)

print(sum_of_values)

# braces alone
# only used during mathematical operations
sum_of_values = (12 + 98 - 8 * 5 / 2 
    + 12 + 98 - 8 * 5 
    + 12 + 98 - 8 * 5)

print(sum_of_values)