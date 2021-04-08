#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
978. 最长湍流子数组

示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])
示例 2：

输入：[4,8,12,16]
输出：2
示例 3：

输入：[100]
输出：1

https://leetcode-cn.com/problems/longest-turbulent-subarray/
"""
from typing import *
from base import *


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        执行用时：
312 ms
, 在所有 Python3 提交中击败了
5.02%
的用户
内存消耗：
19.6 MB
, 在所有 Python3 提交中击败了
8.85%
的用户
        """
        # dp[i][0]表示当目前为止最长满足奇数要求的序列dp[i][1]表示满足偶数要求的序列
        # 奇数的i的0记录减，1记录增。偶数的i的0记录增，1记录减
        len_a = len(arr)
        if len_a <= 1:
            return len_a
        dp = [[1, 1] for i in range(len_a)]
        res = 1 # 记录最大的满足条件长度
        for i in range(1, len_a):
            # 如果满足减，当前的0是i-1的1的值+1
            if arr[i] < arr[i-1]:
                dp[i][0] = dp[i-1][1] + 1
                res = max(res, dp[i][0])
            # 如果满足增，当前的1是i-1的0的值+1
            elif arr[i-1] < arr[i]:
                dp[i][1] = dp[i-1][0] + 1
                res = max(res, dp[i][1])
        return res

    def maxTurbulenceSize1(self, arr: List[int]) -> int:
        """执行用时：
140 ms
, 在所有 Python3 提交中击败了
84.72%
的用户
内存消耗：
18 MB
, 在所有 Python3 提交中击败了
35.05%
的用户"""
        len_a = len(arr)
        if len_a <= 1:
            return len_a
        dp0 = dp1 = 1
        res = 1  # 记录最大的满足条件长度
        for i in range(1, len_a):
            if arr[i] < arr[i-1]:
                # dp0必须优先于dp1
                dp0 = dp1 + 1
                dp1 = 1
                res = max(res, dp0)
            elif arr[i-1] < arr[i]:
                dp1 = dp0 + 1
                dp0 = 1
                res = max(res, dp1)
            else:
                dp0 = dp1 = 1
        return res


if __name__ == '__main__':
    nums = [9,4,2,10,7,8,8,1,9]
    # nums = [9, 9]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.maxTurbulenceSize1(nums))
    pass