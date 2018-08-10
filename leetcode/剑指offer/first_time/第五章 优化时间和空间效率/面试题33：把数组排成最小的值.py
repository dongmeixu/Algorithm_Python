"""
题目描述

    输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一
    个。例如输入数组 {3，32，321}，则打印出这三个数字能排成的最小数字为 321323。
"""

"""
解题思路：
可以看成是一个排序问题，在比较两个字符串 S1 和 S2 的大小时，
应该比较的是 S1+S2 和 S2+S1 的大小，
如果 S1+S2 < S2+S1，那么应该把 S1 排在前面，否则应该把 S2 排在前面。
"""

"""python3没通过"""

# -*- coding:utf-8 -*-
class Solution:
    def compare(self, x, y):
        if x >= y:
            return x - y, 1
        else:
            return y - x, -1

    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""

        numbers = [str(num) for num in numbers]
        # print(numbers)
        # py3引入模块实现cmp
        from functools import cmp_to_key
        cmp2key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))

        numbers = sorted(numbers, key=cmp2key)
        return "".join(numbers).lstrip('0') or '0'


numbers = [3, 32, 321]
print(Solution().PrintMinNumber(numbers))
