#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/1

"""
文件说明：
    加一
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
"""
from typing import List


class Solution:
    def plusOne1(self, digits: List[int]) -> List[int]:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
57.89%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
21.62%
的用户
        :param digits:
        :return:
        """
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            str_s = str()
            result = []
            for i in range(len(digits)):
                str_s += str(digits[i])
            for i in str((int(str_s) + 1)):
                result.append(int(i))
            return result

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        执行用时：
24 ms
, 在所有 Python3 提交中击败了
99.67%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
71.36%
的用户
        :param digits:
        :return:
        """
        index = len(digits)
        if index == 0:
            return digits
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        while index > 0:
            index -= 1
            if digits[index] != 9:
                digits[index] = digits[index] + 1
                return digits
            else:
                digits[index] = 0
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

    def plusOne1(self, digits: List[int]) -> List[int]:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
11.57%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
32.47%
的用户
        :param digits:
        :return:
        """
        index = len(digits)
        if index==0:
            return digits
        flag = 1
        while index > 0:
            index -= 1
            digits[index] = digits[index] + flag
            flag = 0
            if digits[index] >= 10:
                flag = 1
                digits[index] = digits[index] - 10
            else:
                break
        if flag:
            digits.insert(0, 1)
        return digits



if __name__ == '__main__':
    nums = [1,9,9]
    solution = Solution()
    print(solution.plusOne(nums))
    pass
