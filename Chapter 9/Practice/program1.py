# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

with open("poem.txt") as f:
    list = f.read()
    print(list)
    if("twinkle" in list):
        print("Twinkle is present")
    else:
        print("Not present")    