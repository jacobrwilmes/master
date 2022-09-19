#Saving the Largest Value

# Write a function get_largest_numbers that receives 3 dictionaries as parameters: d1, d2, and d3. Get the highest integer value for each dictionary, 
# and return a new dictionary showing the results of each. If there is a non-integer as a value, ignore it. If none of the values are integers, set that result value to None. 
# Your keys in your result dictionary will be the name of each dictionary parameter (hardcoded to "d1", "d2", and "d3").

#Example:

# Add all the values with the key 'a' together, and you get the sum 22.

# d1 = { 
#    'a': 30,          max_value = max(ages.values())
 #   'c': 5            return(max_value)
# }
#                      max_key = max(ages, key=ages.get)
# d2 = {           return max_key
#    'a': 7,
#    'b': 'hi',
#    'c': 90
# }

# d3 = {
#    'a': 'aloha',
#    'b': 'howdy',
#    'c': 'hello'
# }

# result = {                         
#    'd1': 30,
#    'd2': 90,
#    'd3': None
# }

def get_largest_numbers(d1, d2, d3):
    result = {
        "d1": None,
        "d2": None,
        "d3": None
    }

    for key, value in d1.items():
        if type(value) is int and (result["d1"] is None or result["d1"] < value):
            result["d1"] = value

    for key, value in d2.items():
        if type(value) is int and (result["d2"] is None or result["d2"] < value):
            result["d2"] = value

    for key, value in d3.items():
        if type(value) is int and (result["d3"] is None or result["d3"] < value):
            result["d3"] = value
    return result
            
           

             




            