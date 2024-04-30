import random
from art import logo

random_number = random.randint(1,101)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(random_number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

def guess():
  global attempts

  while attempts != 0:
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > random_number:
      print("Too high.")
      attempts -=1
    elif guess < random_number:
      print("Too low.")
      attempts -=1
    else:
      break
      return f"\nYou got it! The answer was {random_number}."
      
  return "\nYou've run out of guesses, you lose."

print(guess())
