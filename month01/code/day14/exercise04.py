from module01 import *

# 在二维列表中，获取13位置，向左，3个元素
re01 = DoubleListHelper.get_elements(list01, Vector2(1, 3), Vector2.left(), 3)
print(re01)
# 在二维列表中，获取22位置，向上，2个元素
re02 = DoubleListHelper.get_elements(list01, Vector2(2, 2), Vector2.up(), 2)
print(re02)
# 在二维列表中，获取03位置，向下，2个元素
re03 = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
print(re03)
