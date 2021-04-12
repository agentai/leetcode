#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
263. 丑数
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

丑数 就是只包含质因数2、3 和/或5的正整数。


示例 1：

输入：n = 6
输出：true
解释：6 = 2 × 3
示例 2：

输入：n = 8
输出：true
解释：8 = 2 × 2 × 2
示例 3：

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数7 。
示例 4：

输入：n = 1
输出：true
解释：1 通常被视为丑数。


https://leetcode-cn.com/problems/ugly-number


264. 丑数 II

给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数2、3 和/或5的正整数。

示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。


https://leetcode-cn.com/problems/ugly-number-ii/


"""
from typing import *
from base import *


class Solution:
    def isUgly(self, n: int) -> bool:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
49.43%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
5.12%
的用户
        """
        # 思路，递归求与和除，判断是否能除尽
        if n == 1:
            return True
        if n <= 0:
            return False

        def sub(n):
            for i in (2, 3, 5):
                if n % i > 0:
                    continue
                tmp = n // i
                if tmp == 1:
                    return True
                return sub(tmp)
            return False
        return sub(n)

    def nthUglyNumber(self, n: int) -> int:
        """
执行用时：
616 ms
, 在所有 Python3 提交中击败了
11.83%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
83.84%
的用户
        """
        # 思路，用一个队列表当前所有的丑数，
        # 给每个丑数都算一次+* 235
        if n <= 1:
            return 1
        stack = [1]
        tmp = 1
        for i in range(n):
            tmp = stack.pop(0)
            for k in (2, 3, 5):
                a = tmp*k
                if a not in stack:
                    stack.append(a)
            stack.sort()
        return tmp




if __name__ == '__main__':
    nums = 1
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.nthUglyNumber(nums))
    print(solution.isUgly(nums))


    pass