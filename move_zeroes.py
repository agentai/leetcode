#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/1

"""
文件说明：
    移动零
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2ba4i/
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
90.63%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
44.04%
的用户
        :param nums:
        :return:
        """
        start = end = 0
        len_nums = len(nums)
        while start < len_nums and nums[start] != 0:
            start += 1
            end += 1
        while start < len_nums:
            while end < len_nums and nums[end] == 0:
                end += 1
            if end == len_nums:
                break
            nums[start] = nums[end]
            start += 1
            end += 1
        while start < len(nums):
            nums[start] = 0
            start += 1
        return nums

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
77.26%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
6.02%
的用户
        :param nums:
        :return:
        """
        fast = slow = 0
        while fast < len(nums):
            while slow < len(nums) and nums[slow] != 0:
                slow += 1
                fast += 1
            if fast < len(nums) and nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        print(nums)

    def moveZeroes1(self, nums: List[int]) -> None:
        """执行用时：
368 ms
, 在所有 Python3 提交中击败了
5.54%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
44.04%
的用户"""
        if len(nums) == 0:
            return
        len_nums = len(nums)-1
        start = 0
        while start < len_nums:
            while start < len_nums and nums[start] != 0:
                start += 1
            index = start
            while index < len_nums and nums[index] == 0:
                index += 1
            if index == len_nums and nums[index] == 0:
                break
            if index > start:
                nums[start] = nums[index]
                nums[index] = 0
                start += 1
                index += 1
        print(nums)
        pass


if __name__ == '__main__':
    nums = [1, 0, 2]
    nums = [1, 0,1,0,3,12]
    # nums = [1]
    solution = Solution()
    print(solution.moveZeroes(nums))
    pass
