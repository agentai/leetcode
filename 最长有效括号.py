#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
32. 最长有效括号

给你一个只包含 '('和 ')'的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0

https://leetcode-cn.com/problems/longest-valid-parentheses

"""
from typing import *
from base import *


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        """
        执行用时：
68 ms
, 在所有 Python3 提交中击败了
15.72%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
81.39%
的用户
        """
        # 用 l 记录左括号数，r 记录右括号数
        l, r = 0, 0
        # max_len 记录最大长度
        max_len = 0
        len_s = len(s)
        # 先从左往右遍历
        for i in range(len_s):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            # 如果l==r，max_len = 2* r
            if l == r:
                max_len = max(max_len, 2 * r)
            # 如果r > l，说明截断了，不合法，l和r清零
            elif r > l:
                l = r = 0
        # 从右往左也要算一遍
        l = r = 0
        for i in range(len_s-1, -1, -1):
            if s[i] == "(":
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, 2 * l)
            elif l > r:
                l = r = 0
        return max_len

    def longestValidParentheses(self, s: str) -> int:
        """
        执行用时：
76 ms
, 在所有 Python3 提交中击败了
7.61%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
13.87%
的用户
        """
        # stack 用来存左括号的索引，dp[i] 来记录第i位置是否合法
        len_s = len(s)
        stack = []
        dp = [0] * len_s
        for i in range(len_s):
            if s[i] == ")":
                if stack:
                    l = stack[-1]
                    match = True
                    for k in range(l+1, i):
                        if not dp[k]:
                            match = False
                            break
                    if match:
                        dp[l] = 1
                        dp[i] = 1
                        stack.pop()
            else:
                stack.append(i)
        max_len = 0
        for i in range(1, len_s):
            if dp[i] > 0:
                dp[i] += dp[i-1]
                max_len = max(max_len, dp[i])
        return max_len


if __name__ == '__main__':
    s = ")()())"
    # s = ")(())())"
    # s = "(()"
    # s = ""
    # s = "()"
    # s = "()(()"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.longestValidParentheses1(s))
    print(solution.longestValidParentheses(s))
    pass