# Sum of Dict Values
# Write a function sum_of_dict_values that receives 3 dictionaries as parameters:
# d1, d2, and d3. Get the sum of the values for each matching key 3 dictionaries, and 
# return a new dictionary showing the results of each. If there is a non-integer as a value, 
# set the value to None for that key.

# Example:

# Add all the values with the key 'a' together, and you get the sum 22.

d1 = {'a': 10,
      'b': 30,
      'c': 5}

d2 = {'a': 7,
      'b': 22,
      'c': 90}

d3 = {'a': 5,
      'b': 1,
      'c': 'hello'}

#result == {
#   'a': 22,
#  'b': 53,
#  'c': None  # d3 has an invalid value, can't be handled }

# sum_of_dict_values(d1, d2, d3) == result

def sum_of_dict_values(d1, d2, d3):
    
# pull vals from dicts and make unique vars to sum later
    
dic1 = {'a': 10,
      'b': 30,
      'c': 5}
dic2 = {'a': 7,
      'b': 22,
      'c': 90}
dic3 = {'a': 5,
      'b': 1,
      'c': 'hello'}



def sum_of_dict_values(d1, d2, d3):

    list_of_dic = [d1,d2,d3]

    return_dic = {}

    for d in list_of_dic: 

        for key in d: 
            
            return_dic.setdefault(key,0)

            if type(d[key]) == int:
                return_dic[key] += d[key]
            
            else: 
                return_dic[key] = None 
            
    return return_dic


print(sum_of_dict_values(dic1, dic2, dic3))







    

    