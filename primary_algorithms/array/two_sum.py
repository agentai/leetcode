#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/1

"""
文件说明：
    两数之和
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2jrse/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """执行用时：
40 ms
, 在所有 Python3 提交中击败了
63.63%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
44.50%
的用户"""
        data = {}
        for index in range(len(nums)):
            if target-nums[index] in data:
                return [data[target-nums[index]], index]
            else:
                data[nums[index]] = index
        return []


if __name__ == '__main__':
    nums = [1,3, 4, 2]
    k = 6
    solution = Solution()
    print(solution.twoSum(nums, k))
    pass
