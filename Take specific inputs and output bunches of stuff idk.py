my_list = ["James", 10, "blue", "Zoe", 8, "red", "Dan", 12, "pink", "Shana", 11, "orange", "Sebastian", 9, "yellow", "Cynthia", 13, "green"]

user_input = input('Request name, age, or favorite color')

if user_input == "name":
    print(my_list[0:16:3])
elif user_input == "age":
    print(my_list[1:17:3])
elif user_input == "favorite color" or "fav color" or "fav" or "color":
    print(my_list[2:18:3])
else:
    print('Invalid Input')
