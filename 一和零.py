#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
474. 一和零

示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

https://leetcode-cn.com/problems/ones-and-zeroes/

"""
from typing import *
from base import *


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
执行用时：
5960 ms
, 在所有 Python3 提交中击败了
12.47%
的用户
内存消耗：
70.1 MB
, 在所有 Python3 提交中击败了
10.96%
的用户
        """
        # dp[k][i][j] 表示放入k个str后，最多能积累的i个0和j个1
        len_s = len(strs)
        dp = [[[0] * (n+1) for i in range(m+1)] for j in range(len_s+1)]
        for k in range(1, len_s+1):
            # 当前0和1的个数
            count_0 = strs[k-1].count("0")
            count_1 = strs[k-1].count("1")
            for i in range(m+1):
                for j in range(n+1):
                    dp[k][i][j] = dp[k-1][i][j]
                    # 如果没有满的话，与k-1的个str的第i-count_0和j-count_1比较
                    if i >= count_0 and j >= count_1:
                        dp[k][i][j] = max(dp[k-1][i][j], dp[k-1][i-count_0][j-count_1] + 1)
        return dp[len(strs)][m][n]

    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        """
        执行用时：
3024 ms
, 在所有 Python3 提交中击败了
75.50%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
91.81%
的用户
        """
        # dp(i,j)，表示到i个1和j个0需要的最多str个数
        dp = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            # 当前str的0个数和1个数
            count_0 = s.count("0")
            count_1 = s.count("1")
            for i in range(m, count_0-1, -1):
                for j in range(n, count_1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-count_0][j-count_1]+1)
        return dp[m][n]


if __name__ == '__main__':
    nums = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.findMaxForm1(nums, m, n))
    pass