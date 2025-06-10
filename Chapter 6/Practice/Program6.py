# Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

grade = int(input("Enter your grade: "))

if(grade >90 or grade<=100):
    print("ex")
elif(grade >80 or grade<=90):
    print('A')      
elif(grade >70 or grade<=80):
    print('B')
elif(grade >60 or grade<=70):
    print('c')
elif(grade >50 or grade<=60):
    print('d')
else:
    print("F")    

