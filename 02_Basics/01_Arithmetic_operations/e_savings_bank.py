"""
Purpose: savings Bank
    Initial Balance 0
Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance

"""

balance = 0
 #  1500  minimum balance is added to the variable balance
balance += 1500  
# salary 3300 credited to account
balance += 3300  
#online purchase of 33.33 is debited from the account 
balance -= 33.33  
#house rent of 1500 is paid
balance -= 1500
# final balnce is shown below   
print("Final balanace is =" ,balance)