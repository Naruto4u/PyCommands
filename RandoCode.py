import random

VariableNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
RandomNumber = random.choice(VariableNumbers)
UserInput = int(input("Please input a number here: "))

if UserInput == RandomNumber:
    print("User input matches the random number!")
else:
    print("User input does not match the random number. The random number was:", RandomNumber)
#Do not ask about the gambling machine I am creating, please