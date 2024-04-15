from random import randint

def play(x):
  y = randint(1, 3) # 1 = rock, 2 = paper, 3 = scissors
  if x == "r":
    if y == 1:
      print("Tie!\n")
    elif y == 2:
      print("You lose!\n")
    else:
      print("You win!\n")
  elif x == "p":
    if y == 1:
      print("You win!\n")
    elif y == 2:
      print("Tie!\n")
    else:
      print("You lose!\n")
  else:
    if y == 1:
      print("You lose!\n")
    elif y == 2:
      print("You win!\n")
    else:
      print("Tie!\n")

print("Rock Paper Scissors\n")
while True:
  choice = input("Type \'r\' for rock, \'p\' for paper, \'s\' for scissors: ").lower()
  if choice == "r" or choice == "p" or choice == "s":
    play(choice)
  else:
    print("Invalid option, try again.\n")
    