import random

def run():
    options_mapping=["rock","paper","scissors"]
    computer_pick= options_mapping[random.randint(0,2)]
    pythonWin=False
    user_turn=input("Choose- rock paper scissors, GO! ").lower()
    if(user_turn and user_turn in options_mapping):
        print(f"{computer_pick.capitalize()}")
        if(user_turn == computer_pick):
            print(f"It's a draw!")
        else:
            if(user_turn=="rock" and computer_pick=="paper"):
                pythonWin=True
            elif(user_turn=="paper" and computer_pick=="scissors"):
                pythonWin=True
            elif((user_turn=="scissors" or user_turn=="scissor") and computer_pick=="rock"):
                pythonWin=True
            if(pythonWin==True):
                print("I win 🥹")
            else:
                print("Okay, you win 😒")
    else:
        print("You didn't choose anything")