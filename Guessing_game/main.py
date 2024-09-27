import random

length = int(input("You want to guess a number between 1 to what?:  "))

ran_num = random.randint(1, length)

guess = 0

while(guess != ran_num):
    guess = int(input(f"Guess a number between 1 and {length}:  "))

    if(guess > ran_num):
        print("Sorry, guess again. Too high.")
        continue
    

    if(guess < ran_num):
        print("Sorry, guess again. Too low.")
        continue
    
print(f"Yay, congrats. You have guessed the number {ran_num} correctly!!")
