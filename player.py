class Player:
    player_name = input("What is your player name?").title()
    full_board = [(x, y) for y in range(1, 11) for x in 'ABCDEFGHIJ']
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
        input("Where would you like to place your ship? (x,x)")
        input("Place it vertically or horizontally (v/h)")


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



