#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
695. 岛屿的最大面积

给定一个包含了一些 0 和 1 的非空二维数组grid 。

一个岛屿是由一些相邻的1(代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)


示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回0。


https://leetcode-cn.com/problems/max-area-of-island
"""
from typing import *
from base import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        执行用时：
136 ms
, 在所有 Python3 提交中击败了
91.67%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
85.70%
的用户
        """
        # dfs,遇到1，就开始传播，一直到无法传播为止，同时记录maxarea
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # 遇到1，开始传播，用一个队列来存当前节点
                    queue = [(i,j)]
                    grid[i][j] = -1
                    tmp_area = 1
                    while queue:
                        (r, c) = queue.pop()
                        # 往四个方向走，如果遇到陆地，加入队列继续走
                        for x, y in [(r-1, c), (r, c-1), (r, c+1), (r+1, c)]:
                            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                                queue.append((x,y))
                                tmp_area += 1
                                grid[x][y] = -1
                    # 走完后比较下这片陆地的大小
                    max_area = max(max_area, tmp_area)
        return max_area


if __name__ == '__main__':
    nums = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.maxAreaOfIsland(nums))
    pass