#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
剑指 Offer 04. 二维数组中的查找

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。

给定 target=20，返回false。


https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
"""
from typing import *
from base import *


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
73.02%
的用户
内存消耗：
19 MB
, 在所有 Python3 提交中击败了
5.00%
的用户
        """
        # 固定一列，然后二分
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        def find(r1, r2, c):
            if r2 - r1 <= 1:
                return matrix[r1][c] == target or matrix[r2][c] == target
            if matrix[r1][c] > target or matrix[r2][c] < target:
                return False
            m = (r1 + r2) // 2
            if matrix[m][c] == target:
                return True
            elif matrix[m][c] > target:
                return find(r1, m, c)
            else:
                return find(m, r2, c)

        for c in range(cols):
            if find(0, rows-1, c):
                return True

        return False


if __name__ == '__main__':
    nums = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    k = 21
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.findNumberIn2DArray(nums, k))
    pass