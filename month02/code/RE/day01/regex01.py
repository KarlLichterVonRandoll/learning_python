"""
    re 模块 功能函数演示
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"(\w+):(\d+)"  # 正则表达式

# re 模块调用 findall
l = re.findall(pattern, s)
print(l)

# compile 对象调用 findall
regex = re.compile(pattern)
l = regex.findall(s, 0, 12)
print(l)

# 按照正则表达式匹配内容切割字符串
l = re.split(r"[:,]", s)
print(l)

# 使用一个字符串替换正则表达式匹配到的内容
l = re.sub(r":", "-", s)
print(l)

# 返回一元组，替换后的字符串和替换了几处
l = re.subn(r":", "-", s)
print(l)

