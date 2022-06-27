import argparse
import datetime

logs = {"qwe": "123", 'time': "2022-06-28 19:10:00:997317"}


class UserDoesNotExist(Exception):
    pass


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, help='username')
    parser.add_argument('-p', '--password', type=str, help='password')
    return parser.parse_args()


def decorator(func):
    def wrapper(user_name: str, user_password: str, time_now: str) -> bool:

        try:
            if not check_password(user_name, user_password):
                print("Wrong password")
                return False
        except UserDoesNotExist as a:
            print(a)
            return False

        if not is_block(time_now):
            print("Wrong time")
            return False

        return func(user_name, user_password, time_now)

    return wrapper


@decorator
def login(user_name: str, user_password: str, time_now: str) -> bool:
    return True


def check_password(user_name: str, user_password: str) -> bool:
    if user_name not in logs:
        raise UserDoesNotExist("Wrong User Name")
    else:
        return logs.get(user_name) == user_password


def is_block(time_now: str) -> bool:
    last_time = logs["time"]
    return last_time > time_now


if __name__ == '__main__':

    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

    counter = 4

    username = parse().username or input("Username: ")
    password = parse().password or input("Password: ")

    while counter >= 1:

        if login(username, password, now_time) is True:
            print("You are in the system!")
            break

        else:
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
