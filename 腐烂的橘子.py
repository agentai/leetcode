#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
994. 腐烂的橘子

在给定的网格中，每个单元格可以有以下三个值之一：

值0代表空单元格；
值1代表新鲜橘子；
值2代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回-1。

示例 1：

输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4

示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。


https://leetcode-cn.com/problems/rotting-oranges
"""
from typing import *
from base import *


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        执行用时：
88 ms
, 在所有 Python3 提交中击败了
5.64%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
49.21%
的用户
        """
        # 用一个队列来存腐烂的橙子位置
        # 另一个队列来存新鲜的橙子位置
        # 如果当前腐烂的橙子周围没有新鲜橙子，直接返回-1
        # 如果有的话，新鲜橙子减1，腐烂橙子加1
        queue_new = []
        queue_old = []
        len_r = len(grid)
        len_c = len(grid[0])
        for i in range(len_r):
            for j in range(len_c):
                if grid[i][j] == 1:
                    queue_new.append((i, j))
                elif grid[i][j] == 2:
                    queue_old.append((i, j))
        step = 0
        while True:
            if not queue_new:
                return step
            to_old = []
            for (i, j) in queue_old:
                tmp = []
                if i > 0 and j > 0:
                    tmp.extend([(i-1, j), (i, j-1)])
                elif i > 0:
                    tmp.append((i-1, j))
                elif j > 0:
                    tmp.append((i, j-1))
                if i < len_r-1 and j < len_c - 1:
                    tmp.extend([(i+1, j), (i, j+1)])
                elif i < len_r-1:
                    tmp.append((i+1, j))
                elif j < len_c-1:
                    tmp.append((i, j+1))
                size = len(queue_new)
                for _ in range(size):
                    (r, c) = queue_new.pop()
                    if (r, c) in tmp:
                        to_old.append((r, c))
                    else:
                        queue_new.insert(0, (r, c))
            step += 1
            if to_old:
                queue_old.extend(to_old)
            else:
                return -1


if __name__ == '__main__':
    nums = [[2,1,1],[1,1,0],[0,1,1]]
    # nums = [[2,1,1],[0,1,1],[1,0,1]]
    # nums = [[0,2]]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.orangesRotting(nums))
    pass