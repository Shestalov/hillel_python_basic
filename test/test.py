import argparse
import datetime

logs = {"qwe": "123", 'time': "2022-06-21 21:00:00:997317"}


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, help='username')
    parser.add_argument('-p', '--password', type=str, help='password')
    return parser.parse_args()


def decorator(func):
    def wrapper(user_name: str, user_password: str) -> bool:
        if check_password(user_name, user_password):
            return func(user_name, user_password) #func(*args, **kwargs)
        else:
            return False

    return wrapper


@decorator
def login(user_name: str, user_password: str) -> bool: #*args, **kwargs
    return True


def check_password(user_name: str, user_password: str) -> bool:
    return logs.get(user_name) == user_password


def block(now: str, last: str) -> bool:
    if datetime.datetime.strptime(now, "%Y-%m-%d %H:%M:%S:%f") > \
            (datetime.datetime.strptime(last, "%Y-%m-%d %H:%M:%S:%f") + datetime.timedelta(seconds=60 * 5)):
        return False
    else:
        print("You are blocked! Try after ",
              datetime.datetime.strptime(last, "%Y-%m-%d %H:%M:%S:%f") + datetime.timedelta(seconds=60 * 5))
        return True


if __name__ == '__main__':

    while True:

        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")
        last_time = logs["time"]

        if block(now_time, last_time) is True:
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

        break
