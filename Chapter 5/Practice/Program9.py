# Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}
# No, you cannot change the values inside a list that is contained in a set. Sets require their elements to be immutable, and lists are mutable. If you try to add a list to a set, it will raise a TypeError. Here's an example: