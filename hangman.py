from random import randint

def game(list, won, lost):
  word = list[randint(0, 4)] # randomly selects a word to be used in the match
  temp = word # temporary variable to store the word
  lives = 10
  display = ["_" for _ in range(len(word))] # list of underscores to hide word
  while True:
    print(f"Lives remaining: {lives}\n")
    print("".join(display)) # turns the list into a string and prints it
    x = input("\nGuess a letter: ").lower()
    if x in temp: # if user guessed correctly
      print("Correct!\n")
      index = temp.find(x) # finds the position of the letter in the word
      display[index] = x # replaces the underscore with the letter
      temp = temp[:index] + "_" + temp[index + 1:] # removes the letter from the variable (if there are repeated letters, the program will account for all of them)
    else:
      print("Incorrect!\n")
      lives -= 1
    if lives == 0:
      print("You lost! The word was {word}.\n")
      lost += 1
      return 0
    if "_" not in display: # user guessed all the letters
      print(f"You won, congrats! The word was {word}.\n")
      won += 1
      return 1

word_list = ["fire", "civilian", "writer", "forest", "honey"] # list of secret words
won = 0
lost = 0
while True:
  print(f"Hangman Game\n\nWon: {won}\nLost:{lost}\n")
  if game(word_list, won, lost) == 0: # runs game function and keeps track of wins and losses
    lost += 1
  else:
    won += 1
  x = input("Play again? (y/n)\n").lower()
  while x != "y" and x != "n": # makes sure user enters valid input
    print("Invalid option, try again.\n")
    x = input().lower()
  if x == "n":
    break