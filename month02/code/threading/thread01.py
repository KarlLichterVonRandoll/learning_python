import threading
import time


def t1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")


def t2_job():
    print("T2 start\n")
    print("T2 finish\n")


def main():
    thread01 = threading.Thread(target=t1_job, name="T1")
    thread02 = threading.Thread(target=t2_job, name="T2")
    thread01.start()
    thread02.start()
    thread01.join()
    thread02.join()
    print("all done\n")
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


if __name__ == "__main__":
    main()
