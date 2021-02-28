#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    只出现一次的数字
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x21ib6/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        使用异或运算，将所有值进行异或
异或运算，相异为真，相同为假，所以 a^a = 0 ;0^a = a
因为异或运算 满足交换律 a^b^a = a^a^b = b 所以数组经过异或运算，单独的值就剩下了
执行用时：
40 ms
, 在所有 Python3 提交中击败了
96.61%
的用户
内存消耗：
16.6 MB
, 在所有 Python3 提交中击败了
13.46%
的用户
        :param nums:
        :return:
        """
        res = 0
        for num in nums:
            res = res ^ num
        return res

    def singleNumber1(self, nums: List[int]) -> int:
        """执行用时：
52 ms
, 在所有 Python3 提交中击败了
58.11%
的用户
内存消耗：
16.6 MB
, 在所有 Python3 提交中击败了
23.73%
的用户"""
        return sum(set(nums)) * 2 - sum(nums)


if __name__ == '__main__':
    nums = [1, 2]
    solution = Solution()
    print(solution.singleNumber(nums))
    pass
