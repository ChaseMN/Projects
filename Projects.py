# Projects
import random


# Safe(er) input function. Returns specific data types depending on the input
def safe_input(text):
    print(text)
    userinput = input('')
    if userinput.isdigit():
        return int(userinput)
    else:
        return userinput


# Encoder, takes a user given input and shifts it to the right by three (a caesar cipher). Excludes non-letters.
def encoder():
    print('Running encoder')
    enabled = True
    while enabled:
        user_input = input('Input text to be encoded using a caesar cipher or "!exit" to return to project selection.\n')
        if user_input.lower() == '!exit':
            enabled = False
        else:
            output = ''
            for char in user_input:
                x = ord(char)
                if 65 <= x <= 90 or 97 <= x <= 122:
                    if 87 < x < 91 or 119 < x < 123:
                        x -= 26
                    x += 3
                output += chr(x)
            print(output + '\n')


# Little number guessing game. Self-explanatory, hopefully
def numberguess():
    running = True
    print('Starting Number Guesser...\n')
    while running:
        tries = 1
        end = safe_input(
            "What's the maximum range for guessable numbers you'd like? Only non-negative integers 10 or above.\n"
            "Alternatively, type exit to return to the selection screen.")
        while type(end) != int or end < 10:
            if end == 'exit':
                break
            end = safe_input("Please enter a valid integer (non-negative, 10 or greater).")
        if end == 'exit':
            break
        number = random.randrange(0, end)
        guess = safe_input("Enter your guess.")
        while type(guess) != int:
            guess = safe_input("Please enter an integer.")
        if guess > number:
            print('The number is lower than your guess.')
        if guess < number:
            print('The number is higher than your guess.')
        while guess != number:
            guess = safe_input("Try again?")
            tries += 1
            while type(guess) != int:
                guess = safe_input("Please enter an integer.")
            if guess > number:
                print('The number is lower than your guess.')
            if guess < number:
                print('The number is higher than your guess.')
        print('Correct! The number was', number, '. You guessed it in', tries, 'tries.')


# Project selector
while True:
    projects = ('encoder', 'numberguess')
    print("Which project would you like to select?\n", projects, sep='')
    selection = input().lower()
    match selection:
        case 'encoder':
            encoder()
        case 'numberguess':
            numberguess()
        case other:
            print('Invalid input, please try again')
