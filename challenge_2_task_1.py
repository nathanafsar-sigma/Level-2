import random

random_number = random.randint(0, 100)
total_guesses = 0
list_guesses = []
guess = int(input("Guess a number between 0 - 100: "))

def check_guess(guess):
  if guess > random_number:
    print("Your guess was too big")
  elif guess < random_number:
    print("Your guess was too small")
  return

while guess != random_number:
  if guess in list_guesses:
    print("You've already guessed this")
    guess = int(input("Try a different number: "))
  else:
    list_guesses.append(guess)
    total_guesses += 1
    check_guess(guess)
    guess = int(input("Try a different number: "))

print(f"You Won! it took you {total_guesses + 1} guesses to find the correct number")
