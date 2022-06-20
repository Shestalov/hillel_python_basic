import argparse
import datetime

logs = {"qwe": "123", 'time': datetime.datetime(2022, 6, 20, 23, 25, 0, 153718)}


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, help='username')
    parser.add_argument('-p', '--password', type=str, help='password')
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
    return True


def check_password(name: str, pas: str) -> bool:
    return logs.get(name) == pas


def block() -> bool:
    if datetime.datetime.now() > logs["time"] + datetime.timedelta(seconds=60):
        return True
    else:
        print("You are blocked! Try after ", (logs["time"] + datetime.timedelta(seconds=60)).strftime("%H:%M:%S"))
        return False


if __name__ == '__main__':

    while True:

        if not block():
            break

        else:
            counter = 4

            username = parse().username or input("Username: ")
            password = parse().password or input("Password: ")

            while counter > 1:

                if login(username, password) is True:
                    print("You are in the system!")
                    break

                elif login(username, password) is False:
                    print("Login or password is WRONG.")
                    counter -= 1
                    print(f"You have {counter} attempts.")

                    if parse().username is None:
                        username = input("Username: ")

                    if parse().password is None:
                        password = input("Password: ")

                    else:
                        username = input("Username: ")
                        password = input("Password: ")

            else:
                print("Attempts expired")
                print("You are blocked for 5 min.")
                # logs["time"] = datetime.datetime.now()

        break
