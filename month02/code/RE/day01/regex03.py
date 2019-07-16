"""
    match 对象的属性方法
"""

import re

pattern = r"(ab)cd(?P<pig>ef)"

regex = re.compile(pattern)

obj = regex.search('abcdefghi')

# 属性变量
print(obj.pos)  # 匹配目标字符串的开始位置
print(obj.endpos)  # 匹配目标字符串的结束位置
print(obj.re)  # 正则表达式
print(obj.string)  # 目标字符串
print(obj.lastgroup)  # 最后一组组名
print(obj.lastindex)  # 最后一组序号

print("\n=======================================\n")

# 属性方法
print(obj.span())  # 获取匹配内容的起止位置
print(obj.start())  # 获取匹配内容的开始位置
print(obj.end())  # 获取匹配内容的结束位置
print(obj.groupdict())  # 获取捕获组字典，组名为键，对应内容为值
print(obj.groups())  # 获取子组对应内容

print(obj.group())  # 获取match对象匹配内容，默认参数为 0
print(obj.group(1))  # 获取第一个子组的内容
print(obj.group(2))  # 获取第二个子组的内容
print(obj.group('pig'))  # 获取 name 为 pig 的子组的内容

