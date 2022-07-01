


from dis import Instruction
import random
from human import Human
from ai import AI
from player import getplayerChoice

class Game:   
   


 def instructions():
    play = input("Would you like to play Rock, Paper, Scissors, Lizard, Spock(y/n): ").lower()
    if play == "y":
            print("1.Rock")
            print("2.Paper")
            print("3.Scissors")
            print("4.Lizard")
            print("5.Spock")

    elif play != "n":
            print("error has accured please type y for yes or n for no:")
           

def instructions():
    play = input("Would you like to play Rock, Paper, Scissors, Lizard, Spock(y/n): ").lower()
    if play == "y":
            print("1.Rock")
            print("2.Paper")
            print("3.Scissors")
            print("4.Lizard")
            print("5.Spock")

    elif play != "n":
            print("error has accured please type y for yes or n for no:")
           







def ai():
            choice = random.randint(1,5)
            if choice == 1:
                print("CPU picked Rock")
            elif choice == 2:
                 print("CPU picked Paper")
            elif choice == 3:
                 print("CPU picked Scissors")
            elif choice == 4:
                 print("CPU picked Lizard")
            elif choice == 5:
                print("CPU picked Spock")
            return choice

def getplayerChoice():
    choice = int(input("Welcome to RPSLS! please pick one '0'Rock, '2'Paper,'3' Scissors,'4' Lizard,'5' Spock: "))
    if choice > 5:
        print("Invalid number please try again....")
        getplayerChoice()
    elif choice < 1:
        print("Invalid number please try again....")
        getplayerChoice()
    elif choice == 1:
        print("You picked Rock")
    elif choice == 2:
        print("You picked Paper")
    elif choice == 3:
        print("You picked Scissors")
    elif choice == 4:
        print("You picked Lizard")
    elif choice == 5:
        print("You picked Spock")
    return choice


def win(playerChoice, CPUChoice, playerWins, CPUWins, ties):
    if playerChoice == 1 and CPUChoice == 3 or CPUChoice == 4:
        print("Player wins.")
        playerWins = playerWins.append(1) 
    elif playerChoice == 2 and CPUChoice == 1 or CPUChoice == 5:
        print("Player wins.")
        playerWins = playerWins.append(1) 
    elif playerChoice == 3 and CPUChoice == 2 or CPUChoice == 4:
        print("Player wins.")
        playerWins = playerWins.append(1) 
    elif playerChoice == 4 and CPUChoice == 2 or CPUChoice == 5:
        print("Player wins.")
        playerWins = playerWins.append(1)
    elif playerChoice == 5 and CPUChoice == 1 or CPUChoice == 3:
        print("Player wins.")
        playerWins = playerWins.append(1)
    elif playerChoice == CPUChoice:
        print("Tie")
        ties = ties.append(1)
    else:
        print("CPU won")
        CPUWins = CPUWins.append(1) 
    return

def gameTotal(playerWins, CPUWins, ties):
    playerWins = sum(playerWins)
    CPUWins = sum(CPUWins)
    ties = sum(ties)
    print("Player final score: ", playerWins)
    print("CPU final Score: ", CPUWins)
    print("Total ties: ",ties)

def main():
    playerChoice = 0
    playerWins = []
    CPUChoice = 0
    CPUWins = []
    ties = []
    finalPlayerWins = 0
    finalCPUWins = 0
    finalTies = 0
    Continue = 'y'
    Instruction=''
    while Continue == 'y':
        playerChoice = getplayerChoice()
        CPUChoice = AI()
        win(playerChoice,CPUChoice,playerWins, CPUWins, ties)
        Continue = input("Would you like to play again (y/n):").lower()
        if Continue == 'n':
            print("Printing final scores.")
            break
    (playerWins, CPUWins, ties)


main()