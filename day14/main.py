import game_data 
import art
import random

logo = art.logo
vs = art.vs
data = game_data.data
def return_a_person():
  """Returns a random person from the list"""
  x = random.ranint(0 , len(data)-1)
  return data[x]


def compare(a , b):
  if a["follower_count"] > b["follower_count"]:
    return 1
  else:
    return 0

# def game():
#   score = 0
#   print(logo)
#   a = return_a_person()
#   b = return_a_person()
#   print("Who has more followers :\n")
#   print(f"A : {a['name']} , {} ")