def greet (name):
    print("Good morning,",name)

greet("Ashu")

# function with return
def avg():
    total =0
    average =0
    num = int(input("Enter the total number: "))
    for i in range(1,num+1):
        a = int(input(f"Enter {i} number: "))
        total= total+a
    average = total /num
    return average

value = avg()
print(value)    