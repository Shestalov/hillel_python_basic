import argparse
import datetime
import json


class UserDoesNotExist(Exception):
    pass


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, help='username')
    parser.add_argument('-p', '--password', type=str, help='password')
    return parser.parse_args()


def decorator(func):
    def wrapper(user_name: str, user_password: str, time_now: str, log: dict) -> bool:

        try:
            if not check_password(user_name, user_password, log):
                print("Wrong password")
                return False
        except UserDoesNotExist as a:
            print(a)
            return False

        if not is_block(time_now, log):
            print("YOU are blocked, try after: ", log["time"])
            return False

        return func(user_name, user_password, time_now, log)

    return wrapper


@decorator
def login(user_name: str, user_password: str, time_now: str, log: dict) -> bool:
    return True


def check_password(user_name: str, user_password: str, log: dict) -> bool:
    if user_name not in log:
        raise UserDoesNotExist("Wrong User Name")
    else:
        return log.get(user_name) == user_password


def is_block(time_now: str, log: dict) -> bool:
    return time_now > log["time"]


def read_logs(file_name: str) -> dict:
    try:
        with open(file_name) as f:
            return json.load(f)
    except OSError as e:
        ...


def rewrite_logs(file_name: str, data: dict):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
    except OSError as e:
        ...


if __name__ == '__main__':

    logs = read_logs("logs.json")

    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

    counter = 4

    username = parse().username or input("Username: ")
    password = parse().password or input("Password: ")

    while counter >= 1:

        counter -= 1

        if login(username, password, now_time, logs) is True:
            print("You are in the system!")
            break

        if counter < 1:
            continue

        else:
            print(f"You have {counter} attempts.")

            if parse().username is None:
                username = input("Username: ")

            if parse().password is None:
                password = input("Password: ")

    else:
        logs["time"] = (datetime.datetime.now() + datetime.timedelta(seconds=60 * 5)).strftime("%Y-%m-%d %H:%M:%S:%f")
        next_time = logs["time"]
        rewrite_logs("logs.json", logs)

        print("Attempts expired")
        print("You are blocked for 5 min. Try after", logs["time"])
