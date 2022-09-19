#####
#Tuple Count
#Complete the function tuple_count so that it receives a_tuple and returns a dictionary 
# with a key of each item in the tuple and a value of the count of how many occurrences it has.

#tuple_count(('a', 'b', 'a', 'b', 'b', 'c', 'd')) ==
#  {
  #  'b': 3,
   # 'd': 1,
   # 'a': 2,
  #  'c': 1
  #  }



for item in a_tuple:

    result_dict = {}
    
        if item not in result_dict.keys():

            result_dict[item] = 0

        result_dict[item] += 1

    return result_dict

    