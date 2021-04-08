#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
730. 统计不同回文子序列

示例 1：

输入：
S = 'bccb'
输出：6
解释：
6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。
示例 2：

输入：
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：
共有 3104860382 个不同的非空回文子序列，对 10^9 + 7 取模为 104860361。

https://leetcode-cn.com/problems/count-different-palindromic-subsequences/

提示：

字符串 S 的长度将在[1, 1000]范围内。
每个字符 S[i] 将会是集合 {'a', 'b', 'c', 'd'} 中的某一个。

"""
from typing import *
from base import *


class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        """
        执行用时：
4188 ms
, 在所有 Python3 提交中击败了
31.69%
的用户
内存消耗：
49.3 MB
, 在所有 Python3 提交中击败了
48.59%
的用户
        """
        # 思路，定义dp[x][i][j]，表示字母x在 s[i...j]上所有回文子串的个数
        # x in {a,b,c,d} -> {0,1,2,3}
        # 分别记录四个字母在子串ij上的所有回文个数，将它们求和就是最终的回文个数
        # if s[i] == s[j] == x==0 dp[0][i][j] = 2 + dp[0][i+1][j-1] + dp[1][i+1][j-1] + dp[2][i+1][j-1] + dp[3][i+1][j-1]
        len_s = len(S)
        dp = [[[0] * len_s for i in range(len_s)] for j in range(4)]
        mod = 1000000007

        for i in range(len_s-1, -1, -1):
            for j in range(i, len_s):
                for k in range(4):
                    # 当前数值对应的字符
                    c = chr(ord("a") + k)
                    if i == j:
                        # 如果i和j相等，表示ij重合，对应的字符的子串个数为1，其他字符的子串个数为0
                        if S[i] == c:
                            dp[k][i][i] = 1
                        else:
                            dp[k][i][i] = 0
                    else:
                        if S[i] != c:
                            dp[k][i][j] = dp[k][i+1][j]
                        elif S[j] != c:
                            dp[k][i][j] = dp[k][i][j-1]
                        else: # s[i] == s[j] == c
                            if j == i+1:
                                dp[k][i][j] = 2 # 特殊情况，两个字符相等，a, aa
                            else:
                                dp[k][i][j] = 2
                                for z in range(4):
                                    dp[k][i][j] += dp[z][i+1][j-1]
                                    # 结果取mod
                                    dp[k][i][j] %= mod
        res = 0
        for k in range(4):
            res += dp[k][0][len_s-1]
            res %= mod
        return res


if __name__ == '__main__':
    nums = 'bccb'
    nums = "abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba"
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.countPalindromicSubsequences(nums))
    pass