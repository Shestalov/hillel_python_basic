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

        if not is_block(time_now, user_name, log):
            print("YOU are blocked, try after: ", log.get(user_name)["time"])
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
        return log.get(user_name)["password"] == user_password


def is_block(time_now: str, user_name: str, log: dict) -> bool:
    try:
        return time_now > log.get(user_name)["time"]
    except TypeError:
        return True


def read_logs(file_name: str) -> dict:
    try:
        with open(file_name) as f:
            return json.load(f)
    except OSError as e:
        print(e)
        return {}


def rewrite_logs(file_name: str, log: dict) -> dict:
    try:
        with open(file_name, "w") as f:
            json.dump(log, f)
        return log
    except OSError as e:
        print(e)
        return {}


def registration_name(log: dict) -> str:
    while True:
        user_name = input("New Username: ")
        if user_name not in log:
            break
        else:
            print("This name is already exist! Try again!")
    return user_name


def registration_password() -> str:
    user_password = input("New Password: ")
    return user_password


def append_new_user_in_logs(log: dict, new_user: str, new_pass: str) -> dict:
    log[new_user] = {"password": new_pass, "time": None}
    return log


def add_five_min(log: dict, user_name: str, time_now: str) -> dict:
    log[user_name]["time"] = (datetime.datetime.strptime(time_now, "%Y-%m-%d %H:%M:%S:%f") +
                              datetime.timedelta(seconds=60 * 5)).strftime("%Y-%m-%d %H:%M:%S:%f")
    return log


if __name__ == "__main__":

    logs = read_logs("logs.json")
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

    while True:

        asking = input("Press [1] for Login or press [2] for Sign up?: ")

        if asking == "2":
            new_username = registration_name(logs)
            new_password = registration_password()
            append_new_user_in_logs(logs, new_username, new_password)
            logs = rewrite_logs("logs.json", logs)
            break  # or continue

        elif asking == "1":

            username = parse().username or input("Username: ")
            password = parse().password or input("Password: ")

            counter = 4
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
                print("Attempts expired")

                if username in logs:
                    add_five_min(logs, username, now_time)
                    rewrite_logs("logs.json", logs)
                    print("You are blocked for 5 min. Try after", logs.get(username)["time"])
                else:
                    print("Username not found! Try again!")
                    continue

            break
