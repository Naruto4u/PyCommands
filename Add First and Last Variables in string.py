my_list = [int(x) for x in input("6 #'s plz").split()]

for x in my_list:
    FirstVariables = my_list[0] + my_list[1]    
    LastVariables = my_list[-1] + my_list[-2]
Total = LastVariables + FirstVariables

print(Total)
