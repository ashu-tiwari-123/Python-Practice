# Write a program to find whether a given number is prime or not

num = int(input("enter the number:"))
prime = True
for i in range(2,num):
   if(num%i==0):
      prime=False
      break   
if(prime):
   print("Prime number")
else:
   print("Not a prime number")         