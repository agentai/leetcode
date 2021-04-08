#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    122. 买卖股票的最佳时机 II
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2zsx1/
"""
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
66.56%
的用户
内存消耗：
15.5 MB
, 在所有 Python3 提交中击败了
74.51%
的用户
        """
        # 思路 dp[i][0]表示卖出收益，dp[i][1]表示持有收益
        # 卖出的话，收益为加上当前price，买入的话，收益是减去当前收益
        # dp[0][0] = 0, dp[0][1] = -prices[0]
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price)
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0]-price)
        dp0, dp1 = 0, -prices[0]
        for price in prices[1:]:
            tmp = dp0
            dp0 = max(dp0, dp1+price)
            dp1 = max(dp1, tmp-price)
        return max(dp0, dp1)

    def maxProfit5(self, prices: List[int]) -> int:
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
