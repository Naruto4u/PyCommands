my_list = [int(n) for n in input("Input a list of numbers").split()]
#User created Integer list

for x in my_list:
	missing = x + 1 #Variable for each Integer term in the user list,
	if missing not in my_list: #If x+1 is not in the the user's list
		print(missing) #print it



