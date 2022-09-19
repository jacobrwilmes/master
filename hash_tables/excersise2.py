#                               First Half
# The function first_half returns the "first" half of a string (pretty obvious, right?). 
# So, if you invoke first_half('abcdef') you should get 'abc' as a result. 
# But what happens if the string has an odd number of characters like the following example? 
# first_half('abcXdef') (7 characters). 
# In that case, first_half should include the character in the middle; 
# the result should be: abcX.

#For this assignment you'll have to check the length of the string and handle the even/odd cases.

#Make sure you return your result!

def first_half(a_string):

    total_length = len(a_string)

    half_length = int(total_length / 2)
    
    if total_length % 2 == 0:

        return a_string[:half_length]

    else:

        return a_string[:half_length + 1]










    

    