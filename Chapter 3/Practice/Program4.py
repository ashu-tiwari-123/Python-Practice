# Replace the double space from problem 3 with single spaces.
string = input("Enter a string: ")
ds =string.find("  ")
print(ds)
if ds != -1:
    string = string.replace("  "," ")
print(string)    