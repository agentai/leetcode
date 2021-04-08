#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    55. 跳跃游戏
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

https://leetcode-cn.com/problems/jump-game/

"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
52.08%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
73.49%
的用户
        """
        # 用一个数来记录最右边可触达的位置
        len_n, right_most = len(nums), 0
        for i in range(len_n):
            if i <= right_most:
                # 如果当前位置已经可触达，取当前位置+当前位置值 和 最大可触达位置比较。
                right_most = max(nums[i] + i, right_most)
                if right_most >= len_n - 1:
                    return True
        return False

    def canJump1(self, nums: List[int]) -> bool:
        """超时"""
        # dp[i]={True, False} True表示能到达
        # if dp[i] is True, dp[i+nums[i]] = True
        len_n = len(nums)
        dp = [False] * len_n
        dp[0] = True
        for i in range(len_n):
            if dp[i]:
                j = min(len_n - 1, i + nums[i])
                if j == len_n - 1:
                    return True
                while j > 0:
                    dp[j] = True
                    j -= 1
        return dp[len_n - 1]


if __name__ == '__main__':
    k = [2,3,1,1,4]
    k = [3,2,1,0,4]
    solution = Solution()
    print(solution.canJump(k))

    pass