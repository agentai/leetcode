#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/7

"""
文件说明：
    516. 最长回文子序列
示例 1:
输入:
"bbbab"
输出:
4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:
"cbbd"
输出:
2
一个可能的最长回文子序列为 "bb"。
    https://leetcode-cn.com/problems/longest-palindromic-subsequence/
"""
from typing import List


class Solution:
    def longestPalindromeSubseq4(self, s: str) -> int:
        """
        执行用时：
1488 ms
, 在所有 Python3 提交中击败了
52.33%
的用户
内存消耗：
31 MB
, 在所有 Python3 提交中击败了
51.21%
的用户
        """
        # 思路，dp是一个二维表，横是序列s，竖也是序列s，dp[i][j]表示s[i:j]之间最长子串
        # 每次迭代，计算当前范围下的最长子串，即dp[i][j]，
        # 先从最右边开始遍历，当s[i]==s[j]的时候，ij之间最长子串对应的是dp[i+1][j-1]+2
        # 当不相等的话，ij之间最长子串取的是dp[i+1][j]和dp[i][j-1]的最大值
        # dp初始化时，先所有元素都为0，然后对角线上设为1
        # 最后0:len_s-1之间最长子串就是最终的结果
        len_s = len(s)
        dp = [[0] * len_s for i in range(len_s)]
        for i in range(len_s):
            dp[i][i] = 1
        for i in range(len_s-1, -1, -1):
            for j in range(i+1, len_s):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len_s-1]

    def longestPalindromeSubseq1(self, s: str) -> int:
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

    def longestPalindromeSubseq(self, s: str) -> int:
        """执行用时：
1372 ms
, 在所有 Python3 提交中击败了
67.77%
的用户
内存消耗：
30.9 MB
, 在所有 Python3 提交中击败了
81.25%
的用户"""
        # dp[i][j] 表示s[i:j]之间的最长子串长度
        len_s = len(s)
        dp = [[0] * len_s for i in range(len_s)]
        for i in range(len_s-1, -1, -1):
            for j in range(i, len_s):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len_s-1]

    def longestPalindromeSubseqaa(self, s: str) -> int:
        # dp[i][j]表示s[i:j]之间最长的回文子串长度
        # 如果s[i]==s[j] dp[i][j] = dp[i+1][j-1] + 2
        # 如果不等 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # 如果 i==j ，dp[i][j]=1
        # 如果 j == i+1 and s[i]== s[j] , dp[i][j] = 2
        len_s = len(s)
        dp = [[0] * len_s for i in range(len_s)]
        for i in range(len_s-1, -1, -1):
            for j in range(i, len_s):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    if j == i+1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


if __name__ == '__main__':
    nums = "bbbab"
    solution = Solution()
    print(solution.longestPalindromeSubseq(nums))
    print(solution.longestPalindromeSubseq4(nums))
    print(solution.longestPalindromeSubseqaa(nums))
    pass
