# Write a program to sum a list with 4 numbers.
list1=[]
for i in range(4):
    num = int(input("Enter the number:"))
    list1.append(num)
sum_of_list=sum(list1)
print("The sum of the list is:", sum_of_list)    