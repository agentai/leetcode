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


45. 跳跃游戏 II

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
    从下标为 0 跳到下标为 1 的位置，跳1步，然后跳3步到达数组的最后一个位置。

https://leetcode-cn.com/problems/jump-game-ii

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

    def jump1(self, nums: List[int]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
57.81%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
82.69%
的用户
        """
        # dp[i]表示到达当前位置需要的最小次数
        len_n = len(nums)
        dp = [len_n + 10] * len_n
        dp[0] = 0
        for i in range(len_n):
            for j in range(i, min(len_n, i + nums[i] + 1)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[len_n - 1]

    def jump(self, nums: List[int]) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
68.58%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
94.09%
的用户
        """
        # 用一个变量记录最右边可触达的，用另一个变量记录到当前步下最多能走的位置
        len_n = len(nums)
        # right_most 记录最右边可触达的位置
        # end 记录i到当前end位置，期间能达到的最右边位置
        right_most, end = 0, 0
        step = 0
        for i in range(len_n-1):
            # 如果当前i可触达
            if i <= right_most:
                # 更新最右边位置
                right_most = max(right_most, i + nums[i])
                # 如果i已经到达了上一步能触达的最右边，则加一步并更新end
                if i >= end:
                    step += 1
                    end = right_most
                    # 提速，如果更新end的同时发现已经到底了，直接返回
                    if right_most >= len_n - 1:
                        break
                else:
                    if right_most >= len_n - 1:
                        step += 1
                        break
        return step


if __name__ == '__main__':
    k = [2,3,1,1,4]
    # k = [3,2,1,0,4]
    k = [0]
    solution = Solution()
    # print(solution.canJump(k))
    print(solution.jump(k))

    pass