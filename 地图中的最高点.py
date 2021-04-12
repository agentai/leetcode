#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

1765. 地图中的最高点

给你一个大小为m x n的整数矩阵isWater，它代表了一个由 陆地和 水域单元格组成的地图。

如果isWater[i][j] == 0，格子(i, j)是一个 陆地格子。
如果isWater[i][j] == 1，格子(i, j)是一个 水域格子。
你需要按照如下规则给每个单元格安排高度：

每个格子的高度都必须是非负的。
如果一个格子是是 水域，那么它的高度必须为 0。
任意相邻的格子高度差 至多为 1。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
找到一种安排高度的方案，使得矩阵中的最高高度值最大。

请你返回一个大小为m x n的整数矩阵 height，其中 height[i][j]是格子 (i, j)的高度。如果有多种解法，请返回任意一个。



示例 1：



输入：isWater = [[0,1],[0,0]]
输出：[[1,0],[2,1]]
解释：上图展示了给各个格子安排的高度。
蓝色格子是水域格，绿色格子是陆地格。
示例 2：



输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
输出：[[1,1,0],[0,1,1],[1,2,2]]
解释：所有安排方案中，最高可行高度为 2 。
任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。

https://leetcode-cn.com/problems/map-of-highest-peak

"""
from typing import *
from base import *


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # 从水域出发，做广度优先搜索，依次赋值为深度，然后求最小值
        len_r = len(isWater)
        len_c = len(isWater[0])
        res = [[-1] * len_c for i in range(len_r)]
        for r in range(len_r):
            for c in range(len_c):
                if isWater[r][c] == 1:
                    res[r][c] = 0

        def bfs(r, c):
            if r < 0 or c < 0 or r >= len_r or c >= len_c:
                return
            for i, j in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if i >= len_r or i < 0 or j >= len_c or j < 0:
                    continue
                if res[i][j] < 0:
                    res[i][j] = res[r][c] + 1
                    bfs(i, j)
                    continue
                if res[i][j] == 0:
                    continue
                tmp = res[i][j] - res[r][c]
                if tmp > 1:
                    res[i][j] = res[r][c] + 1
                    bfs(i, j)
                elif tmp < -1:
                    res[i][j] = res[r][c] - 1
                    bfs(i, j)
                else:
                    return
            return

        for r in range(len_r):
            for c in range(len_c):
                if isWater[r][c] == 1:
                    bfs(r, c)
        return res


if __name__ == '__main__':
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    isWater = [[0, 1], [0, 0]]
    isWater = [[0, 1], [0, 1]]
    isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
    print(solution.highestPeak(isWater))
    pass