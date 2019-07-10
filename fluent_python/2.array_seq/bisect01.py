import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fuc):
    for needle in reversed(NEEDLES):
        position = bisect_fuc(HAYSTACK, needle)  # 用特定的 bisect 函数来计算元素应该出现的位置。
        offset = position * '  |'  # 利用该位置来算出需要几个分隔符号。
        print(ROW_FMT.format(needle, position, offset))  # 把元素和其应该出现的位置打印出来。


if __name__ == '__main__':

    if sys.argv[-1] == 'left':  # 根据命令上最后一个参数来选用 bisect 函数。
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # 把选定的函数在抬头打印出来。
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)
