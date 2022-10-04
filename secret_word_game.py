import time
from random import choice


def play_hang_man():
    word_list = ["dog", "soccer", "gym", "fitness", "rocket", "league"]
    word = choice(word_list)

    wrong_guess = []

    correct_guess = []
    for i in range(len(word)):
        correct_guess.append('__')

    print('Get ready to play a game of Hang Man!')
    time.sleep(1)
    print('Your word is', len(word), 'letters long.')
    time.sleep(1)

    life = 7

    while life:

        guess = input('Guess a letter! ')
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
            print('That letter is not in your word, try again! You have',
                  life, "lives left!")

        guessed_word = (''.join(correct_guess))
        if guessed_word == word:
            print('Congrats! You guessed the word:', word, '!')
            break

        if life == 0:
            if guessed_word != word:
                print('You lost...better luck next time! The word was', word)
            break

        time.sleep(1)

        print("\n")
        print('Here is what your work looks like now:')
        print("\n")
        print(' '.join(correct_guess))

        time.sleep(1)


play_hang_man()
