# Write a python function to remove a given word from a list ad strip it at the same time.

def remove(list , str):
    n = []
    for i in list:
        if not(i == str):
            n.append(i.strip(word))
    print(n)
l = ["ashu","ashutosh","shashank","shruti","shashi"]
word = input("enter the word:")
remove(l,word)