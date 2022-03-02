import random

# This is how a normal print statement is done
print("Welcome to the DMV!")

user_number = random.randint(0,200)

# By typing f infront of the first "", we tell it to format anything in {} as variables, replacing them with the variable values
print(f"Your number is {user_number}, please wait until your number is called")

# the range method returns an array with the provided range.
for num in range(1,200):

    current_number = (user_number + num) % 200

    print(f"Now serving number {current_number}")

print(f"Now serving number {user_number}, please step up")

print("You haven't responded to our numerous attempts to contact you regarding your car's warranty that is well outstanding at this point!  If you don't contact us soon we're going to key your car and not being under warranty you'll have to pay gobs of money to fix!  Have a nice day. :|")
