import random
import main

chances = 10
manual_points = 0
computer_points = 0
times = 1

def gamePlay():
    global times
    global chances
    global manual_points
    global computer_points
    while times <= chances:
        manualChoice = input("Enter R for Rock, S for Scissor and P for paper: \n")
        aritificialChoice = random.choice(main.listOfChoice)
        if manualChoice == "R" and aritificialChoice == "Scissor":
            print("You Won")
            print(f"Computer did {aritificialChoice}")
            manual_points += 1
            print(f"{10 - times} chances left.....")
        elif manualChoice == "R" and aritificialChoice == "Paper":
            print("Computer Won")
            print(f"Computer did {aritificialChoice}")
            computer_points += 1
            print(f"{10 - times} chances left.....")
        elif manualChoice == "R" and aritificialChoice == "Rock":
            print("Game tied")
            print(f"Computer also did {aritificialChoice}")
            print(f"{10 - times} chances left.....")
        elif manualChoice == "S" and aritificialChoice == "Rock":
            print("Computer Won")
            print(f"Computer did {aritificialChoice}")
            computer_points += 1
            print(f"{10 - times} chances left.....")
        elif manualChoice == "S" and aritificialChoice == "Paper":
            print("You Won")
            print(f"Computer did {aritificialChoice}")
            manual_points += 1
            print(f"{10 - times} chances left.....")
        elif manualChoice == "S" and aritificialChoice == "Scissor":
            print("Game tied")
            print(f"Computer also did {aritificialChoice}")
            print(f"{10 - times} chances left.....")
        elif manualChoice == "P" and aritificialChoice == "Rock":
            print("You Won")
            print(f"Computer did {aritificialChoice}")
            manual_points += 1
            print(f"{10 - times} chances left.....")
        elif manualChoice == "P" and aritificialChoice == "Scissor":
            print("Computer Won")
            print(f"Computer did {aritificialChoice}")
            computer_points += 1
            print(f"{10 - times} chances left.....")
        elif manualChoice == "P" and aritificialChoice == "Paper":
            print("Game tied")
            print(f"Computer also did {aritificialChoice}")
            print(f"{10 - times} chances left.....")
        else:
            print("Something went wrong, try again")
        times += 1

        if times > 10:
            print("\n\nGame Over")
            if manual_points < computer_points:
                print(f"Computer Scored: {computer_points} points\nYou Scored: {manual_points} points")
                print("Computer Won".upper())
            elif manual_points > computer_points:
                print(f"You Scored: {manual_points} points\nComputer Scored: {computer_points} points")
                print("You Won".upper())
            elif manual_points == computer_points:
                print(f"Computer Scored: {computer_points} points\nYou Scored: {manual_points} points")
                print("Game tied".upper())
                print("No one won")
            else:
                print("No results declared")
            print("Thanks for playing....")



