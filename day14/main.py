import game_data 
import art
import random
import os

logo = art.logo
vs = art.vs
data = game_data.data
def return_a_person():
  """Returns a random person from the list"""
  x = random.randint(0 , len(data)-1)
  return data[x]


def compare(a , b):
  if a["follower_count"] > b["follower_count"]:
    return 1
  else:
    return 0

def game():
  end_of_game = False
  score = 0
  while not end_of_game:
    print(logo)
    a = return_a_person()
    b = return_a_person()
    print(f"Score : {score}")
    print("\nWho has more followers :\n")
    print(f"A : {a['name']} , {a['description']} , from {a['country']}\n")
    print(vs)
    print(f"B : {b['name']} , {b['description']} , from {b['country']}\n")
    x = input("Enter your choice ").lower()
    if x == a['name']:
      y = compare(a,b)
    else:
      y = compare(b,a)
    if y == 1:
      print("Correct , You get a point")
      score+=1
    else:
      print("You were incorrect , you lose")
      end_of_game = True
    print(f"Your score is {score}")

game()