#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
322. 零钱兑换

示例1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1

https://leetcode-cn.com/problems/coin-change/
"""
from typing import *
from base import *


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]表示到当前金额最低需要的硬币次数
        if amount == 0:
            return 0
        dp = [amount+100 for i in range(amount+1)]
        stack = [] # 存当前空的队列
        for i in coins:
            if i > amount:
                continue
            dp[i] = 1
            stack.append(i)
        stack.sort()
        while stack:
            index = stack.pop(0)
            for i in coins:
                tmp = index + i
                if tmp == amount:
                    dp[amount] = min(dp[index] + 1, dp[amount])
                elif tmp < amount:
                    dp[tmp] = min(dp[index] + 1, dp[tmp])
                    if tmp not in stack:
                        stack.append(tmp)
                        stack.sort()
        if dp[amount] > amount + 1:
            return -1
        return dp[amount]

    def coinChange1(self, coins: List[int], amount: int) -> int:
        """
        执行用时：
1424 ms
, 在所有 Python3 提交中击败了
43.49%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
57.40%
的用户
        """
        # dp[i] 表示到达当前价格需要的最少零钱数
        # 因为要求最少次数，所以初始化用大数
        dp = [amount + 100 for i in range(amount+1)]
        dp[0] = 0
        # 给每个coin都从0到amount+1进行遍历
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        if dp[amount] > amount+1:
            return -1
        return dp[amount]


if __name__ == '__main__':
    nums = [1, 2, 5]
    k = 11
    nums = [2]
    k = 1
    nums = [175,148,417,221,31,198,409,83,21,181]
    k = 1594
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.coinChange(nums, k))
    print(solution.coinChange1(nums, k))
    print(solution.coinChange2(nums, k))
    pass