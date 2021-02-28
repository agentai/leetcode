#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    买卖股票的最佳时机 II
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2zsx1/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
89.41%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
53.92%
的用户
        :param prices:
        :return:
        """
        len_prices = len(prices)
        if len_prices==0:
            return 0
        profit = 0
        index = 0
        while index < len_prices-1:
            if prices[index+1] > prices[index]:
                profit += prices[index+1] - prices[index]
            index += 1
        return profit

    def maxProfit1(self, prices: List[int]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
82.54%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
79.12%
的用户
        :param prices:
        :return:
        """
        len_prices = len(prices)
        if len_prices == 0:
            return 0
        index = 0
        profit = 0
        hold = True
        start = prices[index]
        while index < len_prices-1:
            if not hold:
                start = prices[index]
                hold = True
            if prices[index] >= prices[index+1] and hold:
                profit += prices[index] - start
                hold = False
                start = prices[index]
            index += 1
        if hold and prices[index] > start:
            profit += prices[index] - start

        return profit


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    solution = Solution()
    print(solution.maxProfit(nums))
    pass
