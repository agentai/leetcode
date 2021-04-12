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


63. 不同路径 II

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

https://leetcode-cn.com/problems/unique-paths-ii

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

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
执行用时：
36 ms
, 在所有 Python3 提交中击败了
88.24%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
13.90%
的用户
        """
        # dp[i][j]表示到当前位置的路径数
        len_r = len(obstacleGrid)
        len_c = len(obstacleGrid[0])
        dp = [[0 for i in range(len_c)] for j in range(len_r)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for r in range(len_r):
            for c in range(len_c):
                if obstacleGrid[r][c] == 0:
                    if c == 0 and r == 0:
                        continue
                    elif c == 0:
                        dp[r][c] = dp[r - 1][c]
                    elif r == 0:
                        dp[r][c] = dp[r][c - 1]
                    else:
                        dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[len_r - 1][len_c - 1]


if __name__ == '__main__':
    m = 3
    n = 7
    solution = Solution()
    print(solution.uniquePaths(m, n))

    nums = [[0,0,0],[0,1,0],[0,0,0]]
    print(solution.uniquePathsWithObstacles(nums))

    pass