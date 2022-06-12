logs = {"qwe": "123"}


def third():
    pass


def login(name: str) -> bool:
    return name in logs


def check_password(name: str, pas: str) -> bool:
    return logs.get(name) == pas


if __name__ == '__main__':

    counter = 3
    while counter >= 1:

        print(f"You have {counter} attempts.")

        username = input("Username: ")
        password = input("Password: ")

        log = login(username)
        check = check_password(username, password)

        if check and log is True:
            print("You are in the system!")
            break
        else:
            print("Login or password is wrong.")
            counter -= 1
