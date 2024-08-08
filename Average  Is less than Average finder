IntUserInput = [int(x) for x in input("Please input numbers here").split()] #turns the input into an integer, and turns it into a list

#print(IntUserInput)
#Used for Debug purposes
NumAdded = 0
counter = 0
#Num added is to start adding the numbers, counter is for counting numbers
for x in IntUserInput:
    if x:
        counter += 1 #adds to the counter
    else: print("Please use numbers")
for x in IntUserInput:
    NumAdded = NumAdded + x
#Takes the first number, and adds the newly looped number
Average = int(NumAdded) / int(counter)
#Finds the average of both integers, converted just in case
for x in IntUserInput:
    if x > Average:
        print(x)
    else: print(str(x) + " is not greater than the average")
#Finds what number is smaller than the average, and says so
print(counter)

print(NumAdded)

print(Average)
