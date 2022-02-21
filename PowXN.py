#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

"""
from typing import *
from base import *


class Solution:
    """
    执行用时：
28 ms
, 在所有 Python3 提交中击败了
91.99%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
60.41%
的用户
    """
    def myPow(self, x: float, n: int) -> float:
        # 分治递归
        def helper(x, n):
            if n == 1:
                return x
            half = helper(x, n // 2)
            if n % 2 == 1:
                return x * half * half
            else:
                return half * half
        if n == 0 or x == 1:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1 / helper(x, -n)
        return helper(x, n)


if __name__ == '__main__':
    nums = "PAYPALISHIRING"
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.problem(nums, k))
    pass