# Positions
# Write a function positions that receives a string and 3 words, 
# and returns the first position of each one of them in the original string. 
# Example:

# Positions:
#           0                         26      34
# phrase = "Python is good. Python is Wise. I like Python"
# positions(phrase, 'Python', 'Wise', 'like')  # "0,26,34"
# (Note that the position of "Python" in this case is 0, because is the first one found)
# If the word doesn't exist in the original string, it should backfill using dashes. Example:

# Positions:
#           0                         26
# phrase = "Python is good. Python is Wise. I like Python"
# positions(phrase, 'Python', 'Wise', 'Ruby')  # "0,26,-" (Ruby doesn't exist)


def positions(a_string, first_word, second_word, third_word):

    result = ''
    
    if first_word in a_string:
        result += str(a_string.index(first_word))
    
    else:
        result += '-'
        result += ','

    if second_word in a_string:
        result += str(a_string.index(second_word))
    
    else:
        result += '-'
        result += ','

    if third_word in a_string:
        result += str(a_string.index(third_word))   
    
    else:
        result += '-'

    return result

        



