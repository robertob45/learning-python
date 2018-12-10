import time
import random
import sys

def start_game():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    wordList = ["lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]
    secretWord = random.choice(wordList)
    word_len = len(secretWord)
    used_letters = []
    print('Hello! :)\n')
    # time.sleep(2)
    print('The word you have to guess has', word_len, 'characters\n')
    # time.sleep(2)
    print('You can only enter 1 letter from a - z\n')
    # time.sleep(2)
    print('Lets start! :)\n')
    # time.sleep(2)
    guessing(letters, used_letters, secretWord, word_len)


def guessing(letters, used_letters, secretWord, word_len):
    correct_lett = []
    missed_lett = []
    blank_spaces = '_' * word_len
    print(blank_spaces, '\n')
    attempts = 10
    print('You have:', attempts, 'attempts')
    print('')
    while attempts > 0:
        guess = input('Enter a letter (Write "exit", to stop playing):\n')
        print('')
        if guess == 'exit':
            sys.exit('Ok, goodbye! :)')
        elif not guess in letters:
            print('Thats not a valid letter!')
        elif guess == '':
            print('No blank spaces!')
        elif guess in used_letters:
            print('You already have used that letter!')
        else:
            used_letters.append(guess)
            correct_lett.append(guess)
            if guess in secretWord:
                print('You got one!\n')
                for x in range(word_len):
                    if secretWord[x] in correct_lett:
                        blank_spaces = blank_spaces[:x] + secretWord[x] + blank_spaces[x+1:]
                for letter in blank_spaces:
                    print(letter, end=' ')
                print('')
                print('')
                foundAllLetters = True
                for y in range(word_len):
                    if not secretWord[y] in correct_lett:
                        foundAllLetters = False
                if foundAllLetters:
                    print('You won! :D\n')
                    playAgain = input('Want to play again? :) y/n: ')
                    print('')
                    if playAgain == 'y':
                        start_game()
                    else:
                        sys.exit('Goodbye! ;)')
            else:
                print('That letter is not in the word!, -1 try')
                print('You have', attempts, 'attempts left')
                missed_lett.append(guess)
                attempts -= 1
                if attempts == 0:
                    print('Sorry you lost :(, the word was:', secretWord)

# def won(correct_lett):
#     foundAllLetters = True
#     for y in range(word_len):
#         if not word[y] in correct_lett:
#             foundAllLetters = False
#     if foundAllLetters:
#         print('You won! :D')

start_game()