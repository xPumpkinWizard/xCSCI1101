import re
import random

#get the answer.
pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line : 
    pool_answers.append(pool_answer_line)

    pool_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

answer = answer.upper()

# Pre-game setup.
answer_guessed = []

for current_answer_char in answer: 
    if re.search("^[A-Z]$", current_answer_char):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# Game logic.
num_of_wrong = 5

current_inc_guesses = 0

letters_guess = []

# User gameplay logic.

while current_inc_guesses < num_of_wrong and False in answer_guessed:
    # Display game summary. 
    print(f"Number of inccorect guesses remaining: {num_of_wrong - current_inc_guesses}")
    print("Guessed letter: ", end="")
    
    for current_letters_guesses in letters_guess:
        print(current_letters_guesses, end=" ")

    print()

    #Display puzzle board.
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")
    print()

    #let user guess a letter.
    letter = input("enter a letter: ")


    letter= letter.upper()

    # check if user enttered a valid letter.
    if  re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letters_guess: 
        #insert the letter guessed by the user (insertion sort).
        current_letter_index = 0

        for current_letter_guesses in letters_guess:
            if letter < current_letter_guesses:
                break

            current_answer_index += 1
        
        letters_guess.insert(current_letter_index, letter)

        # cheack if letter is in the puzzle.
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_inc_guesses += 1
# post game summary.
if current_inc_guesses < num_of_wrong:
    print("Congratulations, you won!")
else: 
    print(f"sorry, you lost, the anser was {answer}")