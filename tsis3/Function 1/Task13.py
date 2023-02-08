import random

def Guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print("\nWell, {name}, I am thinking of a number between 1 and 20.".format(name=name))
    
    
    guess_num = random.randint(1,20)
    gn=0
    while gn<10:
        num = int(input("Take a guess.\n"))
        gn+=1
        if num < guess_num:
            print("\nYour guess is too low.")
        elif num > guess_num:
            print("\nYour guess is too high.")
        else:
            break

    if num == guess_num:
        print("\nGood job, {name}! You guessed my number in {gn} guesses!".format(name=name,gn=gn))
    else:
        print("\nNope. The number I was thinking of was {guess_num}".format(guess_num=guess_num))
Guess_the_number()
