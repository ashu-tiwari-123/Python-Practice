#Arithematic operators
a=10
b=12
c=a+b
print(c) # addition

# Assignment operators
a = 10 # Assigns the value 10 to the variable a
b = 6 
b += a # Adds the value of a to b and assigns the result to b
print(b) # b is now 16
b -= a # Subtracts the value of a from b and assigns the result to b
print(b)
b*= a # Multiplies b by a and assigns the result to b
print(b)
b /= a # Divides b by a and assigns the result to b
print(b)

#  Comparison operators
print(a>b)  
print(a<b)
print(a==b)  # Checks if a is equal to b
print(a!=b) # Checks if a is not equal to b
print(a>=b) # Checks if a is greater than or equal to b
print(a<=b) # Checks if a is less than or equal to b    

# Logical operators
print(a>5 or b<6)
#three logical operators: and, or, not
print(a>5 and b<6)
print(not(a>5)) # not operator negates the result of the expression 
# Identity operators
print(a is b)  # Checks if a and b are the same object
print(a is not b)  # Checks if a and b are not the same object
# Membership operators
list1 = [1, 2, 3, 4, 5]
print(1 in list1)  # Checks if 1 is in list1
print(6 not in list1)  # Checks if 6 is not in list1