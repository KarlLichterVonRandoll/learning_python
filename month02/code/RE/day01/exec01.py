"""
编写接口函数，从终端输入端口名称获取端口运行状态中的
地址值

思路分析：
1. 根据输入的端口名称找到对应的段落
2. 在该段落中匹配address
"""

import re


def get_addr():
    pos = input("输入端口:")

    f = open('exc.txt')
    while True:
        data = ""
        for line in f:
            if line == "\n":
                break
            data += line

        if not data:
            break

        obj = re.match(pos, data)

        if obj:
            # pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            pattern = r"(\d{1,3}\.){3}\d{1,3}/\d|Unknown"
            l = re.search(pattern, data)
            return l.group()
    return "没有这个端口"


if __name__ == "__main__":
    print(get_addr())
