if __name__ == '__main__':

    BOARD_WIDTH = "ABCDEFGHIJ"

    class Ship:

        def __init__(self, coordinate, orientation, length):
            self.coordinate = coordinate
            self.orientation = orientation
            self.length = length

        def set_ship(self, orientation, coordinate, ship_length):
            # h/v plus length, compensate for edges, return coordinates [('A', 2), ('B', 2), ('C', 2), ('D', 2), ('E', 2)]

            if orientation == "h":
                strposition = BOARD_WIDTH.index(coordinate[0])
                if (strposition + ship_length) > 1:
                    row_position = len(BOARD_WIDTH) - ship_length
                    row_coordinates = [(coordinate)]
                    count = 0
                    while count < ship_length:
                        row_coordinates = (BOARD_WIDTH[strposition + count], coordinate[1])
                        count = count + 1
                    print(row_coordinates)

                else:
                    row_position = strposition
                    row_coordinates = []

            elif orientation == "v":
                # count out on a column
                pass
            else:
                print("Your orientation was invalid")



        def check_other_ships(self, placed_coordinate):
            # checking for collision with other ships
            # returns a string "ship placed successfully" or "Another ship is there, try again"
            pass

    class Player:
        player_name = input("What is your player name?").title()
        full_board = [(x, y) for y in range(1, 11) for x in BOARD_WIDTH]
        hits = [('I', 1), ('J', 1), ('A', 2), ('B', 2), ('C', 2), ('D', 2), ('E', 2)]

        ship_info = [
            ("Aircraft Carrier", 5),
            ("Battleship", 4),
            ("Submarine", 3),
            ("Cruiser", 3),
            ("Patrol Boat", 2)
        ]
        def __init__(self):

            # Ask player their name
            # Ask to add Ships

            input("What is your player name?")
            c = input("Where would you like to place your ship? (A,1)")
            o = input("Place it vertically or horizontally (v/h)")

            Ship(c, o, 4)


            # five ships place each one and redraw

            self.draw_board()
            # create subclass for ships
            # Owner
            # Position
            # Horizontal or Vertical
            # function for list of coordinates

        def ask_name(self):

            return input("What is your player name?").title()

        print(full_board)

        def draw_board(self):
            print("Player -"+self.player_name)
            print("  " + "  ".join([chr(c) for c in range(ord('A'), ord('A') + 10)]))
            count = 0
            row_count = 1
            board = """1"""
            for space in self.full_board:

                if space in self.hits:
                    board += " X "
                else:
                    board += " O "
                count += 1
                if count == 10:
                    row_count += 1

                    if row_count < 11:
                        board += """
    """ + str(row_count)

                    count = 0
            print(board)

    Player()

    # player2 = Player()


