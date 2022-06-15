import argparse

logs = {"qwe": "123"}


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--password')
    return parser.parse_args()

def decorator(func):
    def wrapper(name: str, pas: str) -> bool:
        if check_password(name, pas):
            return func(name, pas)
        else:
            return False

    return wrapper


@decorator
def login(name: str, pas: str) -> bool:
    return True  # name in logs


def check_password(name: str, pas: str) -> bool:
    return logs.get(name) == pas


if __name__ == '__main__':

    counter = 3
    while counter >= 1:

        args = parse()
        if login(args.username, args.password):
            log = login(args.username, args.password)
        elif args.username:
            print(f"You have {counter} attempts.")
            password = input("Password: ")
            log = login(args.username, password)
        elif args.password:
            print(f"You have {counter} attempts.")
            username = input("Username: ")
            log = login(username, args.password)
        else:
            print(f"You have {counter} attempts.")
            username = input("Username: ")
            password = input("Password: ")
            log = login(username, password)

        if log is True:
            print("You are in the system!")
            break
        else:
            print("Login or password is wrong.")
            counter -= 1
    else:
        print("Attempts expired")
