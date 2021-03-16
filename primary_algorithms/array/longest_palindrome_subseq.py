#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/7

"""
文件说明：
    516. 最长回文子序列
    https://leetcode-cn.com/problems/longest-palindromic-subsequence/
"""
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        执行用时：
1784 ms
, 在所有 Python3 提交中击败了
24.69%
的用户
内存消耗：
31 MB
, 在所有 Python3 提交中击败了
44.58%
的用户

        :param s:
        :return:
        """
        len_s = len(s)
        dp = [[0] * len_s for i in range(len_s)]
        for index in range(len_s):
            dp[index][index] = 1
        i = len_s-1
        while i >= 0:
            j = i + 1
            while j < len_s:
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                j += 1
            i -= 1
        return dp[0][len_s-1]

        pass


if __name__ == '__main__':
    nums = "bbbab"
    solution = Solution()
    print(solution.longestPalindromeSubseq(nums))
    pass
