#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/20

"""
文件说明：
    131. 分割回文串
    https://leetcode-cn.com/problems/palindrome-partitioning/
    给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 思路：dp[i][j]表示s[i][j]是回文串
        # 先用dp来存i-j是否说回文串
        # 在递归对字符串进行分割
        len_s = len(s)
        dp = [[1] * len_s for i in range(len_s)]
        for i in range(len_s - 1, -1, -1):
            for j in range(i+1, len_s):
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == len_s:
                ret.append(ans[:])
                return

            for j in range(i, len_s):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret


    def partition1(self, s: str) -> List[List[str]]:
        """
        执行用时：
144 ms
, 在所有 Python3 提交中击败了
63.14%
的用户
内存消耗：
30.9 MB
, 在所有 Python3 提交中击败了
50.54%
的用户
        :param s:
        :return:
        """
        len_s = len(s)
        dp = [[1] * len_s for x in range(len_s)]
        i = len_s - 1
        while i >= 0:
            j = i+1
            while j < len_s:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
                j += 1
            i -= 1
        # for i in range(len_s - 1, -1, -1):
        #     for j in range(i + 1, len_s):
        #         dp[i][j] = int((s[i] == s[j]) and dp[i + 1][j - 1])


        ret = list()
        ans = list()

        def dfs(i: int):
            if i == len_s:
                ret.append(ans[:])
                return

            for j in range(i, len_s):
                if dp[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return ret


if __name__ == '__main__':
    nums = "aab"
    solution = Solution()
    print(solution.partition(nums))
    pass
