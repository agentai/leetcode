#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
75. 颜色分类


示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]

https://leetcode-cn.com/problems/sort-colors/

"""
from typing import *
from base import *


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """执行用时：
48 ms
, 在所有 Python3 提交中击败了
15.26%
的用户
内存消耗：
14.6 MB
, 在所有 Python3 提交中击败了
93.13%
的用"""
        # 快排
        def quick_sort(l, r):
            # 加速，以0开头的，l+=1
            while l < r and nums[l] == 0:
                l += 1
            # 以2结尾的r-=1
            while l < r and nums[r] == 2:
                r -= 1
            # 以2开头的，对换，r-=1
            while l < r and nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            while l < r and nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            if l >= r:
                return
            base = nums[r]
            min_i = l
            for i in range(l, r):
                if nums[i] < base:
                    nums[min_i], nums[i] = nums[i], nums[min_i]
                    min_i += 1
            nums[min_i], nums[r] = nums[r], nums[min_i]
            quick_sort(l, min_i-1)
            quick_sort(min_i+1, r)
        quick_sort(0, len(nums)-1)


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.sortColors(nums))
    pass