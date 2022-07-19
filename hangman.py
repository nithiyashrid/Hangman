import random
from words import wordList,hangman

#to choose a random word from the given wordlist
def chooseWord():
    word = random.choice(wordList).lower()
    return word

#to initialize the word to be found
def initializeParams(word):
    length = len(word)
    notGuessed = ['_']*length
    return notGuessed


def play(word,notGuessed):
    guessedOverall = []
    guessedCorrect = []
    guessedWrong = []
    guessed = False
    print(hangman[0])
    incrementHangman = 1
    #until the hangman is built completely-guessing is allowed
    while incrementHangman<8:
        nextChar = input("Enter the guessed letter\t:\t")
        nextChar = nextChar.lower()

        while nextChar in guessedOverall:
            print("Cannot guess the same letter again, change your guess")
            nextChar = input("\nEnter the guessed letter\t:\t")
        guessedOverall.append(nextChar)

        if nextChar in word:
            print(hangman[incrementHangman])
            for i in range(len(word)):
                if word[i]==nextChar:
                    notGuessed[i] = nextChar
            print("Guessed word :-",notGuessed)
            guessedCorrect.append(nextChar)

        else:
            print(hangman[incrementHangman])
            print("\nWRONG Guess, Attempts left\t=\t",7-incrementHangman)
            incrementHangman += 1
            guessedWrong.append(nextChar)
        if notGuessed.count('_')==0:
            guessed = True
            break

    if guessed == True:
        return "You Win!"
    else:
        return "You loose :("


#start the game
word = chooseWord()
notGuessed = initializeParams(word)
result = play(word,notGuessed)
print("\n",result)

choice=input("Do you want to continue?(Y/N)").lower()
choice = True if choice=='y' else False

#if-want to continue repeat the same steps
while choice:
    word = chooseWord()
    notGuessed = initializeParams(word)
    result = play(word,notGuessed)
    print("\n",result)
    choice=input("Do you want to continue?(Y/N)").lower()
    choice = True if choice=='y' else False
