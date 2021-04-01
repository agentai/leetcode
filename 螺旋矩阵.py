#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    54. 螺旋矩阵
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

https://leetcode-cn.com/problems/spiral-matrix/

"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        执行用时：
28 ms
, 在所有 Python3 提交中击败了
98.71%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
41.13%
的用户
        """
        # 用direction控制方向，用r,c记录当前位置，用cycle记录第几圈
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        r, c = 0, 0 # 当前位置
        direction = 'r' # 指定方向
        cycle = 1  # 第几圈
        i = 0 # 总循环次数
        while i < rows * cols:
            res.append(matrix[r][c])
            i += 1
            # 初始方向是r，往左走
            if c < cols - cycle and direction == "r":
                c += 1
            # 方向是r，且走到底后，换方向往下走
            elif c == cols - cycle and direction == "r":
                direction = "d"
                r += 1
            # 方向是d，往下走
            elif r < rows - cycle and direction == "d":
                r += 1
            # 往下走到底后，换方向
            elif r == rows - cycle and direction == "d":
                direction = "l"
                c -= 1
            elif c > cycle - 1 and direction == "l":
                c -= 1
            elif c == cycle - 1 and direction == "l":
                # 往上走后，周期+1
                direction = "u"
                r -= 1
                cycle += 1
            elif r > cycle - 1 and direction == "u":
                r -= 1
            elif r == cycle - 1 and direction == "u":
                direction = "r"
                c += 1
        return res


if __name__ == '__main__':
    k = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()
    print(solution.spiralOrder(k))

    pass