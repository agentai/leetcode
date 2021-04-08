#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
31. 下一个排列

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]

https://leetcode-cn.com/problems/next-permutation/
"""
from typing import *
from base import *


class Solution:

    def nextPermutation(self, nums: List[int]) -> List[int]:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def nextPermutation1(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快排
        change = [False]
        def quick_sort(l, r):
            if l >= len(nums) or r < 0:
                return
            if r - l <= 1:
                if nums[r] < nums[l]:
                    change[0] = True
                    nums[r], nums[l] = nums[l], nums[r]
                return
            base_i = l
            base_n = nums[r]
            for i in range(l, r):
                if nums[i] < base_n:
                    nums[i], nums[base_i] = nums[base_i], nums[i]
                    base_i += 1
            if base_i != r:
                nums[base_i], nums[r] = nums[r], nums[base_i]
                change[0] = True
            quick_sort(l, base_i-1)
            quick_sort(base_i+1, r)
        quick_sort(0, len(nums)-1)
        if change[0]:
            return nums
        if len(nums) > 1:
            nums[-2], nums[-1] = nums[-1], nums[-2]
        return nums


if __name__ == '__main__':
    nums = [1,2,3]
    nums = [1,3,2]
    nums = [3,2,1]
    nums = [1,1,5]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.nextPermutation(nums))
    pass