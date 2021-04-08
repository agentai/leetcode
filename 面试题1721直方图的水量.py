#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
面试题 17.21. 直方图的水量

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

https://leetcode-cn.com/problems/volume-of-histogram-lcci/
"""
from typing import *
from base import *


class Solution:
    def trap1(self, height: List[int]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
61.21%
的用户
内存消耗：
16 MB
, 在所有 Python3 提交中击败了
5.01%
的用户
        """
        # 思路，dp[i] = [(l,r)]，dp表示当前位置左边的最大值l和右边的最大值r
        # dp[l][0] = max(dp[l-1][0], height[l])
        # dp[r][1] = max(dp[r+1][1], height[r])
        len_h = len(height)
        dp = [[-1, -1] for i in range(len_h)]
        for l in range(len_h):
            r = len_h - l - 1
            if l > 0:
                dp[l][0] = max(dp[l-1][0], height[l])
            else:
                dp[l][0] = height[l]
            if r < len_h - 1:
                dp[r][1] = max(dp[r+1][1], height[r])
            else:
                dp[r][1] = height[r]
        res = 0
        for i in range(len_h):
            res += min(dp[i][0], dp[i][1]) - height[i]
        return res

    def trap(self, height: List[int]) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
79.95%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
17.68%
的用户
        """
        # 栈, 先从左往右存从左往右的最小值，结果存入栈，然后从右往左走，同时出栈
        if not height:
            return 0
        stack = []
        for i in height:
            if not stack:
                stack.append(i)
            else:
                stack.append(max(stack[-1], i))
        max_r = height.pop()
        stack.pop()
        res = 0
        while height:
            cur = height.pop()
            if max_r < cur:
                max_r = cur
            res += min(stack.pop(), max_r) - cur
        return res


if __name__ == '__main__':
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.trap(nums))
    pass