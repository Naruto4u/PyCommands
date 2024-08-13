ListOItems = [int(x) for x in input("List of numbers").split()]

DivideList = []
#creates a blank list for the variable DivideList
for x in ListOItems:
    if x >= 5: 
        x *= .1 #multiplies x by .1
        DivideList.append(round(x, 1))
#Will round by 1 decimal place and add x to a new list

print(DivideList)
