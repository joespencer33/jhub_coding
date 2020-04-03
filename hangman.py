#Author Joe Spencer
# April 2020

import random
import os
import sys
def main():

    #clears the screen each go
    clear = lambda: os.system('clear') #
        #Open the word list.txt file and store it locally
    #I was unsure if you wanted to access the .txt file or have words stored locally
    #So it can do both
    def create_word_list():
            try:
                word_list=[]
                with open('word_list.txt') as file:
                    for word in file:
                        word_list.append((word.split('\n'))[0])
            except:
                word_list=["rarely", "universe", "notice", "sugar", "interference", "constitution", "we", "minus", "breath", "clarify", "take", "recording", "amendment", "hut", "tip", "logical", "cast", "title", "brief", "none", "relative", "recently", "detail", "port", "such", "complex", "bath", "soul", "holder", "pleasant", "buy", "federal", "lay", "currently", "saint", "for", "simple", "deliberately", "means", "peace", "prove", "sexual", "chief", "department", "bear", "injection", "off", "son", "reflect", "fast", "ago", "education", "prison", "birthday", "variation", "exactly", "expect", "engine", "difficulty", "apply", "hero", "contemporary", "that", "surprised", "fear", "convert", "daily", "yours", "pace", "shot", "income", "democracy", "albeit", "genuinely", "commit", "caution", "try", "membership", "elderly", "enjoy", "pet", "detective", "powerful", "argue", "escape", "timetable", "proceeding", "sector", "cattle", "dissolve", "suddenly", "teach", "spring", "negotiation", "solid", "seek", "enough", "surface", "small", "search"]

            return(word_list)

#Defining function used later to allow game restart.
    def restart_game(y_or_n):
        if y_or_n != 'y' and y_or_n != 'n':
            print("Please enter 'y' or 'n'")
            print('Would You Like To Play Again? (Y/N)')
            play_again=input()
            restart_game(play_again)

        elif y_or_n == 'y':
            choice = None
            rem_guess = None
            word_build = None
            already_guessed = None
            refresh=main()

        elif y_or_n =='n':
            print('\nThanks for Playing, See You Next Time')
            refresh=sys.exit()

        return(refresh)

    #picks a random word from word_list
    choice = random.choice(create_word_list())
    #print (choice)
    length = len(choice)
        #define a few entities that are used later
    rem_guess=7
    already_guessed=[]
    word_build='{}'.format('-'*length)
    width=40

    print("***YOU HAVE {} GUESSES TO FILL IN THE BLANKS***\n".format(rem_guess))

    while rem_guess>0:
        clear ()
        print(("\nYou Have {} Guesses Remaining".format(rem_guess)).upper())
        print('\nWord so far: {}'.format(word_build))
        guess = input('\nType Next Guess: ').lower()

        #Ensure only single letter are input
        #ie No numbers or multiple letters.

        if len(guess)==1 and guess.isalpha():

            #Test to see if already guessed
            if guess in already_guessed:
                    print('You have already guessed {}'.format(guess))
                    continue
            #Log of guesses
            already_guessed.append(guess)

            #see if letter is in the word
            if guess not in choice:
                rem_guess -= 1
                print("\nSorry '{}' is not in the word.".format(guess))
                continue
            #Gives a word to display
            else:
                word_build=''
                print("\nCorrect, '{}' is in the word.".format(guess))
                for letter in choice:
                    if letter in already_guessed:
                        word_build += letter

                    else:
                        word_build += '-'

        #Stops multiple letters or numbers being input
        else:
            print("Please Enter a Valid Input (Single Letters Only)")
        clear()
        #checks if You've reached the word
        if word_build == choice:
            print('\n\nCONGRATULATIONS! You Guessed The Correct Word: {}'.format((choice.upper())))
#Calls to the predefined restart function
            print('Would You Like To Play Again? (Y/N)')
            play_again=input()
            restart_game(play_again)
            clear()
        #Stops if you're out of guesses
    if rem_guess == 0:
        clear()
        print('\n\nGAME OVER...You Ran Out Of Guesses. The Correct Word Was: {}'.format((choice.upper())))
        print('Would You Like To Play Again? (Y/N)')
        play_again=input()
        restart_game(play_again)

main()
