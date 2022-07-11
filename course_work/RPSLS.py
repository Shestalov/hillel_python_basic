import random

ITEMS = {"rock": ["lizard", "scissors"],
         "lizard": ["paper", "spock"],
         "spock": ["scissors", "rock"],
         "scissors": ["lizard", "paper"],
         "paper": ["rock", "spock"]}


def ask_player_choice(items_dict: dict) -> str:
    while True:
        player = input("Your choice (rock paper scissors lizard spock)?: ")
        if player not in items_dict.keys():
            print("Invalid input")
        else:
            break
    return player


def random_choice(items_dict: dict) -> str:
    return random.choice(list(items_dict.keys()))


def find_winner(player: str, computer: str, items_dict: dict) -> str:
    if computer in items_dict[player]:
        return "Player wins!"
    elif computer == player:
        return "Tie!"
    else:
        return "Computer wins!"


if __name__ == '__main__':

    game = True
    while game:

        # ask player his choice
        player_choice = ask_player_choice(ITEMS)
        print("Players:", player_choice)

        # make random computer choice
        computer_choice = random_choice(ITEMS)
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
