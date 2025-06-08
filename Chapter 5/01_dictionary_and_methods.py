dict1 = {
    "Ashu":100,
    "Sarthika":100,
    "shashank":98,
    70:"Remaining students",
}

# print(dict1)

# Methods of dictionary
# print(dict1.items())  # Returns a view object that displays a list of a dictionary's key-value tuple pairs
# print(dict1.keys())   # Returns a view object that displays a list of all the keys in the dictionary
# print(dict1.values()) # Returns a view object that displays a list of all the values in the dictionary
# print(dict1.get("Ashu"))  # Returns the value for the specified key if it exists, otherwise returns None
# print(dict1["Ashu"]) # difference between get and direct access
# print(dict1["Ashu1"])  # Raises KeyError if the key does not exist  
# print(dict1.get("Ashu1", "Not Found"))  # Returns the value for the specified key if it exists, otherwise returns "Not Found"
# print(dict1.get("Ashu", "Not Found"))  # Returns the value for the specified key if it exists, otherwise returns "Not Found"
# print(dict1.pop("Ashu"))  # Removes the specified key and returns its value
# print(dict1.popitem())  # Removes and returns the last inserted key-value pair as a tuple
# dict1.clear()  # Removes all items from the dictionary

