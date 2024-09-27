from random import randint
from words import words

def random_word():
    valid_word = False
    random_word = ""
    while(not valid_word):
        random_word = words[randint(0, len(words)-1)]
        if (random_word.count('-') == 0 and random_word.count(' ') == 0):
            valid_word = True
    return random_word

def Hangman(lives):
    letters_used = []
    word = random_word().upper()
    game = ["-"]*len(word)

    while(lives > 0):

        if(game.count('-') == 0):
            print("You win! Congratulations.")
            break

        print("Current word: ", ' '.join(game))
        print("Letters Used: ", ' '.join(letters_used))
        letter = input(f"You have {lives} lives left. Guess a letter: \n")

        if(len(letter) != 1):
            print("You have entered too many characters. Please input a letter.\n")
            continue
        elif(letter.isalpha == False):
            print("You did not input a letter. Please input a letter.\n")
            continue
        elif(letters_used.count(letter.upper()) > 0):
            print("You have used this letter already. Please choose a different letter\n")
            continue
        else:
            letter = letter.upper()
            letters_used.append(letter)
            if(word.count(letter) == 0):
                print(f"Your letter {letter} is not found in the word. You lose 1 life. \n")
                lives -= 1
            else:
                for i in range(len(word)):
                    if(word[i] in letters_used):
                        game[i] = word[i]
    
    if(lives == 0):
        print(f"You lose. The word was {word}")
                

Hangman(5)
        


        
