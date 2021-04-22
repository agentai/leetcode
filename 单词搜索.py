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
        rows = len(board)
        cols = len(board[0])
        len_w = len(word)

        def find(r, c, cur):
            if len(cur) == len_w:
                return
            for a, b in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= a < rows and 0 <= b < cols and (a,b) not in cur and board[a][b] == word[len(cur)-1]:
                    cur.append((a, b))
                    find(a, b, cur)
                    cur.pop()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    match = True
                    tmp = []
                    k = 1
                    r, c = i, j
                    while k < len_w:
                        for a, b in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                            if 0 <= a < rows and 0 <= b < cols:

        pass


if __name__ == '__main__':
    nums = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    k = "SEE"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.problem(nums, k))
    pass