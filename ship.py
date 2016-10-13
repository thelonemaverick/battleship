ship_info = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10
BOARD_SIZE_ALPHA = "ABCDEFGHIJ"

# loop through all the user interactions for each of the 5 ships  Ask them three questions then create the coordinates.
for ship in ship_info:

    x_coordinate = input("Which column would you like to place your "+ship[0]+". It has a length of "+str(ship[1])
                         +"? (A-J)")

    while x_coordinate[0:1:1].upper() not in BOARD_SIZE_ALPHA:

        x_coordinate = input("Which column would you like to place your "+ship[0]+"? (A-J)")

    x_coordinate = x_coordinate[0:1:1].upper()

    print(x_coordinate)

    y_coordinate = input("Which row would you like to place your "+ship[0]+"? (1-10)")

    while int(y_coordinate) not in range(1, 10):

        y_coordinate = input("Which row would you like to place your "+ship[0]+"? (1-10)")

    y_coordinate = int(y_coordinate)

    vh_coordinate = input("Place it vertically or horizontally (V/H)")

    while vh_coordinate[0:1:1].upper() not in "VH":

        vh_coordinate = input("Place it vertically or horizontally (V/H)")

    vh_coordinate = vh_coordinate[0:1:1].upper()

    if vh_coordinate == "V" and int(y_coordinate) + ship[1] < BOARD_SIZE:

        print("colums work - vertical")

    if vh_coordinate == "H" and BOARD_SIZE_ALPHA.find(x_coordinate) + ship[1] < BOARD_SIZE:

        print("rows work - horizontal" + str(BOARD_SIZE_ALPHA.find(x_coordinate)))

    coordinate = (x_coordinate[0:1:1].upper(), int(y_coordinate))

    print(coordinate)