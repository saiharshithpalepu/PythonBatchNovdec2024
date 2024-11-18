"""
Purpose: print() function syntax and usage
    Escape Sequences
        - characters whose presence is felt, but they were not print

        \t - tab space
        \n - new line
        \b - overwrites new character

        r'' - raw string

"""

print("Python is Language")
print("Python \tis \tLanguage")  #using tab space
print("Python \nis \tLanguage")  # using new line & tab space

# To ignore the escape sequences
print()
print("Python \tis \\nLanguage")
print(r"Python \tis \nLanguage")

print("C:\my\newfolder")
print(r"C:\my\newfolder")

# print(data, sep =' ', end = '\n')

print("python")  #default end='\n'
print("language")

print("Python", end="\n")
print("language", end="\n")

print("Python" , end="___")
print("Language") # default end='\n'

print("hello", end="\t")
print("world")

print()
print("Python", "language" , 12345, end="\t") # default sep=" "
print("simple") # default end='\n'

print("Python", "language" , 12345, end="\t", sep=";")
print("simple")