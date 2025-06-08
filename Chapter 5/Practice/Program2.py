# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
num = set()
print("Enter eight numbers (press Enter after each number):")
for _ in range(8):
    while True:
        try:
            number = int(input())
            num.add(number)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
print("Unique numbers entered:", num)            