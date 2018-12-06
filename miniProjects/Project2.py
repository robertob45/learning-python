import random
print('Guess the number')

def check_correct(u_guess, num):
    while True:
        if u_guess < num:
            print('Guess is high!')
            return False
        elif u_guess > num:
            print('Guess is low!')
            return False
        else:
            print('You got it!')
            return True

def guess():
    num = random.randint(1, 5)
    while True:
        while True:
            u_guess = input('What number do you think it is? (Between 1 and 5): ')
            try:
                u_guess = int(u_guess)
                break
            except ValueError:
                print('Invalid number, try again!')
        if check_correct(u_guess, num):
            break
guess()