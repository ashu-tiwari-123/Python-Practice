# Write a program to find the sum of first n natural numbers using while loop

num = int(input("Enter the number:"))
total = 0

for i in range(num):
    total = i+total
print(total)    