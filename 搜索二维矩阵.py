#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    74. 搜索二维矩阵
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

https://leetcode-cn.com/problems/search-a-2d-matrix/

"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
62.45%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
94.52%
的用户
        """
        # 二分查找所在行
        row = len(matrix)
        col = len(matrix[0])
        def find(l, r, i):
            if r - l <= 1:
                if matrix[i][l] == target or matrix[i][r] == target:
                    return True
                return False
            m = (l+r)//2
            if matrix[i][m] == target:
                return True
            elif matrix[i][m] > target:
                return find(l, m, i)
            else:
                return find(m, r, i)

        for i in range(row):
            # 如果到所在行第一个数大于target了，return false
            if matrix[i][0] > target:
                return False
            # 如果不满足条件2 或者不在所在行，就继续
            if matrix[i][col-1] < target:
                continue
            # 定位所在行，在继续二分查找
            return find(0, col-1, i)
        return False


if __name__ == '__main__':
    nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    k = 3
    solution = Solution()
    print(solution.searchMatrix(nums, k))

    pass