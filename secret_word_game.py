import time
from random import choice
from random_word import RandomWords


def play_hang_man():

    print(''' 
 __   __  _______  __    _  _______  __   __  _______  __    _ 
|  | |  ||   _   ||  |  | ||       ||  |_|  ||   _   ||  |  | |
|  |_|  ||  |_|  ||   |_| ||    ___||       ||  |_|  ||   |_| |
|       ||       ||       ||   | __ |       ||       ||       |
|       ||       ||  _    ||   ||  ||       ||       ||  _    |
|   _   ||   _   || | |   ||   |_| || ||_|| ||   _   || | |   |
|__| |__||__| |__||_|  |__||_______||_|   |_||__| |__||_|  |__|
''')

    r = RandomWords()
    word = r.get_random_word()

    wrong_guess = []

    correct_guess = []
    for i in range(len(word)):
        correct_guess.append('__')

    print('Get ready to play a game of Hang Man!')
    time.sleep(1)
    print('Your word is', len(word), 'letters long.')
    time.sleep(1)
    print("\n")

    life = 7

    while life:

        guess = input('Guess a letter! ')

        if not guess.isalpha():
            print('That is not a letter, please try again.')
            continue
        if len(guess) > 1:
            print('Please guess only one letter.')
            continue

        if guess in wrong_guess:
            print('You\'ve already guessed that, try another letter.')
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    correct_guess[i] = word[i]
            print(
                'You guessed a letter correctly!')
        elif guess not in word:
            wrong_guess.append(guess)
            life -= 1
            print('Nope! That letter is not in your word.')

        guessed_word = (''.join(correct_guess))
        if guessed_word == word:
            print('Congrats! You guessed the word:', word, '!')
            break

        time.sleep(1)

        print("\n")

        if life == 7:
            print('''
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___ ''')
            print('You have', life, 'lives left!')
        elif life == 6:
            print('''
      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
 ____|___ ''')
            print('You have', life, 'lives left!')
        elif life == 5:
            print('''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___ ''')
            print('You have', life, 'lives left!')
        elif life == 4:
            print('''
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ____|___ ''')
            print('You have', life, 'lives left!')
        elif life == 3:
            print('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ____|___ ''')
            print('You have', life, 'lives left!')
        elif life == 2:
            print('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___ ''')
            print('You have', life, 'lives left!')
        elif life == 1:
            print('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___ ''')
            print('You have', life, 'life left!')
        elif life == 0:
            print('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
 ____|___ ''')
            if guessed_word != word:
                print('You lost...better luck next time! The word was', word)
                break

        time.sleep(1)

        print("\n")
        print('Here is what your work looks like now:')
        print("\n")
        print(' '.join(correct_guess))
        print("\n")

        time.sleep(1)


play_hang_man()
