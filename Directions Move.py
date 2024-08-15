ShipSpot1 = 0
ShipSpot2 = 0
Exited = "Program exited. You left the grid at ({},{})"
Moved = "You moved {} to ({},{})"
NSEW = ["North", "South", "East", "West"]
Escaped = "You left the grid at ({},{})"
Playing = True


while Playing:
    if ShipSpot1 >= 5 or ShipSpot1 <= -5 or ShipSpot2 >= 5 or ShipSpot2 <= -5:
        print(Escaped.format(ShipSpot1,ShipSpot2))
        Playing = False
        break
    Direction = input("Input a cardinal direction - or Exit to quit").lower()
    
    if Direction == "e" or Direction == "east":
        ShipSpot1 += 1
        print(Moved.format(NSEW[2],ShipSpot1, ShipSpot2))
    
    elif Direction == "w" or Direction == "west":
        ShipSpot1 -= 1
        print(Moved.format(NSEW[3],ShipSpot1, ShipSpot2))
    
    elif Direction == "n" or Direction == "north":
        ShipSpot2 += 1
        print(Moved.format(NSEW[0],ShipSpot1, ShipSpot2))
    
    elif Direction == "s" or Direction == "south":
        ShipSpot2 -= 1
        print(Moved.format(NSEW[1],ShipSpot1, ShipSpot2))
    
    elif Direction == "exit" or Direction == "quit":
        print(Exited.format(ShipSpot1, ShipSpot2))
        Playing = False
    
    else: print("Wrong input, try again")
