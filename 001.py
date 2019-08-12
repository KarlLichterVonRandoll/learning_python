# dict01 = {}
# with open("names.txt") as f:
#     names = f.readlines()
#     for name in names:
#         if name.startswith("欧阳"):
#             first_name = name[:2]
#         else:
#             first_name = name[0]
#         if first_name in dict01:
#             dict01[first_name] += 1
#         else:
#             dict01[first_name] = 1
#
# for k, v in dict01.items():
#     print('"%s"姓出现了%d次' % (k, v))

# list01 = []
# with open("numbers.txt") as f:
#     numbers = f.readlines()
#     for number in numbers:
#         str_ = " "
#         for n in number:
#             if n in str_:
#                 continue
#             str_ += n
#         list01.append(int(str_.strip()))
#
# for i in sorted(list01, reverse=True):
#     print(i)


str01 = input("输入：")
list01 = []
list02 = []
for i in range(len(str01)):
    if str01[i] == "(":
        list01.append(i)
    elif str01[i] == ")":
        if len(list01) == 0:
            print("不合法")
            break
        else:
            n = list01.pop()
            list02.append((n, i))
else:
    if len(list01):
        print("不合法")
    else:
        for j in range(len(list02)):
            print(str01[list02[j][0]:list02[j][1]+1])


# (5*(9+6*(2-30)-(10/2))-4)*8
