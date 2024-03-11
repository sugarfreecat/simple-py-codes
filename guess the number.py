import random

random_number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != random_number:
  if guess > random_number:
    guess = int(input("Oops, too high! Try again: "))
  elif guess < random_number:
    guess = int(input("Oops, too low! Try again: "))
print(f"That's correct! The number was {random_number}! Yay!")