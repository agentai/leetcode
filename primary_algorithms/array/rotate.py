#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    旋转数组
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        先 -k:len_nums 反转
        再 0:len_num-k 反转
        再整体反转
        """

        def reverse(nums):
            len_nums = len(nums) - 1
            index = 0
            while index < len_nums:
                tmp = nums[index]
                nums[index] = nums[len_nums]
                nums[len_nums] = tmp
                index += 1
                len_nums -= 1
            return nums
        len_nums = len(nums)
        if len_nums<=1:
            return
        k = len_nums%k

        tmp = reverse(nums[-k:len_nums])
        for index in range(k):
            nums[-k+index] = tmp[index]
        tmp = reverse(nums[0:len_nums-k])
        for index in range(len_nums-k):
            nums[index] = tmp[index]
        return reverse(nums)


if __name__ == '__main__':
    nums = [-1]
    solution = Solution()
    print(solution.rotate(nums, 2))
    pass
