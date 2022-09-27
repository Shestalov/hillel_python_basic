import random

ITEMS = {"rock": ["lizard", "scissors"],
         "lizard": ["paper", "spock"],
         "spock": ["scissors", "rock"],
         "scissors": ["lizard", "paper"],
         "paper": ["rock", "spock"]}


class Player:

    def __init__(self):
        self._manual_choice = None
        self._random_choice = None
        self._result = None

    def manual_choice(self):
        while True:
            self._manual_choice = input("Your choice (rock paper scissors lizard spock)?: ")
            if self._manual_choice not in ITEMS.keys():
                print("Invalid input")
            else:
                break
        return self._manual_choice


    def random_choice(self):
        self._random_choice = random.choice(list(ITEMS.keys()))
        return self._random_choice

    def find_winner(self):
        if self._random_choice in ITEMS[self._manual_choice]:
            self._result = "Player wins!"
        elif self._random_choice == self._manual_choice:
            self._result = "Tie!"
        else:
            self._result = "Computer wins!"

    def run(self):

        game = True
        while game:

            # ask player his choice
            self.manual_choice()
            print("Player: ", self._manual_choice)

            # make random computer choice
            self.random_choice()
            print("Computer:", self._random_choice)

            # find and print winner
            self.find_winner()
            print(self._result)

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


if __name__ == '__main__':
    Player().run()
