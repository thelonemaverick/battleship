class Player:

    def __init__(self):
        # Ask player their name

        name = self.ask_name()
        print("My name is" + name)
        # Draw empty board
        # Ask to add Ships
        # five ships place each one and redraw

        # create subclass for ships
        # Owner
        # Position
        # Horizontal or Vertical
        # function for list of coordinates

    def ask_name(self):

        return input("What is your player name?").title()

    def draw_empty_board(self):
        pass


# = Player()

# player2 = Player()

full_board = [(x,y) for y in range(1,11) for x in 'ABCDEFGHIJ']

print(full_board)

hits = [('A', 1), ('B', 3), ('C', 4), ('D', 1), ('E', 6), ('F', 9)]
print("  " + "  ".join([chr(c) for c in range(ord('A'), ord('A') + 10)]))
count = 0
row_count = 1
board = """1"""
for space in full_board:

    if space in hits:
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

