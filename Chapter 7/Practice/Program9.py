# Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * * 

n = int(input("Enter the number:"))

for i in range(1,n+1):
    if(i==1 or i ==n):
        print("x"*n,end="")
    else:
        print("x",end="") 
        print(" "*(n-2),end="")
        print("x",end="") 
    print("")       