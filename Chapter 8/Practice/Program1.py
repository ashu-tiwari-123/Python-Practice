#  Write a program using functions to find greatest of three numbers

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

a= int(input("Enter number:"))
b= int(input("Enter number:"))
c= int(input("Enter number:"))
value = greatest(a,b,c)  
print(value)  