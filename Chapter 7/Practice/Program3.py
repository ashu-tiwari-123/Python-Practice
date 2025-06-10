# Attempt problem 1 using while loop.
# Write a program to print multiplication table of a given number using for loop

num = int(input("Enter the number: "))
i = 1
while(i<11):
    print(f"{num}X{i}={num*i}")
    i+=1