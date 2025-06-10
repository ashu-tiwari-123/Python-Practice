# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

maths = int(input("Enter the marks:"))
science = int(input("Enter the marks:"))
hindi = int(input("Enter the marks:"))

total = ((maths+science+hindi)*100)/300

print(total)
if(total >=40):
    if((maths and science and hindi ) >= 33):
        print("Congratulations Pass!")
    else:
        print("Failed")        
    
