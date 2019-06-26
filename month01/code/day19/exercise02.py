"""
    装饰器练习
    在不改变原有功能的定义与调用情况下，
    增加验证账号的功能。
"""


def verify_account(func):
    def wrapper(*args, **kwargs):
        print("验证账号")
        func(*args, **kwargs)

    return wrapper


@verify_account
def deposit(money):
    print("存了%d钱" % money)


@verify_account
def withdraw(login_id, pwd):
    print("取钱了", login_id, pwd)


# deposit(10000)
# withdraw('abc', 123456)


"""
    增加新功能，打印函数执行时间
"""
import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        time01 = time.time()
        func(*args, **kwargs)
        time02 = time.time()
        print(time02 - time01, "s")

    return wrapper


@calculate_time
def func01():
    time.sleep(1)
    print("func02执行完毕")


@calculate_time
def func02(a):
    time.sleep(2)
    print("func02执行完毕，参数是", a)


func01()
func02(200)
