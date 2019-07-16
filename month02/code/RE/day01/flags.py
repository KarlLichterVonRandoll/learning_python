"""
    flags 扩展功能演示
"""

import re

s = """Hello
北京
"""

# 元字符只能匹配ascii码
regex = re.compile(r'\w+', flags=re.ASCII)

l = regex.findall(s)
print(l)

# 匹配忽略字母的大小写
regex = re.compile(r'[A-Z]+', flags=re.IGNORECASE)

l = regex.findall(s)
print(l)

# 使 . 能匹配换行
regex = re.compile(r'.+', flags=re.DOTALL)

l = regex.findall(s)
print(l)

# 使 ^  $可以匹配每一行的开头结尾位置
regex = re.compile(r'^北京', flags=re.MULTILINE)

l = regex.findall(s)
print(l)

# 为正则添加注释
pattern = r"""\w+  # Hello
\s+  # 匹配换行
\w+  # 北京
"""
regex = re.compile(pattern, flags=re.VERBOSE)

l = regex.findall(s)
print(l)
