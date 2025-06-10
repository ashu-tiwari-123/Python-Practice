# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if("S".lower() in i.lower()):
        print("Greet",i)    