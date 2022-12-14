import random
from words import words_list


lives_remaining = 7
guessed_letters = ''


def pick_a_word():
    """
    Function to generate a random word from our list of strings
    """
    word_position = random.randint(0, len(words_list) - 1)
    return words_list[word_position]


def welcome():
    """
    Function to welcome the user to our Hangman Game
    """
    print('|    ********** H A N G M A N **********      |')
    print('|          Welcome to Hangman game!           |')
    print('|         **********RULES***********          |')
    print('|                                             |')
    print('| 1. Enter a letter or a whole word           |')
    print('| 2. Press "Enter" to submit                  |')
    print('| 3. You have 7 lives                         |')
    print('| 4. For every wrong entry you loose one life |')
    print('| 5. You dont loose lives for wrong input     |')
    print('|    (number, symbol or space)                |')
    print('|_____________________________________________|')


def play():
    """
    Playing the game function
    """
    welcome()
    word = pick_a_word()
    while True:
        print('Lives remaining: ' + str(lives_remaining))
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            print('The word is ' + word)
            break
        if lives_remaining < 1:
            print('You are Hung!')
            print('The Word was: ' + word)
            break


def get_guess(word):
    """
    Function to tell how the player is doing when they try and guess
    Gives a print statement with lives remaining after guess
    Returning the user's guess
    """
    print_word_with_blanks(word)
    global lives_remaining
    while True:
        try:
            guess = input('Guess a letter or a whole word?\n')
            if guess.isalpha():
                return guess
            if guess in guessed_letters:
                print('This letter has been guessed')
            raise ValueError('Invalid input')
        except:
            print('Invalid input!')
        else:
            return guess


def print_word_with_blanks(word):
    """
    Compares the letter the player entered with every letter ofselected word.
    Displays if any of the guessed letters are in the generated word.
    """
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > - 1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    
    print(display_word)


def process_guess(guess, word):
    """
    To decide what to do if the user enters whe whole word or a single letter.
    """
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)
    


def whole_word_guess(guess, word):
    """
    Function to handle if the user guessed the whole word
    """
    global lives_remaining
    if guess.lower() == word.lower():
        return word
    else:
        lives_remaining == lives_remaining - 1
        return False


def single_letter_guess(guess, word):
    """
    Function to handle a single letter input
    """
    global guessed_letters
    global lives_remaining
    if word.find(guess) == - 1:
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess.lower()
    if all_letter_guessed(word):
        return True
    return False

  
def all_letter_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == - 1:
            return False
    return True

play()  
 
