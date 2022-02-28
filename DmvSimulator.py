import random

# This is how a normal print statement is done
print("Welcome to the DMV!")

user_number = random.randint(0,100)

# By typing f infront of the first "", we tell it to format anything in {} as variables, replacing them with the variable values
print(f"Your number is {user_number}, please wait until your number is called")

# the range method returns an array with the provided range.
for num in range(1,100):

    current_number = (user_number + num) % 100

    print(f"Now serving number {current_number}")

print(f"Now serving number {user_number}, please step up")

print("Sorry, you do not have the proper paperwork! Please come back when you have the proper paperwork")