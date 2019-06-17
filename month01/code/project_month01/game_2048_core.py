"""
    2048 游戏核心算法
"""


# 1. 零元素移至末尾
#    [2,0,2,0] --> [2,2,0,0]
#    [2,0,0,2] --> [2,2,0,0]
#    [2,4,0,2] --> [2,4,2,0]

def zero_to_end(num_list):
    """
        零元素移动到末尾
    """
    # 从后向前，如果发现零元素，删除并在末尾追加 0
    for i in range(-1, -len(num_list) - 1, -1):
        if num_list[i] == 0:
            del num_list[i]
            num_list.append(0)


# 测试代码......
# list01 = [2,0,2,0]
# zero_to_end(list01)
# print(list01)


# 2. 将相同数字合并
#    [2,0,2,0] --> [4,0,0,0]
#    [2,0,0,2] --> [4,0,0,0]
#    [2,2,2,2] --> [4,4,0,0]

def merge(num_list):
    """
    合并
    """
    # 先将中间的零元素一直末尾，在合并相同元素
    zero_to_end(num_list)
    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            # 将后一个累加前一个之上
            num_list[i] *= 2
            del num_list[i + 1]
            num_list.append(0)


# 测试代码......
# list02 = [2,0,2,0]
# merge(list02)
# print(list02)


# 3. 地图向左移动
map01 = [
    [2, 8, 2, 2],
    [4, 4, 2, 2],
    [2, 4, 2, 2],
    [4, 0, 2, 2]
]


def move_left(map_list):
    for i in range(len(map_list)):
        # 合并
        merge(map_list[i])


# 测试代码......
# move_left(map01)
# for i in map01:
#     print(i)
# print("++++++++++++++++++++++++++++")

# 地图向右移动
def move_right(map_list):
    for i in range(len(map_list)):
        # 从右向左取出数据形成新列表
        map_list[i] = map_list[i][::-1]
        # 合并
        merge(map_list[i])
        # 从右向左接受合并后的数据
        map_list[i] = map_list[i][::-1]


# 测试代码......
# move_right(map01)
# for i in map01:
#     print(i)

# 矩阵转置
def square_matrix_transpose(map_list):
    for i in range(len(map_list)):
        for j in range(i + 1, len(map_list)):
            map_list[i][j], map_list[j][i] = map_list[j][i], map_list[i][j]


# 4. 上移、下移
# 上移
def move_up(map_list):
    square_matrix_transpose(map_list)
    move_left(map_list)
    square_matrix_transpose(map_list)


# 下移
def move_down(map_list):
    square_matrix_transpose(map_list)
    move_right(map_list)
    square_matrix_transpose(map_list)


# 测试代码......
# move_up(map01)
# for item in map01:
#     print(item)
#
# print("++++++++++++++++++++++++++++++")
#
# move_down(map01)
# for item in map01:
#     print(item)


