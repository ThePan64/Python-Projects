import random
def play():
    Gamer1 = input("Choose Rock Paper or Scissors\n").lower()
#User will choose Rock, Paper, Scissors
    print(Gamer1)


#Computer Options
    options = ["rock" , "paper", "scissors"]
    Terminator = random.choice(options).lower()
    print(Terminator)
    print("You chose " + Gamer1 + " the Terminator chose " +Terminator)

#Breakdown of game
    if Gamer1 == "scissors" and Terminator == "scissors":
        print("TIE")
    elif Gamer1 == "paper" and Terminator == "paper":
        print("TIE")
    elif Gamer1 == "rock" and Terminator == "rock":
        print("TIE")
    elif Gamer1 == "rock" and Terminator == "scissors":
        print("YOU WIN")
    elif Gamer1 == "rock" and Terminator == "paper":
        print("YOU LOSE")
    elif Gamer1 == "paper" and Terminator == "rock":
        print("YOU WIN")
    elif Gamer1 == "paper" and Terminator == "scissors":
        print("YOU LOSE")
    elif Gamer1 == "scissors" and Terminator == "paper":
        print("YOU WIN")
    elif Gamer1 == "scissors" and Terminator == "rock":
        print("YOU LOSE")  

def main():
    play()
    while True:
        Pan = input("Would you like to play again? Y/N\n").upper()
        if Pan == "Y":
            play()
        else:
            break    

main()