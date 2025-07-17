# python terminal game for jotto

import random
import os

word_list = []
with open("words.txt", "r") as file:
    word_list = file.readlines()

for i in range(0, len(word_list)):
    word_list[i] = word_list[i].strip()

secret_word = word_list[random.randint(0,len(word_list)-1)]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guesses = []
omitted_letters = [] # guesses that score 0 confirm the letter isn't in the secret
likely_letters = {} # letters potentially in the secret, value is accumulated based on guess score 1-4
secret_not_guessed = True

# returns count of letters in the guess that match the secret word
def get_score(secret_word, guess):
    score = 0
    secret_word_characters = list(secret_word)
    for letter in guess:
        if letter in secret_word_characters:
            score += 1
            secret_word_characters.remove(letter)
    return score

def print_game_board(guesses, likely_letters, omitted_letters):
    
    os.system('cls' if os.name == 'nt' else 'clear')

    print("----------------------------------------------------------")
    print("|                 Let's Play Jotto!                      |")
    print("----------------------------------------------------------")
    print("Previous Guesses and Point Value:")
    for guess in guesses:
        print("  {} - {}".format(guess, get_score(secret_word, guess)))
    print("\nLikely Letters:")
    count = 0
    temp_string = "  "
    for letter in likely_letters:
        temp_string += letter
        if count < 9 and count < len(likely_letters) - 1:
            temp_string += ", "
        else:
            break
        count += 1
    print(temp_string)
    print("\nOmitted Letters:")
    temp_string = "  "
    count = 0
    for letter in omitted_letters:
        temp_string += letter
        if count < len(omitted_letters) - 1:
            temp_string += ", "
        else:
            break
        count += 1
    print(temp_string)

    
while secret_not_guessed:
    print_game_board(guesses, likely_letters, omitted_letters)

    guesses.append(input("\nGuess a word: "))

    score = get_score(secret_word, guesses[-1])

    # add to omitted letters list
    if score == 0:
        for letter in guesses[-1]:
            if letter not in omitted_letters:
                omitted_letters.append(letter)
        omitted_letters.sort()
    # else add to likely letters list    
    else:
        for letter in guesses[-1]:
            if letter in likely_letters:
                likely_letters[letter] += score
            else:
                likely_letters[letter] = score
        likely_letters = dict(sorted(likely_letters.items(), key=lambda item: item[1], reverse = True))

    if guesses[-1] == secret_word or guesses[-1] == 'quit':
        secret_not_guessed = False

print("\nCongrats, you guessed it!")
num_tries = len(guesses)
print("It took you {} tries for a score of {} points.".format(num_tries, 105 - num_tries * 5))
