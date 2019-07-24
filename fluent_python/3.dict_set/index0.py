"""创建一个从单词到其出现情况的映射"""
import re

WORD_RE = re.compile(r'\w+')
index = {}
with open("zen.txt", encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现,这样写只是为了证明论点
            occurrences = index.get(word, [])
            occurrences.append(location)

            index[word] = occurrences

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])
