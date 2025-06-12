# Write a python function which converts inches to cms

def convert(n):
    return n*2.54

n = int(input("Enter the number inches:"))
ans = convert(n)
print(f"inches to cm {n} to {ans}")