# this is a simple hangman game script
# summon the randomizer!!!
import random

# I really wanted to install and import a package that generates random words, but I haven't learned how to yet
# here's a big old collection of words presented as data values getting split to form a list of strings
word_pool = "educational freak bloody torch caregiver surreal capture crypt dexterity fool menace finale settler" \
            "rerun pill believing bloat evaluate bachelor growl barbell world trauma old blocker domino finite daisy" \
            "day absolution brand daddy switch deathtrap devil coil charade pitch headstrong chromosome pick promised" \
            "coma locus border biological".split()

# assigned the value of the rando word to "word". word_list is a list of its letters in order
word = random.choice(word_pool)

# fills word_list with letters from "word" in order. word_list2 is a version of word_list meant to be manipulated
word_list = []
for i in word:
    word_list.append(i)
word_list2 = list(word_list)

# creates a list of placeholders that will be replaced with letters contingent on successful guesses
user_word = []
for i in word:
    user_word.append("_")


# to visualize the hangman as wrong answers are given, I'll define a function that interacts with loss_value
# the "stage" loss_value is at will print a different hangman. the final stage prints an exit message and
def hangman_status():
    if len(wrong_guesses) == 0:
        print('   +----+')
        print('   |    |')
        print('        |')
        print('        |')
        print('        |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
    elif len(wrong_guesses) == 1:
        print('   +----+')
        print('   |    |')
        print('   O    |')
        print('        |')
        print('        |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
    elif len(wrong_guesses) == 2:
        print('   +----+')
        print('   |    |')
        print('   O    |')
        print('   I    |')
        print('        |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
    elif len(wrong_guesses) == 3:
        print('   +----+')
        print('   |    |')
        print('   O    |')
        print('  |I    |')
        print('        |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
    elif len(wrong_guesses) == 4:
        print('   +----+')
        print('   |    |')
        print('   O    |')
        print('  |I|   |')
        print('        |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
    elif len(wrong_guesses) == 5:
        print('   +----+')
        print('   |    |')
        print('   O    |')
        print('  |I|   |')
        print('  l     |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
    else:
        print('   +----+')
        print('   |    |')
        print('   O    |')
        print('  |I|   |')
        print('  l l   |')
        print('  ______|_')
        print(f"You have {6 - len(wrong_guesses)} guesses left.")
        print("You lose!")
        quit()
    return


name = input('Welcome to Hangman! Please enter you name: ')
print('Good luck!')
print(f'Your word has {len(word_list)} letters.')

# inspired by a friend, this list will be stuffed with wrong guesses which will be printed for the user to see
# loss_value goes hand in hand. once it reaches 6 (six wrong guesses), the script quits
wrong_guesses = []

# this uh... is actually really hard for me to explain. but I can say simply what it does
# this code prompts guessing a letter. if the guess is right, it displays the user's correct guesses together
# if the guess is wrong, it shows a list of wrong guesses so far, and uses a function to visualize the hangman
# this is done through one main red-pilled alpha male loop and several pathetic beta male nested loops
while user_word != word_list:
    x = input("Please guess a letter: ")
    if x in word_list2:
        while x in word_list2:
            y = word_list2.index(x)
            user_word[y] = x
            word_list2[y] = 0
            print(f"{x} was right!")
    else:
        print(f"Oops, it's not {x}!")
        if x not in wrong_guesses:
            wrong_guesses.append(x)
        print(f"Oops, it's not {x}!")
        hangman_status()
        print(f"Wrong guesses: {' '.join(wrong_guesses)}")
    print(' '.join(user_word))
print(f"That's right! The word is {word}!!")
print(f"Congratulations, {name}, you won!")
