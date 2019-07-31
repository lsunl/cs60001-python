# Problem Set 2, hangman.py

# Hangman Game
# -----------------------------------
# Helper code

import random
import string
from string import ascii_lowercase, ascii_letters


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters = "".join(letters_guessed)
    if (secret_word.lower() == letters.lower()):
        return True
    else:
        return False




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    # letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word = string_to_dashedlist(secret_word)

    for letter in letters_guessed:
        if letter in secret_word:
            index = secret_word.index(letter)
            word[index] = letter
    return word





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = ""
    for x in ascii_lowercase:
        if x not in letters_guessed:
            letters += (x + " ")
    return letters


def string_to_dashedlist(secret_word):
    '''
    secret_word: secret words
    returns: string of underscores to represent secret word
    '''
    word = []
    for letter in secret_word:
        word.append("_ ")
    return word


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("You get 6 guesses")
    print(string_to_dashedlist(secret_word))

    letters_guessed = []
    guessnumber = 6

    while (is_word_guessed(secret_word, letters_guessed) == False):

        # Ask user for letter
        guess = input("Pick a letter: ")

        # Appends the letter to list of all letters guessed
        letters_guessed.append(guess)

        # Display list of letters that user has not guessed
        print(get_available_letters(letters_guessed))

        # Display partially guessed word
        print(get_guessed_word(secret_word, letters_guessed))

        # Check if all the letters of the secret word has been guessed
        is_word_guessed(secret_word, letters_guessed)

        # Check if the guess is valid and adjust guess number
        if guess not in secret_word:
            guessnumber -= 1
            print(f"You have {guessnumber} turn(s) left.")

        if (guessnumber <= 0):
            print("You lost. The word is: ")
            print(secret_word)
            break

    if (is_word_guessed(secret_word, letters_guessed) == True):
        print("Congrats! You won!")

    return 0





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    if len(my_word) == len(other_word):
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for other_word in wordlist:
        if (match_with_gaps(my_word, other_word) == True):
            myword = "".join(my_word)
            if myword in other_word:
                print(other_word)


    return 0


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("You have 6 guesses")
    guessNum = 6
    letters_guessed = []


    while (is_word_guessed(secret_word, letters_guessed) == False):

        my_word = ""

        # Ask user for guess and check if it's a letter or *
        guess = input("Pick a letter: ")
        if guess == "*":
            print(show_possible_matches(my_word))

        while guess not in ascii_letters:
            guess = input("Pick a letter: ")


        letters_guessed.append(guess)

        if guess in secret_word:
            my_word.append(guess)

        # Display partially guessed word
        my_word = get_guessed_word(secret_word, letters_guessed)
        print(my_word)

        # Check if the guess is valid and adjust guess number
        if guess not in secret_word:
            guessNum -= 1
            print("Your guess is not in the secret word")
            print(f"You have {guessNum} turn(s) left.")

        if (guessNum <= 0):
            print("You lost. The word is: ")
            print(secret_word)
            break

    if (is_word_guessed(secret_word, letters_guessed) == True):
        print("Congrats! You won!")

    return 0


# # When you've completed your hangman_with_hint function, comment the two similar
# # lines above that were used to run the hangman function, and then uncomment
# # these two lines and run this file to test!
# # Hint: You might want to pick your own secret_word while you're testing.
#
#
if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
