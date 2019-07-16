"""
    利用 memoryview 精准地修改了一个数组的某个字节来更新数组里某个元素的值
"""
import array

# 使用 'h', 这个数组的元素是 16 位二进制有符号整数。
numbers = array.array('h', [-2, -1, 0, 1, 2])

# 利用含有 5 个短整型有符号整数的数组(类型码是 'h')创建一个memoryview。
memv = memoryview(numbers)
print(len(memv))

# memv 里的 5 个元素跟数组里的没有区别。
print(memv[0])

# 创建一个 memv_oct,这一次是把 memv 里的内容转换成 'B' 类型,也就是无符号字符。
memv_oct = memv.cast('B')

# 以列表的形式查看 memv_oct 的内容。
print(memv_oct.tolist())

# 把位于位置 5 的字节赋值成 4。
memv_oct[5] = 4

print(numbers)
