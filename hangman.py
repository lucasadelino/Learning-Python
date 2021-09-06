# A very simple hangman game

import random

wordList = ['Advocate', 'Berserk', 'Coddle', 'Dawdle', 'Earnest', 'Failure', 
            'Gadfly', 'Heroism', 'Invertebrate', 'Jurisprudence', 'Kennel', 
            'Liminal', 'Mortician', 'Novice', 'Orator', 'Pensive', 'Quotient', 
            'Riveting', 'Sapience', 'Terminus', 'Unity', 'Vicissitude', 
            'Wandering', 'Xenophobia', 'Yield', 'Zealot']

def guessIsValid(): #conditions for a valid guess
    if len(guess) > 1 and guess.upper() != 'GIVE UP':
        print('Please enter only one letter')
        return False
    elif len(guess) == 0:
        print('Please enter a letter')
        return False
    elif guess.isdecimal():
        print('Numbers are not allowed. Please enter a letter')
        return False
    else:
        return True

def guessIsCorrect():
    if guess in word:
        return True
    else:
        return False

def updateGuessList():
    for i in range(len(word)):
            if word[i] == guess:
                guesses[i] = guess

def lostGame():
    if mistakes == 6:
        return True

def wonGame():
    if guesses == word:
        return True

def wannaPlayAgain():
    print('Do you want to play again? (Y/N)')
    answer = 'a'
    while answer.upper() not in 'YN':
        answer = input()
    if answer.upper() == 'Y':
        return True
    else:
        return False
    
def printHangman(): #prints the hangman & 
    if mistakes == 0:
        print(r'''
    |---------|
    |        
    |        
    |        
    |
    |
    ''')
    if mistakes == 1:
        print(r'''
    |---------|
    |         0
    |        
    |        
    |
    |
    ''')
    if mistakes == 2:
        print(r'''
    |---------|
    |         0
    |         |
    |          
    |
    |
    ''')
    if mistakes == 3:
        print(r'''
    |---------|
    |         0
    |        /|
    |         
    |
    |
    ''')
    if mistakes == 4:
        print(r'''
    |---------|
    |         0
    |        /|\
    |         
    |
    |
    ''')
    if mistakes == 5:
        print(r'''
    |---------|
    |         0
    |        /|\
    |        / 
    |
    |
    ''')
    if mistakes == 6:
        print(r'''
    |---------|
    |         0
    |        /|\
    |        / \
    |
    |
    ''')
    
    for i in range(len(guesses)):
        if guesses[i] == '':
            print('_ ', end = '')
        else:
            print(guesses[i] + ' ', end = '')
    print('\n')

print('Welcome to the Hangman game!')
isPlaying = True

while isPlaying:    
    mistakes = 0
    tries = 0
    word = list((random.choice(wordList)).upper())
    guesses = [''] * len(word) #this holds the correct guesses the player has tried so far

    while True:        
        printHangman()
        if lostGame():
            print('Too bad! Game over :(')
            print('The word was ' + ''.join(word))
            if wannaPlayAgain() == True:            
                break
            else:
                isPlaying = False
                break
        if wonGame():
            print('Congatulations! You won the game :) It only took you ' + str(tries) + ' tries!')
            if wannaPlayAgain() == True:            
                break
            else:
                isPlaying = False
                break
        guess = input('Please, enter your guess (or enter "give up" to give up):\n').upper()
        while not guessIsValid():
           guess = input().upper() 
        if guessIsValid():
            if guessIsCorrect():
                updateGuessList()
                tries += 1
            elif guess.upper() == 'GIVE UP':
                print('You gave up on the game...')
                isPlaying = False
                break
            else:
                mistakes += 1
                tries += 1