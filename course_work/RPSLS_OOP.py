import random

ITEMS = {"rock": ["lizard", "scissors"],
         "lizard": ["paper", "spock"],
         "spock": ["scissors", "rock"],
         "scissors": ["lizard", "paper"],
         "paper": ["rock", "spock"]}


class Choice:

    def __init__(self, items: dict):
        self.items = items

    def ask_choice(self) -> str:
        while True:
            choice = input("Your choice (rock paper scissors lizard spock)?: ")
            if choice not in self.items.keys():
                print("Invalid input")
            else:
                break
        return choice

    def random_choice(self) -> str:
        return random.choice(list(self.items.keys()))


def find_winner(player: str, computer: str, items_dict: dict) -> str:
    if computer in items_dict[player]:
        return "Player wins!"
    elif computer == player:
        return "Tie!"
    else:
        return "Computer wins!"


if __name__ == '__main__':

    player = Choice(ITEMS)  # ?

    game = True
    while game:

        # ask player his choice
        player_choice = player.ask_choice()  # ?
        print("Players:", player_choice)

        # make random computer choice
        computer_choice = Choice(ITEMS).random_choice()  # ?
        print("Computer:", computer_choice)

        # find and print winner
        print(find_winner(player_choice, computer_choice, ITEMS))

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
