import argparse

logs = {"qwe": "123"}


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
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

        print(f"You have {counter} attempts.")

        args = parse()

        # if username and password come from terminal
        if args:
            log = login(args.username, args.password)
            if log is True:
                print("You are in the system!")
                break
            # if username and password wrong from terminal
            else:
                username = input("Username: ")
                password = input("Password: ")

                log = login(username, password)

                if log is True:
                    print("You are in the system!")
                    break
                else:
                    print("Login or password is wrong.")
                    counter -= 1
        # if username wrong
        elif args.password:
            username = input("Username: ")
            log = login(username, args.password)
            if log is True:
                print("You are in the system!")
                break
            else:
                counter -= 1
        # if password wrong
        elif args.username:
            password = input("Password: ")
            log = login(args.username, password)
            if log is True:
                print("You are in the system!")
                break
            else:
                counter -= 1
        # if run
        else:
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
