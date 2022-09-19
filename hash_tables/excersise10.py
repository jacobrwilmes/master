# Censor Your Dictionary
# The government wants you to "update" some books (in our case, dictionaries) and remove 
# the words with descriptions including certain words. Write a function censor_dictionary 
# that receives an dictionary named unclean_dictionary and a string flagged_word. 
# If the flagged_word is in the description (value) of a word (key), remove the word 
# (key-value pair) from the dictionary.

#Hint: You can use pop or del to remove key-value pairs.

def censor_dictionary(unclean_dictionary, flagged_word):

    if flagged_word in unclean_dictionary:

        unclean_dictionary.pop(flagged_word)

        return unclean_dictionary
    


    