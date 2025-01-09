def run():
    choose=input("You just landed on a random location after yoor paratchute broke. Do you want to go left or right? ").lower()
    if(choose == "left"):
        choose=input(f"As you kept walking you hear a noise. Would you like to go torwards it or away from it? ").lower()
        if(choose=="towards"):
            print(f"A lion just killed you, you lose")
        elif(choose=="away"):
            print("You kept walking, ran out of water and died, you lose")
        else:
            wrongOption()
    elif(choose == "right"):
        choose=input("As you kept walking, you got thirsty and you see a lake. Would you like to drink water? ").lower()
        if(choose=="yes"):
            print("The water was poisoned, you drank and got killed. You lose")
        elif(choose=="no"):
            print("You died of thirst. You lost")
        else:
            wrongOption()
    else:
        wrongOption()

def wrongOption():
    print("You chose an incorrect option")