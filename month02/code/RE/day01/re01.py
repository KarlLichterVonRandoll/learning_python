"""
    1. 匹配一个 .com邮箱格式字符串串
    2. 匹配一个密码 8-12 位数字字母下划线构成
    3. 匹配一个数字 正数，负数，整数，小数 分数 百分数
    4. 匹配一段文字中以大写字母开头的单词，注意文字中可能有 iPython(不算) H-base(算)
       单词可能有 大写字母 小写字母 - _
"""

import re

re01 = r"\w+@\w+.com"
list01 = re.findall(re01, "sa@sdjjk.com .com")
print(list01)

re02 = r"\b[a-zA-Z0-9_]{8,12}\b"
list02 = re.findall(re02, "54555_hGG 哈哈526452 563_lkhjjH55454")
print(list02)

re03 = r"[-.%/0-9]+"
re05 = r"-?\d+\/?\.?\d*%?"
list03 = re.findall(re05, "dj 9 90% 1/2 0.4 -0.4 99")
print(list03)

re04 = r"\b[A-Z]+[a-zA-z_-]*"
list04 = re.findall(re04, "iPython H-base Git_hub Keras")
print(list04)
