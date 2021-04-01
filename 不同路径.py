#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
    62. 不同路径
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

https://leetcode-cn.com/problems/unique-paths/

"""
from typing import List


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
85.16%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
48.14%
的用户
        """
        # dp[i][j] 表示当前位置的路径
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    m = 3
    n = 7
    solution = Solution()
    print(solution.uniquePaths(m, n))

    pass