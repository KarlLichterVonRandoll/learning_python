import redis
from multiprocessing import Process
import random
import time


# 一个进程负责生产url, 一个进程负责消费url
class Spider:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0, password='123456')

    def product(self):
        for i in range(67):
            url = 'http://app.mi.com/category/2#page=%s' % str(i)
            self.r.rpush('spider:urls', url)
            time.sleep(random.randint(1, 3))

    def consumer(self):
        while True:
            url = self.r.brpop('spider:urls', 5)
            if url:
                print("正在抓取 ", url[1].decode())
            else:
                print("抓取结束")
                break

    def run(self):
        p1 = Process(target=self.product)
        p2 = Process(target=self.consumer)
        p1.start()
        p2.start()
        p1.join()
        p2.join()


if __name__ == "__main__":
    spider = Spider()
    spider.run()
