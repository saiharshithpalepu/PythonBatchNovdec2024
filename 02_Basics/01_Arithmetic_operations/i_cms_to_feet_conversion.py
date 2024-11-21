'''
    Program to convert cms to feet 

    1 feet = 30.48cms
     to convert cms to feet we need to divide given cms with the value of 30.48 then we will get the value in feet

'''



def cms_to_feet(cms):
    return cms / 30.48

value_in_cms = 100

value_in_feet = cms_to_feet(100)

print(value_in_cms,"cms in feet is", round(value_in_feet,2), " feet")

