#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
1006. 笨阶乘

示例 1：

输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1

示例 2：

输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1


https://leetcode-cn.com/problems/clumsy-factorial/
"""
from typing import *
from base import *


class Solution:
    def clumsy(self, N: int) -> int:
        """
        执行用时：
80 ms
, 在所有 Python3 提交中击败了
26.09%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
83.70%
的用户
        """
        # 思路：需要注意加减乘除的顺序，并且注意整除在正负数时候的区别
        i = 0
        stack = [N]
        for cur in range(N - 1, 0, -1):
            i = i % 4
            if i == 0:
                stack[-1] *= cur
            elif i == 1:
                if stack[-1] < 0:
                    # 如果小于0，需要先转成正数进行整除，在转回去
                    stack[-1] = -stack[-1]
                    stack[-1] //= cur
                    stack[-1] = -stack[-1]
                else:
                    stack[-1] //= cur
            elif i == 2:
                # 因为减法后面是乘法，所以先不计算减法，将数据的负数加入队列
                stack[-1] += cur
            else:
                stack.append(-cur)
            i += 1
        return sum(stack)


if __name__ == '__main__':
    k = 7
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.clumsy(k))
    pass