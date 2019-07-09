"""
    死锁
"""

from threading import Thread, Lock
import time


# 交易类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id
        self.balance = balance
        self.lock = lock

    # 取钱
    def get(self, value):
        self.balance -= value

    # 存钱
    def add(self, value):
        self.balance += value

    # 查看余额
    def search(self):
        return self.balance


# 产生两个账户
tom = Account('Tom', 5000, Lock())
alex = Account("Alex", 10000, Lock())


# 转账过程
def transfer(from_, to_, money):
    if from_.lock.acquire():  # 锁住子集账户
        from_.get(money)
        time.sleep(0.5)
        if to_.lock.acquire():  # 对方账户上锁
            to_.add(money)
            to_.lock.release()
        from_.lock.release()

    print("%s给%s转账完成"%(from_.id, to_.id))


t1 = Thread(target=transfer, args=(tom, alex, 2000))
t2 = Thread(target=transfer, args=(alex, tom, 2000))
t1.start()
t2.start()
t1.join()
t2.join()
