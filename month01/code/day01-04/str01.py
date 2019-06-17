"""
    str 字面值
    转义符 \n \t
"""
# str01 = "我是\"苏打强\""
# str02 = "我是\n苏打强"
# str03 = "我是\t苏打强"
# str04 = "C:\\nmt\\home\\anaconda\\python"  # 转义符 \
# str05 = r"C:\nmt\home\anaconda\python"  # 原始字符串
# print(str01)
# print(str02)
# print(str03)
# print(str04)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# """
#    字符串格式化
# """
# a, b = 1, 2
# str01 = "%d+%d=%d" % (a, b, a + b)
# str02 = "%s+%.2f=1.5" % ('1', 0.5)
# print(str01)
# print(str02)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
获取一个字符串，打印第一个字符，最后一个字符，倒数第三个字符
打印前两个字符，倒序打印字符，
如果字符串长度是奇数，打印中间字符
"""
# input_str = input("输入一个字符串:")
# print(input_str[0])
# print(input_str[-1])
# print(input_str[-3])
# print(input_str[:2])
# print(input_str[::-1])
# length_str = len(input_str)
# if length_str % 2 != 0:
#     print(input_str[length_str//2])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
(扩展)一个小球从１００ｍ的高度落下
    　　每次弹回原高度的一半．
    　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
            总共走了多少米
"""
# height = 100
# distance = 100
# count = 0
# # 判断能弹起来的高度
# while height/2 >= 0.01:
#     # 弹起
#     count += 1
#     distance += height  # 总距离加上一起一落
#     height /= 2  # 下一次能弹起的高度变为一半
# print("总共弹起%d次，总共走了%.2f米" % (count, distance))