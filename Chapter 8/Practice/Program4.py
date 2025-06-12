# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==1 or n==0):
        return 1
    return n + sum(n-1)

n = int(input("Enter number:"))
s = sum(n)
print(f"sum of {n} is {s}")