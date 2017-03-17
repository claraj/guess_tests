
import random

# Store these separately for ease of editing
# And our tests can use these for comparison
low = 'too low'
high = 'too high'
correct = 'correct! you win!'

def make_secret_number():
    return random.randint(0, 10)


def get_guess():
    while True:
        try:
            return int(input('Guess the number! '))
        except:
            print('please enter a number')


def compare(secret, guess):

    if secret == guess:
        return correct

    if secret < guess:
        return high

    if secret > guess:
        return low



def main():

    secret = make_secret_number()
    guess = get_guess()

    while True:

        result = compare(secret, guess)
        print(result)   # too low, too high, correct!

        if result == correct:
            break;

        guess = get_guess()



if __name__ == '__main__':
    main()
