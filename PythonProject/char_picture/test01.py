import argparse

# 构建命令行输入参数处理对象
parser = argparse.ArgumentParser()

# 添加描述信息，当输入 python3 test01.py --help  就会出现
parser.description = "给两个数，计算两个数的积"

# 添加参数
parser.add_argument('--verbose', help="echo the string you use here", action="store_true")
parser.add_argument("--PartA", help="我是A", type=int)
parser.add_argument("--PartB", help="我是B", type=int)

# 解析并获取参数
args = parser.parse_args()

if args.verbose:
    print("morning")
# print("A=", args.PartA)
# print("B=", args.PartB)
# print("积是", args.PartA * args.PartB)

