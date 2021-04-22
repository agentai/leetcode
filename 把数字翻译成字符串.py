#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
"""
from typing import *
from base import *


class Solution:
    def translateNum(self, num: int) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
29.31%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
76.08%
的用户
        """
        # dp[i]表示从s[i:len_s]一个有多少中翻译
        # s[i]!=0
        s = str(num)
        len_s = len(s)
        dp = [0] * len_s

        for i in range(len_s-1, -1, -1):
            # 最后一位的话默认是1
            if i == len_s - 1:
                dp[i] = 1
            else:
                # 其他位置等于其后一个位置
                dp[i] = dp[i+1]
                # 如果当前位置是0，只有一种编码
                if s[i] == "0":
                    continue
                # 当前位置不是0，判断双数是否合理，合理的话加上
                if int(s[i:i+2]) < 26:
                    if i == len_s - 2:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i+2]

        return dp[0]


if __name__ == '__main__':
    nums = 12258
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.translateNum(nums))
    pass