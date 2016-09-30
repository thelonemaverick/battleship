ship_info = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]
# loop through all the user interactions for each of the 5 ships  Ask them three questions then create the coordinates.
for ship in ship_info:
    x_coordinate = input("Which column would you like to place your "+ship[0]+". It has a length of "+str(ship[1])+"? (A-J)")
    while x_coordinate[0:1:1].upper() not in 'ABCDEFGHIJ':
        x_coordinate = input("Which column would you like to place your "+ship[0]+"? (A-J)")

    y_coordinate = input("Which row would you like to place your "+ship[0]+"? (1-10)")
    while int(y_coordinate) not in range(1, 10):
        y_coordinate = input("Which row would you like to place your "+ship[0]+"? (1-10)")

    vh_coordinate = input("Place it vertically or horizontally (v/h)")
    while vh_coordinate[0:1:1] not in "vh":
        vh_coordinate = input("Place it vertically or horizontally (v/h)")

    coordinate = (x_coordinate[0:1:1].upper(), int(y_coordinate))

    print(coordinate)