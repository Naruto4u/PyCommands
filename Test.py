#This will determine whether a user input is Even or Odd
UserInput = input("Odd or Even Number Here")
#User input, just like the terms specify
Data = int(UserInput)
#Turns the user inputted prompt into an integer
if Data % 2 == 0:
#makes an if statement, uses modulus command to find the remainder and == to see if it's 0
    print("Even")

elif Data % 2 == 1:
#checks to see if it's equal to 1
    print("Odd")
#putting words for the input won't work, it'll toss an error, 
#which can be remedied with the except command, but idk