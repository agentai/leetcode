#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/1

"""
文件说明：
    1. 两数之和
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

    https://leetcode-cn.com/problems/two-sum/
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2jrse/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """执行用时：
36 ms
, 在所有 Python3 提交中击败了
85.36%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
22.21%
的用户"""
        # 思路：因为要返回数值的下标，所有需要用一个字典来存，key是值，val是下标
        # 依次遍历，如果target-当前值不在字典里，字典中加上当前值，如果在的话，直接返回
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
