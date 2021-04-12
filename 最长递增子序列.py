#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

300. 最长递增子序列

示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1

https://leetcode-cn.com/problems/longest-increasing-subsequence/

"""
from typing import *
from base import *


class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        """执行用时：
3440 ms
, 在所有 Python3 提交中击败了
59.87%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
19.61%
的用"""
        # dp[i]表示到当前为止最长的子序列个数
        # dp[i] = max(dp[0]+1 if nums[i]>nums[0], dp[1]+1 if nums[i]>nums[1],... dp[n]+1 if nums[n]>nums[0])

        len_n = len(nums)
        dp = [1 for i in range(len_n)]
        max_v = 0
        for i in range(1, len_n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    max_v = max(dp[i], max_v)
        print(max_v)
        return max(dp)

        # # 相应的可以用dp[i] = list(递增序列)来存
        # len_n = len(nums)
        # dp = [[nums[i]] for i in range(len_n)]
        # max_index = 0
        # for i in range(1, len_n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[j].append(nums[i])
        #             if len(dp[j]) > len(dp[max_index]):
        #                 max_index = j
        # return dp[max_index]

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
执行用时：
5240 ms
, 在所有 Python3 提交中击败了
5.00%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
97.04%
的用户
        """
        # dp[i] 表示从nums[0:i]之间最长的递增子串
        # 拿nums[i]依次与0-i之间的数比较，如果nums[i] > nums[j]，则dp[i] = max(dp[i], dp[j]+1)
        len_n = len(nums)
        dp = [1] * len_n
        max_l = 1
        for i in range(len_n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    max_l = max(max_l, dp[i])
        return max_l


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    # nums = [7, 7, 7, 7, 7, 7]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.lengthOfLIS1(nums))
    print(solution.lengthOfLIS(nums))
    pass