"""
    查找单词
"""

word = input(":")

f = open("dict.txt")
while True:
    re_list = f.readline()
    w = re_list.split(" ")[0]
    if w > word:
        print("No Found")
        break
    elif word == w:
        print(re_list)
        break

f.close()