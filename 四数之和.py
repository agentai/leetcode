#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
18. 四数之和
给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。


示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：

输入：nums = [], target = 0
输出：[]

https://leetcode-cn.com/problems/4sum
"""
from typing import *
from base import *


class Solution:
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        """
        执行用时：
8460 ms
, 在所有 Python3 提交中击败了
5.03%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
64.66%
的用户
        """
        len_n = len(nums)
        nums.sort()
        res = []
        for i in range(len_n - 3):
            aim = target - nums[i]
            a = i + 1
            while a < len_n - 2:
                b = a + 1
                while b < len_n - 1:
                    c = b + 1
                    while c < len_n:
                        tmp = nums[a] + nums[b] + nums[c]
                        if tmp == aim and [nums[i], nums[a], nums[b], nums[c]] not in res:
                            res.append([nums[i], nums[a], nums[b], nums[c]])
                        if tmp > aim:
                            break
                        c += 1
                    b += 1
                a += 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        执行用时：
72 ms
, 在所有 Python3 提交中击败了
97.36%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
24.72%
的用户
        """
        # 三指针
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets

        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets


if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2]
    k = 0
    nums = [2, 2, 2, 2, 2]
    k = 8
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.fourSum(nums, k))
    pass