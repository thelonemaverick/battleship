SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'
EMPTY = 'O'
MISS = '.'
HIT = '*'
SUNK = '#'



class Board:
    def clear_screen():
        print("\033c", end="")

    def print_board_heading():
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]))

    def print_board(board):
        print_board_heading()

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1

    def game_play(self):
        while True:
            Board.clear_screen()
            Player1.turn()
            Board.clear_screen()
            Player2.turn()


class Player:
    def __init__(self):
        # Ask player their name
        # Ask to add Ships
        self.name = input("What is your player name?").title()
        Ship.build_ships(self, SHIP_INFO)

    def turn(self):
        input("{}, Select a coordinate to hit (A,1)".format(self.name))


class Ship(Player):

    def __init__(self):

        # self.ship_name = ship_name
        # self.coordinate = coordinate
        # self.orientation = orientation
        # self.ship_length = ship_length
        print("I made a ship{}".format(self.name))

    def build_ships(self, SHIP_INFO):
        for ship in SHIP_INFO:
            self.ship_name = ship[0]
            self.ship_length = ship[1]
            coordinate = input("{}, where would you like to place your {} ({})? (A,1)".format(self.name, self.ship_name, self.ship_length))
            orientation = input("Place the {} vertically or horizontally (v/h)".format(self.ship_name))
            print("You just placed a {}".format(self.ship_name + coordinate + orientation))

Board_Play = Board()
Player1 = Player()
Board.clear_screen()
Player2 = Player()
Board.clear_screen()
Board_Play.game_play()
