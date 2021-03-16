#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/2

"""
文件说明：
    
"""
from typing import List


class Solution:

    def isValidSudoku(self, board):
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
97.66%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
10.99%
的用户
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                curNum = ord(board[i][j]) - ord('0')
                if row[i][curNum] != 0 or col[j][curNum] != 0 or box[j // 3 + (i // 3) * 3][curNum] != 0:
                    return False
                row[i][curNum], col[j][curNum], box[j // 3 + (i // 3) * 3][curNum] = 1, 1, 1
        return True

    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        """执行用时：
44 ms
, 在所有 Python3 提交中击败了
91.94%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
75.40%
的用户 """
        data = {}
        # row_key = row*10
        # col_key = col*100
        # key = (r<3,c<3)-> 1
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                key = int(row / 3) + int(int(col / 3) * 3)
                row_key = (row+1) * 10
                col_key = (col+1) * 100
                tmp = data.get(key, set())
                if board[row][col] in tmp:
                    return False
                else:
                    tmp.add(board[row][col])
                    data[key] = tmp

                tmp = data.get(row_key, set())
                if board[row][col] in tmp:
                    return False
                else:
                    tmp.add(board[row][col])
                    data[row_key] = tmp

                tmp = data.get(col_key, set())
                if board[row][col] in tmp:
                    return False
                else:
                    tmp.add(board[row][col])
                    data[col_key] = tmp
        return True


if __name__ == '__main__':
    nums = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

    solution = Solution()
    print(solution.isValidSudoku(nums))
    pass
