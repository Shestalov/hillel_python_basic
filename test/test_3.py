import json
import datetime

def read_logs(file_name: str) -> str:
    try:
        with open(file_name) as f:
            return json.load(f)
    except OSError as e:
        return str(e)

def check_password(user_name: str, user_password: str, log: dict) -> bool:
    if user_name not in log:
        return False
    else:
        return log.get(user_name)["password"] == user_password

def is_block(time_now: str, user_name: str, log: dict) -> bool:
    return time_now > log.get(user_name)["time"]

now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")

logs = dict(read_logs("logs_test.json"))

res = check_password("qwe", "123", logs)
# print(res)

block = is_block(now_time, "qwe", logs)
# print(block)

new_password = "12345"
new_username = "qwerty"
new_time = now_time

logs[new_username] = {"password": new_password, "time": now_time}
print(logs)

