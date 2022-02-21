#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

"""
from typing import *
from base import *


class Solution:
    """
    执行用时：
212 ms
, 在所有 Python3 提交中击败了
5.31%
的用户
内存消耗：
18.7 MB
, 在所有 Python3 提交中击败了
20.78%
的用户
    """
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] 表示从word1[:i]到word2[:j]的最小距离
        dp = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for i in range(len(word2)+1):
            dp[0][i] = i
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                cost = 0 if word1[i-1] == word2[j-1] else 1
                dp[i][j] = min(dp[i-1][j-1] + cost, min(dp[i][j-1] + 1, dp[i-1][j] + 1))
        return dp[len(word1)][len(word2)]


if __name__ == '__main__':
    nums = "PAYPALISHIRING"
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.minDistance("horse", "ros"))
    pass