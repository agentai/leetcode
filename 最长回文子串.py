#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/7

"""
文件说明：
5. 最长回文子串
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
https://leetcode-cn.com/problems/longest-palindromic-substring/
409. 最长回文串
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
https://leetcode-cn.com/problems/longest-palindrome/
"""
from typing import List


class Solution:
    def longestPalindrome409(self, s: str) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
48.88%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
37.42%
的用户
        :param s:
        :return:
        """
        words = set()
        res = 0
        for word in s:
            if word in words:
                res += 1
                words.remove(word)
            else:
                words.add(word)
        return res * 2 + int(len(words) > 0)

    def longestPalindrome5(self, s: str) -> str:
        """
        执行用时：
4820 ms
, 在所有 Python3 提交中击败了
42.45%
的用户
内存消耗：
22.5 MB
, 在所有 Python3 提交中击败了
20.62%
的用户
        :param s:
        :return:
        """
        # 思路：dp[i][j]=1 表示s[i:j]是回文串，先初始化dp全为1，然后i从后往前遍历，j从i+1往后遍历
        len_s = len(s)
        if len_s <= 1:
            return s
        max_s = s[0]
        max_len = 1
        dp = [[1] * len_s for x in range(len_s)]
        for i in range(len_s - 1, -1, -1):
            for j in range(i + 1, len_s):
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    if j+1 - i > max_len:
                        max_s = s[i:j + 1]
                        max_len = len(max_s)
                else:
                    dp[i][j] = 0
        return max_s

    def longestPalindrome5_1(self, s: str) -> str:
        # 从前往后遍历，比较麻烦
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans

    def longestPalindrome(self, s: str) -> str:
        """
        执行用时：
8204 ms
, 在所有 Python3 提交中击败了
23.80%
的用户
内存消耗：
31.1 MB
, 在所有 Python3 提交中击败了
5.28%
的用户
        """
        # dp[i][j] = 1 表示s[i:j]是回文串
        len_s = len(s)
        if len_s <= 1:
            return s
        dp = [[0] * len_s for i in range(len_s)]
        max_l = 1
        max_s = s[0]
        for i in range(len_s - 1, -1, -1):
            for j in range(i, len_s):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j] and j - i == 1:
                    dp[i][j] = 2
                    if j + 1 - i > max_l:
                        max_s = s[i:j + 1]
                        max_l = j + 1 - i
                elif s[i] == s[j] and dp[i + 1][j - 1] >= 1:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    if j + 1 - i > max_l:
                        max_s = s[i:j + 1]
                        max_l = j + 1 - i
        return max_s


if __name__ == '__main__':
    nums = "abccccddddda"
    # nums = "babad"
    # nums = "ac"
    solution = Solution()
    print(solution.longestPalindrome(nums))
    pass
