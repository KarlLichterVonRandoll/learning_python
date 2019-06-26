"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item
        return None

    @staticmethod
    def get_count(list_target, func_duration):
        """
               通用的计算满足某个条件的元素数量方法
           :param list_target: 需要查找的列表
           :param func_duration: 需要查找的条件,函数类型
                   函数名(参数) --> bool
           :return: 满足条件元素的数量
        """
        count_value = 0
        for item in list_target:
            if func_duration(item):
                count_value += 1
        return count_value

    @staticmethod
    def is_exists(list_target, func_duration):
        """
            判断指定条件的对象是否存在
        :param list_target: 需要查找的列表
        :param func_duration: 需要查找的条件,函数类型
        :return: 是否存在 bool
        """
        for item in list_target:
            if func_duration(item):
                return True
        return False

    @staticmethod
    def get_sum(list_target, func_duration):
        """
            通用的求和方法
        :param list_target: 需要查找的列表
        :param func_duration:  需要查找的条件,函数类型
        :return:  总和
        """
        summation = 0
        for item in list_target:
            summation += func_duration(item)
        return summation

    @staticmethod
    def select(list_target, func_duration):
        """
            通用筛选操作
        :param list_target: 需要查找的列表
        :param func_duration: 需要查找的条件,函数类型
        :return: 需要的元素，生成器类型
        """
        for item in list_target:
            yield func_duration(item)

    @staticmethod
    def get_max(list_target, func_duration):
        """
            通用获取最大值
        :param list_target: 需要查找的列表
        :param func_duration: 需要查找的条件,函数类型
        :return: 最大值
        """
        return max(list_target, key=func_duration)

    @staticmethod
    def get_min(list_target, func_duration):
        """
            通用获取最小值
        :param list_target: 需要查找的列表
        :param func_duration: 需要查找的条件,函数类型
        :return: 最小值
        """
        return min(list_target, key=func_duration)

    @staticmethod
    def order_by_up(list_target, func_duration):
        """
            通用升序排序方法
        :param list_target:  需要查找的列表
        :param func_duration:  需要查找的条件,函数类型
        :return:  排序后的结果，列表
        """
        list_target.sort(key=func_duration)

    @staticmethod
    def order_by_down(list_target, func_duration):
        """
            通用降序排序方法
        :param list_target:  需要查找的列表
        :param func_duration:  需要查找的条件,函数类型
        :return:  None
        """
        list_target.sort(key=func_duration)

    @staticmethod
    def remove_enemy(list_target, func_duration):
        """
            通用删除方法
        :param list_target:  需要查找的列表
        :param func_duration: 需要查找的条件,函数类型
        :return: None
        """
        for i in range(len(list_target) - 1, -1, -1):
            if func_duration(list_target[i]):
                del list_target[i]
