#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

DIFFICULTY_LEVELS_EASY = 5
DIFFICULTY_LEVELS_HARD = 10

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == 'easy':
        return DIFFICULTY_LEVELS_EASY
    else:
        return DIFFICULTY_LEVELS_HARD

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
    else:
        print("Too low.")
    print("Guess again.")    
    return turns - 1

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking og a number between 1 and 100.")

    answer = random.randint(1, 100)
    print(answer)
    turns = set_difficulty()

    while turns != 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))     
        if answer == guess:
            print(f"You got it! The answer was {answer}.")
            break
        else:
            turns = check_answer(guess, answer, turns)
    else:
        print("You've run out of guesses, you lose.")
        
game()