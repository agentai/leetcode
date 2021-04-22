#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
338. 比特位计数

给定一个非负整数num。对于0 ≤ i ≤ num 范围中的每个数字i，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例2:

输入: 5
输出: [0,1,1,2,1,2]

https://leetcode-cn.com/problems/counting-bits
"""
from typing import *
from base import *
import math


class Solution:
    def countBits(self, num: int) -> List[int]:
        """
        执行用时：
60 ms
, 在所有 Python3 提交中击败了
92.84%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
89.53%
的用户
        """
        res = [0] # 记录最终结果
        high = 0 # 记录高位位置
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                # 如果 i 和 i-1 没交集，表示在类似 1->2 3>4 7>8 的位置，高位+1
                high = i
            # high + i 的位置 比 前一个high + i位置的值多1
            res.append(res[i - high] + 1)
        return res


if __name__ == '__main__':
    nums = 5
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.countBits(nums))
    pass