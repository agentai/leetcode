#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
202. 快乐数
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为 1，那么这个数就是快乐数。
如果 n 是快乐数就返回 true ；不是，则返回 false 。

示例 1：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：

输入：n = 2
输出：false

https://leetcode-cn.com/problems/happy-number
"""
from typing import *
from base import *


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
95.46%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
27.71%
的用户
        """
        data = set()
        def sub(num):
            if num == 1:
                return True
            if num in data:
                return False
            # 这个位置很关键，先判断要计算的数有没有在data里了，再进行计算
            data.add(num)
            res = 0
            while num:
                res += (num%10) * (num%10)
                num //= 10
            return sub(res)
        return sub(n)


if __name__ == '__main__':
    nums = 19
    nums = 2
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.isHappy(nums))
    pass