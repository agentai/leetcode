#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
200. 岛屿数量

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

https://leetcode-cn.com/problems/number-of-islands/
"""
from typing import *
from base import *


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        执行用时：
76 ms
, 在所有 Python3 提交中击败了
69.86%
的用户
内存消耗：
19 MB
, 在所有 Python3 提交中击败了
24.96%
的用户
        """
        # 如果遇到"1"，往周边传播(dfs)，如果周边是"1"，改变值，直到无法传播
        rows = len(grid)
        cols = len(grid[0])

        # dfs搜索所有"1"，如果是"1"，改变值来表示已访问
        def dfs(r,c):
            # 当是"1"时才搜索
            if grid[r][c] == "1":
                # 改变值表示已访问
                grid[r][c] = 0
                # 搜索周边
                for (i,j) in [(r-1,c), (r,c-1), (r+1,c), (r,c+1)]:
                    # 去掉不合理的坐标
                    if i<0 or j<0 or i>=rows or j>=cols:
                        continue
                    # 继续递归搜索
                    dfs(i,j)

        # 记录岛屿数
        count = 0
        for i in range(rows):
            for j in range(cols):
                # 遇到岛屿了，岛屿数加1，并且基于当前点进行搜索
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        return count


        # count = 1
        # for i in range(rows):
        #     for j in range(cols):
        #         if i == 0 and j == 0:
        #             continue
        #         if grid[i][j] == "1":
        #             grid[i][j] = str(i)+str(j)
        #             if i == 0:
        #                 if grid[i][j-1] != "0":
        #                     grid[i][j] = grid[i][j-1]
        #             elif j == 0:
        #                 if grid[i-1][j] != "0":
        #                     grid[i][j] = grid[i-1][j]
        #             else:
        #                 if grid[i-1][j] != "0":
        #                     grid[i][j] = grid[i-1][j]
        #                     if grid[i][j-1] != "0":
        #                         grid[i][j-1] = grid[i-1][j]
        #                 else:
        #                     if grid[i][j - 1] != "0":
        #                 grid[i][j] = grid[i-1][j] + grid[i][j-1]
        #                 if (grid[i-1][j] == 1 and grid[i][j-1] >= 1) or (grid[i-1][j] >= 1 and grid[i][j-1] == 1):
        #                     count -= 1
        #         if grid[i][j] == 1:
        #             count += 1
        # return count


if __name__ == '__main__':
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    # grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    # grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.numIslands(grid))
    pass