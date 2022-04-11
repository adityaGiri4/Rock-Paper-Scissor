import machine

class Detailer:
    def __init__(self, choice):
        print("Welcome to the Grand Rock Paper Scissor Game")
        self.choice = choice
    def start(self):
        print("You are having this choices:")
        i = 1
        for ch in self.choice:
            print(f"{i}. {ch}")
            i += 1
        print("You are having 10 chances".upper())
        print("You have to type the respected serial number for desired choice respectively")
        n = input("Wanna play, type 'Yes' or 'No':\n")
        match n:
            case "Yes":
                machine.gamePlay()
            case "No":
                print("We will talk later")
            case _:
                print("Something went wrong, try again")
