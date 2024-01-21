from art import logo 
print(logo)
import random

def game():

  def no_of_tries(x):
    if x == "hard":
      return 5
    else:
      return 10
  
  
  def index(guess):
    if guess > answer:
      return 1
    elif guess < answer:
      return 2
    else:
      return 0
  
  def track(lives):
    if lives == 0:
      return True
    else:
      return False
  
  answer = random.randint(0,100)
  end_of_game = False
  difficulty = input("Choose a difficulty : Easy or Hard\n").lower()
  no_of_guesses = no_of_tries(difficulty)
  
  while( not end_of_game):
    x = int(input("Guess a number\n"))
    y = index(x)
    if y==1:
      print("Too high")
      no_of_guesses -=1 
      print(f"You have {no_of_guesses} left")
    elif y == 2:
      print("Too low")
      no_of_guesses -=1 
      print(f"You have {no_of_guesses} left")
    else:
      print(f"You win! The number was {answer}")
      end_of_game = True
  
    end_of_game = track(no_of_guesses)

game()
