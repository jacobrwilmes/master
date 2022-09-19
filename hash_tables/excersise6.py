            #                                   Format Board
#In this assignment you'll be formatting a simple Tic Tac Toe board:

#O  |  O  |  X
--------------
#X  |  X  |  O
--------------
#O  |  X  |  O

#The information of the rows of the board will be kept as strings. 
# Example (considering the board above):

#first_row = 'OOX'
#second_row = 'XXO'
#third_row = 'OXO'
#The function that you need to write is format_tic_tac_toe_board that just receives those three rows. 
# It will return the board with those rows filled in correctly from the row information.

#Example:

#first_row = 'OOX'
#second_row = 'XXO'
##third_row = 'OXO'

#board = format_tic_tac_toe_board(first_row, second_row, third_row)
"""
print(board)  # Result below:
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
Hint: String formatting (the format method) will be really important for this assignment
"""




# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    
    return BOARD_TEMPLATE.format(
        
        first_row[0], first_row[1], first_row[2],
        
        second_row[0], second_row[1], second_row[2],
        
        third_row[0], third_row[1], third_row[2]
    
    )