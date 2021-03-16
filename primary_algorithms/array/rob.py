#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/15

"""
文件说明：
    
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """213. 打家劫舍 II
        执行用时：
32 ms
, 在所有 Python3 提交中击败了
95.86%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
75.00%
的用
        :param nums:
        :return:
        """
        def max(a, b):
            if a > b:
                return a
            return b

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur

        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
    def rob5(self, nums: List[int]) -> int:
        """
        213. 打家劫舍 II
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
60.10%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
7.38%
的用户"""
        def max(a, b):
            if a > b:
                return a
            return b
        l1,r1 = nums[0], max(nums[0], nums[1])
        l2,r2 = nums[1], max(nums[1], nums[2])
        for i in range(2, len(nums)-1):
            l1,r1 = r1, max(l1 + nums[i], r1)
            l2,r2 = r2, max(l2 + nums[i+1], r2)

        dp = [nums[0], max(nums[0], nums[1])]
        dp1 = [nums[1], max(nums[1], nums[2])]
        for i in range(2, len(nums)-1):
            dp = [dp[1], max(dp[0] + nums[i], dp[1])]
            dp1 = [dp1[1], max(dp1[0] + nums[i+1], dp1[1])]
        return max(dp1[1],dp[1])

    def rob2(self, nums: List[int]) -> int:
        """198.打家劫舍（简单）
        执行用时：
32 ms
, 在所有 Python3 提交中击败了
93.83%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
46.90%
的用户
        :param nums:
        :return:
        """
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second

    def rob1(self, nums: List[int]) -> int:
        """198.打家劫舍（简单）
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
57.87%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
28.56%
的用户"""
        # dp[i][j] 表示第i个房间，j={0,1}表示不偷和偷
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        # dp[i][1] = dp[i-1][0]+nums[i]
        # badcase
        # dp[0][0] = 0
        # dp[0][1] = nums[0]
        def max(a,b):
            if a>b:
                return a
            else:
                return b
        res = 0
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            dp = [max(dp[0], dp[1]), dp[0] + nums[i]]
        return max(dp[0], dp[1])


if __name__ == '__main__':
    # nums = [1, 2,3,1]
    # # nums = [2,3,2]
    # nums = [2,7,9,3,1]
    # solution = Solution()
    # print(solution.rob(nums))
    nums = [3, 2, 3, None, 3, None, 1]
    pass
