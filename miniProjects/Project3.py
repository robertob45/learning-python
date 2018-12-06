import time

def start_game():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    word = 'hello'
    word_len = len(word)
    used_letters = []
    print('Hello! :)\n')
    time.sleep(2)
    print('The word you have to guess has', word_len, 'characters\n')
    time.sleep(2)
    print('You can only enter 1 letter from a - z\n')
    time.sleep(2)
    print('Lets start! :)\n')
    time.sleep(2)
    guessing(letters, used_letters, word, word_len)


def guessing(letters, used_letters, word, word_len):
    correct_lett = []
    missed_lett = []
    blank_spaces = '_' * word_len
    print(blank_spaces, '\n')
    attempts = 3
    print('You have:', attempts, 'attempts')
    print('')
    while attempts > 0:
        guess = input('Enter a letter')
        print('')
        if not guess in letters:
            print('Thats not a valid letter!')
        elif guess == '':
            print('No blank spaces!')
        elif guess in used_letters:
            print('You already have used that letter!')
        else:
            used_letters.append(guess)
            correct_lett.append(guess)
            if guess in word:
                print('You got one!\n')
                for x in range(word_len):
                    if word[x] in correct_lett:
                        blank_spaces = blank_spaces[:x] + word[x] + blank_spaces[x+1:]
                for letter in blank_spaces:
                    print(letter, end=' ')
                print('')
                print('')
                foundAllLetters = True
                for y in range(word_len):
                    if not word[y] in correct_lett:
                        foundAllLetters = False
                if foundAllLetters:
                    print('You won! :D')
                    playAgain = input('Want to play again? :) y/n')
                    if playAgain == 'y':
                        start_game()
                    else:
                        print('Goodbye! ;)')
                        break
            else:
                print('That letter is not in the word!, -1 try')
                missed_lett.append(guess)
                attempts -= 1
                if attempts == 0:
                    print('Sorry you lost :(, the word was:', word)

# def won(correct_lett):
#     foundAllLetters = True
#     for y in range(word_len):
#         if not word[y] in correct_lett:
#             foundAllLetters = False
#     if foundAllLetters:
#         print('You won! :D')

start_game()