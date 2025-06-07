tup1=(1,2,3,12,131,1,"ashutosh","sarthika","shashank",True,False,12.34,45.67)
print(tup1)

# Tuple Methods
# 1. count() - Returns the number of occurrences of a specified element
count_of_1 = tup1.count(1)
# 2. index() - Returns the index of the first occurrence of a specified element
index_of_12 = tup1.index(12)        
# 3. len() - Returns the number of elements in the tuple
length_of_tup1 = len(tup1)
# 4. min() - Returns the smallest element in the tuple (if they are comparable)
min_value = min(tup1[:6])  # Only consider numeric elements for min
# 5. max() - Returns the largest element in the tuple (if they are comparable)
max_value = max(tup1[:6])  # Only consider numeric elements for max
# 6. sum() - Returns the sum of all numeric elements in the tuple
sum_value = sum(tup1[:6])  # Only consider numeric elements for sum
# 7. slice - Returns a portion of the tuple
sliced_tup1 = tup1[2:5]  # Returns elements from index 2 to 4
print("Count of 1:", count_of_1)
print("Index of 12:", index_of_12)
print("Length of tup1:", length_of_tup1)
print("Min value in tup1:", min_value)
print("Max value in tup1:", max_value)
print("Sum of numeric values in tup1:", sum_value)
print("Sliced tup1:", sliced_tup1)
# 8. Tuple unpacking
# a, b, c, d, e, f, g, h, i, j, k, l = tup1
# print("Unpacked values:")
# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)
# print("e:", e)
# print("f:", f)
# print("g:", g)
# print("h:", h)
# print("i:", i)
# print("j:", j)
# print("k:", k)
# print("l:", l)
# 9. Concatenation - Combining two tuples
tup2 = (100, 200, 300)
tup3 = tup1 + tup2
print("Concatenated tuple (tup1 + tup2):", tup3)
# 10. Repetition - Repeating a tuple
tup4 = tup1 * 2
print("Repeated tuple (tup1 * 2):", tup4)
# 11. Membership - Checking if an element exists in the tuple
is_ashutosh_in_tup1 = "ashutosh" in tup1
print("Is 'ashutosh' in tup1?", is_ashutosh_in_tup1)