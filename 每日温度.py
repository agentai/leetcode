#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
739. 每日温度

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用0 来代替。

例如，给定一个列表temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是[1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是[1, 30000]。每个气温的值的均为华氏度，都是在[30, 100]范围内的整数。


https://leetcode-cn.com/problems/daily-temperatures
"""
from typing import *
from base import *


class Solution:
    def dailyTemperatures1(self, T: List[int]) -> List[int]:
        # 思路，从右往左遍历，dp[i]表示从右往左 最近的超过当前i温度的位置
        # 中间查找用二分法
        len_t = len(T)

        def find(l, r, aim):
            if l >= len_t:
                return len_t + 10
            if T[l] > aim:
                return l
            if r - l <= 1:
                if T[r] > aim:
                    return r
                else:
                    return len_t + 10
            m = (l+r)//2
            if T[m] > aim:
                return find(l, m, aim)
            left = find(l, m, aim)
            if left < len_t:
                return left
            return find(m+1, r, aim)

        dp = [len_t + 10] * len_t
        for i in range(len_t-1, -1, -1):
            k = find(i+1, len_t-1, T[i])
            if k < len_t:
                dp[i] = min(dp[i], k-i)
        for i in range(len_t):
            if dp[i] > len_t:
                dp[i] = 0
        return dp

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        执行用时：
636 ms
, 在所有 Python3 提交中击败了
13.92%
的用户
内存消耗：
19 MB
, 在所有 Python3 提交中击败了
82.23%
的用户
        """
        # 单调栈，用一个栈来记录到当前为止还没有找到对应温度更高的位置的索引
        # 并且栈中的元素是索引，其对应的温度递增的
        stack = []
        len_t = len(T)
        dp = [0] * len_t
        for i in range(len_t):
            while stack and T[i] > T[stack[-1]]:
                k = stack.pop()
                dp[k] = i - k
            stack.append(i)
        return dp


if __name__ == '__main__':
    nums = [73, 74, 75, 71, 69, 72, 76, 73]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.dailyTemperatures(nums))
    pass