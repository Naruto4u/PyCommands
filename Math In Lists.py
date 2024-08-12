my_list = [int(n) for n in input().split()]
Math = 1 #For addition, set to 0, multiplication, 1, division, probably 1, subtraction, lord knows what
for x in my_list:
    Math *= x #change the sign to whatever property to use, might get a better system when smarter
print(Math)
