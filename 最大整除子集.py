#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
368. 最大整除子集

给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]

https://leetcode-cn.com/problems/largest-divisible-subset
"""
from typing import *
from base import *


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        执行用时：
352 ms
, 在所有 Python3 提交中击败了
70.08%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
71.39%
的用户
        """
        # 排序 + 动态规划
        # 先排序
        if not nums:
            return []
        nums.sort()
        # 动态规划求解
        # dp[i] 表示当前数的最多有效子集列表
        # 如果 nums[i] % nums[j] == 0 则表示i有因子j，j包含的所以因子也能包含
        len_n = len(nums)
        max_len = 0
        max_index = 0
        dp = [[] for i in range(len_n)]
        for i in range(len_n):
            # 从后往前推，可以减少调换次数
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) <= len(dp[j])+1:
                        dp[i] = dp[j].copy()
                        dp[i].append(nums[j])
            if len(dp[i]) > max_len:
                max_len = len(dp[i])
                max_index = i
        dp[max_index].append(nums[max_index])
        return dp[max_index]


if __name__ == '__main__':
    nums = [1,2,4,8]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.largestDivisibleSubset(nums))
    pass