# Write a python program using function to convert Celsius to Fahrenheit.

def convert_celsius_to_fhrenheit(celsius):
    return (celsius*(9/5)+32)

c=int(input("Enter celsius degree:"))
f= convert_celsius_to_fhrenheit(c)
print(f)