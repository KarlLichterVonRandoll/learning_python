"""
    re 模块功能演示2
    生成 match 对象的函数
"""

import re

s = "今年是2019年,建国70周年"

pattern = r"\d+"

# 根据正则表达式匹配目标字符串内容, 返回匹配结果的迭代器
it = re.finditer(pattern, s)
for i in it:
    print(i.group())  # 获取 match 对象的内容

# 完全匹配某个目标字符串
m = re.fullmatch(r'[,\w]+', s)
print(m.group())

# 匹配起始位置
m = re.match(r'\w+?', s)
print(m.group())

# 匹配目标字符串第一个符合内容
m = re.search(r"\d+", s)
print(m.group())

