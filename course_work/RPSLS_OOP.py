import random

ITEMS = {"rock": ["lizard", "scissors"],
         "lizard": ["paper", "spock"],
         "spock": ["scissors", "rock"],
         "scissors": ["lizard", "paper"],
         "paper": ["rock", "spock"]}


class Player:

    def __init__(self):
        self.choice = None

    def ask_choice(self):
        while True:
            self.choice = input("Your choice (rock paper scissors lizard spock)?: ")
            if self.choice not in ITEMS.keys():
                print("Invalid input")
            else:
                break
        return self.choice

    def random_choice(self):
        self.choice = random.choice(list(ITEMS.keys()))
        return self.choice


def find_winner(player_item, computer_item):
    if computer_item in ITEMS[player_item]:
        return "Player wins!"
    elif computer_item == player_item:
        return "Tie!"
    else:
        return "Computer wins!"


if __name__ == '__main__':

    # create instance's player and computer
    player = Player()
    computer = Player()

    game = True
    while game:

        # ask player his choice
        player_choice = player.ask_choice()
        print("Players:", player_choice)

        # make random computer choice
        computer_choice = computer.random_choice()
        print("Computer:", computer_choice)

        # find and print winner
        print(find_winner(player_choice, computer_choice))

        # ask repeat game
        while True:
            repeat = input("Repeat (Y/N)?: ").lower()
            if repeat == "y":
                break
            elif repeat == "n":
                game = False
                break
            else:
                print("Invalid input")
