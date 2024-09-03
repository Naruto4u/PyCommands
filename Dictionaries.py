
# code to add inputs into a dictionary and then multiply them together with a for loop
group = {3:10,5:3,10:6,4:30}
group[int(input("key: "))] = int(input("value: "))
print(group)
test = 0
for key,value in group.items():
    test += key * value
print(test)
