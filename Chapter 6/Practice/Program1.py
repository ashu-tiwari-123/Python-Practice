# Write a program to find the greatest of four numbers entered by the user

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
num4 = int(input("Enter the fourth number:"))

if(num1>num2 and num1>num3 and num1>num4):
    print("Number 1 is greatest of all:",num1)
elif(num2>num3 and num2>num4):
    print("Number 2 is greatest of all", num2)
elif(num3>num4):
    print("Number 3 is greatest of all",num3)
else:
    print("Number 4 is greatest of all",num4)         