# Write a program to print multiplication table of n using for loops in reversed order.

num = int(input("Enter the number: "))
n=10
for i in range(n+1):
    print(f"{num}X{n}={num*n}")
    n-=1