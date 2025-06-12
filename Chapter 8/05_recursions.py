# factorial with recursion

def factorial(n):
    if(n==0 or n==1):
        return n
    return n * factorial(n-1)

n = int(input("Enter any number:"))
a = factorial(n)
print(f"Factorial of {n} is {a}")


