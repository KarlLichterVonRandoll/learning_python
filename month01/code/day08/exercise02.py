# str01 = r"  校  训：自 强不息、厚德载物。   "
#
# # 查找空格的数量
# print(str01.count(" "))
# # 删除字符串前后空格
# print(str01.strip())
# # 删除字符串所有空格
# print(str01.replace(" ", ""))
# # 查找"载物"的位置
# print(str01.find("载物"))
# # 判断字符串是否以"校训"开头.
# print(str01.startswith("校训"))

"""
    定义函数查找指定范围内的素数
"""
import math


def get_prime_number(begin, end):
    """
        查找指定范围内的素数
    :param begin: 起始值 int
    :param end: 结束值 int
    :return:  素数组成的列表 list
    """
    list01 = []
    is_prime(begin, end, list01)
    return list01


def is_prime(begin, end, list01):
    for num in range(begin, end + 1):
        if num == 1:
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            list01.append(num)
    return list01


result = get_prime_number(1, 100)
print(result)
