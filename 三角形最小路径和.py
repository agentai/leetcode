#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
120. 三角形最小路径和

给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为11（即，2+3+5+1= 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10

https://leetcode-cn.com/problems/triangle
"""
from typing import *
from base import *


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
57.62%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
32.32%
的用户
        """
        # dp[i][j] 表示到达第i行第j列的最小路径和
        # dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        # if i == 0: dp[i] = [tran[0]]
        dp = [triangle[0]]
        for i in range(1, len(triangle)):
            tmp = [dp[i-1][0] + triangle[i][0]]
            for j in range(1, len(triangle[i])-1):
                tmp.append(min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
            tmp.append(dp[i-1][-1] + triangle[i][-1])
            dp.append(tmp)
        return min(dp[-1])


if __name__ == '__main__':
    nums = [[2],[3,4],[6,5,7],[4,1,8,3]]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.minimumTotal(nums))
    pass