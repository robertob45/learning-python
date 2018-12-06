from random import *

def roll():
    y_n = input('Would you like to throw again? (y/n)')
    if y_n == 'y':
        dado()
    elif y_n == 'n':
        print('Exit...')
    else:
        print('Invalid answer, try again')
        roll()

def dado():
    print('Throwing dice...')
    print('.')
    print('.')
    print('The number is:', randint(1,6))
    roll()

dado()