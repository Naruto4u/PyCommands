Tests = ["testA", "testB", "testC", "testD"]
for x in Tests:
    if x == "testA":
        print(x + " is working")
    elif x == "testC":
        print(x + " is also working")
    elif x == "testD":
        print(x + " is also, also working")
    else: print(x + "is working, it just looks like it's not")
