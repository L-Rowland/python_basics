# Python Basics

# Print function
print("hello world!")

# Variables

# String
name = "Lucas"
print(name)

# Integer (Whole number)
age = 18
print(age)

# Float (Decimal number)
height = 175.25
print(height)

# Boolean (True/False)
employed = False
print(employed)

# List
vegetables = ["carrot", "lettuce", "cabbage"] # Index starts at 0
print(vegetables)

# Dictionary
person = {"name": "Lucas", "age": "18", "height": "175.25", "employed": "false"}
print(person)

# Array (List)
integers = [4, 21, -363, 6745]
print(integers)

float = [2.0, -46.6, 213.652, 893.675]
print(float)

# Mathematics (Addition = "+" Subtraction = "-" Multiplication = "*" Division = "/")
num1 = 6
num2 = 3

print(num1+num2)
print(num1*num2)
print(num1/num2)

# Key value pairs (Key = "name". Value = "Lucas".)
print(person["name"])
print(person["age"])
print(person["height"])
print(person["employed"])

# User Input
number1 = input("Enter 1st number:")
print(number1)

print("The number you entered was =", number1) # User will see what was inputted

# Conditionals (Restrictions/Rules)

age = int(input("Enter your age:"))
# If age less than 13 print you are a kid
# If age 13-17 print you are a teenager
# If age 18-60 print you are an adult
# Else print you are a senior citizen

if age < 13:
    print("You are a kid")
elif age >= 13 and age <= 17:
    print("You are a teenager")
else:
    print("You are an adult")

# For Loop (Finite limit)
for i in range(1, 10): 
    print(i)

for i in range(1, 16): # 1, 15 would only produce 14 values, so must add 1 more
    print("Lucas")

# While Loop (Will repeat until condition met)
boolean = input("Enter T/F:")

while boolean == "T":
    print("you entered true")
    boolean = input("input T/F:")
else:
    print("you entered false")

boolean = input("Are you Lucas? Enter yes/no:")

while boolean == "no":
    print("I am not Lucas")
    boolean = input("Enter yes/no:")
else:
    print("I am Lucas")



# Python Functions
def add(num1, num2):
    return num1 + num2

print(add(5, 7))
print(add(20, 6))
print(add(615, 728))


def str(name):
    print(name)
str("Lucas")


# Lists and Loops
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])

list_length = len(fruits)
print("Length of fruits array is = ", list_length)

int1 = [1, 2, 3]
print(int1)
print(int1[2])

int2 = [6, 12, 18]
print(int2)
print(int2[1])

int3 = [-4, -8, -12]
print(int3)
print(int3[0])

int4 = [222, 555, 888]
print(int4)
print(int4[1])

int5 = [1000, 1000000, 1000000000]
print(int5)
print(int5[2])


for i in fruits:
    print("fruit = ", i)

for i in int3:
    print("number = ", i)

for i in int4:
    print("number = ", i)


# Dictionaries
me = {"name": "Lucas", "age": 18, "employed": False, "friends": ["Ryan", "Harvey", "Josh", "George", "Blessing"]} # Can insert list within dictionary
print(me)
print(me["name"])
print(me["age"])
print(me["employed"])

print(me["friends"][3])
