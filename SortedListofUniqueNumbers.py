UserList = [int(x) for x in input("List please:").split()]
UserList.sort()
SecondList = []
for x in UserList:
    if x not in SecondList:
        SecondList.append(x)

print(len(SecondList))
print(SecondList)