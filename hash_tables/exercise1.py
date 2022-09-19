#               Count in even-odd positions
# We're going to extend our counting from strings by adding a subtle twist. 
# You'll need to write a count_in_position function that receives three parameters: 
# a word/sentence, a character to find, and a modifier like even or odd. Example:

#         Example 1
#         0123456789
#         phrase = 'aXbcXdXXeX'
#         count_in_position(phrase, 'X', 'even')  # 2

def count_in_position(a_string, a_char, position_type):

    count = 0

    for index, current_char in enumerate(a_string):

        if a_char == current_char:

            if position_type == 'even' and index % 2 == 0:

                count += 1

            elif position_type == 'odd' and index % 2 != 0:

                count += 1

    return count

