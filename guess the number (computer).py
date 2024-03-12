# the user comes up with a secret number and the computer has to guess it
import random
start = 1
end = 1000
i = input("Think of a number between 1 and 1000. Press enter when you're ready.")
while True:
  guess = random.randint(start, end)
  while True: # loop to check if the user's input is valid
    verify = input(f"\nIs your number... {guess}? [Y/N]\n")
    if verify.upper() != "Y" and verify.upper() != "N":
      print("Invalid option, try again.\n")
    else:
      break
  if verify.upper() == "Y":
    print("Yay, I guessed it!")
    break
  else:
    while True: # loop to check if the user's input is valid
      verify = input("\nDarn. Is it too low or too high? [L/H]\n")
      if verify.upper() != "L" and verify.upper() != "H":
        print("Invalid option, try again.\n")
      else:
        break
    if verify.upper() == "L":
      start = guess + 1
    else:
      end = guess - 1