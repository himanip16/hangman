import random
from art import logo, stages
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)


#Create blanks
display = ["_" for i in range(word_length)]


while not end_of_game:
    guess = input(f"Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}. Try another word")
        continue

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(" ".join(display))
    print(stages[lives])

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")


