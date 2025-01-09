import random
def run():
    shouldPlay = input(f"Do you want to play a game? ")
    if(shouldPlay and (shouldPlay.lower().find("yes") == 0 or shouldPlay.lower().find("yeah") == 0 or shouldPlay.lower().find("sure") == 0 or shouldPlay.lower().find("why not") == 0)):
        random_num=random.randint(1,3)
        guess=input("Guess the number ")
        if int(random_num) == int(guess):
            print(f"You are right, the number is {random_num}")
        else:
            print(f"You are wrong, the number is {random_num}") 
    else:
        print(f"Look forward to playing with you when you are bored. Bye!")