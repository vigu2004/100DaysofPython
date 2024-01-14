import random
import hangman_words
import hangman_art

word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

logo = hangman_art.logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages=hangman_art.stages
    print(stages[lives])