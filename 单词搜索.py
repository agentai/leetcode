#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
79. 单词搜索

给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

https://leetcode-cn.com/problems/word-search

"""
from typing import *
from base import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        执行用时：
4144 ms
, 在所有 Python3 提交中击败了
12.58%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
84.93%
的用户
        """
        rows = len(board)
        cols = len(board[0])
        len_w = len(word)

        def find(r, c, cur):
            # 用cur来记录当前命中的所有坐标
            if len(cur) == len_w:
                return
            for a, b in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= a < rows and 0 <= b < cols and (a,b) not in cur and board[a][b] == word[len(cur)]:
                    cur.append((a, b))
                    find(a, b, cur)
                    if len(cur) == len_w:
                        return
                    cur.pop()

        for i in range(rows):
            for j in range(cols):
                # 命中首字母后，递归找
                if board[i][j] == word[0]:
                    tmp = [(i,j)] # 存所有坐标
                    find(i, j, tmp)
                    if len(tmp) == len_w:
                        return True

        return False


if __name__ == '__main__':
    nums = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    k = "SEE"
    # nums = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # k = "ABCCED"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.exist(nums, k))
    pass