# The hangman game
import random
import hangman_art
import hangman_words

words = hangman_words.word_list

stages = hangman_art.stages

logo = hangman_art.logo

print(logo)

# pick a random word from the list
chosen_word = random.choice(words).lower()

print(f"the chosen word is {chosen_word}")

# set lives
lives = 6

display = []

# get word length
word_length = len(chosen_word)

for i in range(word_length):
    display += '_'

guess_count = 0
end_of_game = False
while not end_of_game:
    guess_count += 1
    guess = input("Guess a letter : ").lower()

    if guess not in chosen_word:
        lives -= 1
        print(f"opps {guess} is not in the chosen word, you lose a live")

    if guess in display:
        print(f"you already entered { guess }")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if '_' not in display:
        end_of_game = True

    if lives < 1:
        end_of_game = True

    print(display)

    print(stages[lives])

if '_' in display:
    print('You loss')
else:
    print('You won')
