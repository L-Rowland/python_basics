name = input("Enter your name ") # Name input
print("Hi", name)

secret = 9 # Secret number guessing game
guess = int(input("Please enter a number: "))
while guess != secret:
    if guess > secret:
        print("Too high. Try another number.")
    else:
        print("Too low. Try another number.")
    guess = int(input("Please enter a number: "))
print("You found the secret number!")


for i in range(1,11): # Forward counting
  print (i)

for i in range(1,11): # Backward counting
  print (i)

import time # Timer

time.sleep(2)

i = 0 # Counting with a statement
while i != 10:
  i = i + 1
  print(i)
  time.sleep(2)
