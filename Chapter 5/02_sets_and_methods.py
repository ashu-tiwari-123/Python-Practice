empty_set = set()
non_empty_set = {1, 2, 3}

print(empty_set)  # Output: set()
print(non_empty_set)  # Output: {1, 2, 3}


# Methods of set
# empty_set.add(4)  # Adds an element to the set
# empty_set.add(5)  # Adds another element to the set
# empty_set.remove(4)  # Removes the specified element from the set; raises KeyError if not found
# empty_set.discard(5)  # Removes the specified element from the set; does not raise an error if not found
# empty_set.clear()  # Removes all elements from the set
# empty_set.update([6, 7, 8])  # Adds multiple elements to the set
# empty_set.update({9, 10})  # Adds elements from another set to the set
# empty_set.intersection_update({6, 7, 11})  # Keeps only elements that are also in the specified set
# print(empty_set)  # Output: {6, 7}
# print(non_empty_set)  # Output: {1, 2, 3}
# empty_set.union(non_empty_set)  # Returns a new set with elements from both sets
# empty_set.difference(non_empty_set)  # Returns a new set with elements in empty_set but not in non_empty_set
# empty_set.symmetric_difference(non_empty_set)  # Returns a new set with elements in either set but not in both
# empty_set.isdisjoint(non_empty_set)  # Returns True if the sets have no elements in common
# empty_set.issubset(non_empty_set)  # Returns True if empty_set is a subset of non_empty_set
# empty_set.issuperset(non_empty_set)  # Returns True if empty_set is a superset of non_empty_set 
# empty_set.copy()  # Returns a shallow copy of the set
# empty_set.pop()  # Removes and returns an arbitrary element from the set; raises KeyError if the set is empty
# empty_set == non_empty_set  # Returns True if both sets are equal
# empty_set != non_empty_set  # Returns True if both sets are not equal
# empty_set.intersection(non_empty_set)  # Returns a new set with elements common to both sets
# print(empty_set)  # Output: {6, 7}
