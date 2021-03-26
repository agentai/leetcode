#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/7

"""
文件说明：
    131. 分割回文串
    https://leetcode-cn.com/problems/palindrome-partitioning/
"""
from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        """
        执行用时：
128 ms
, 在所有 Python3 提交中击败了
80.09%
的用户
内存消耗：
31 MB
, 在所有 Python3 提交中击败了
55.21%
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

    def partition2(self, s: str) -> List[List[str]]:
        """

        执行用时：
184 ms
, 在所有 Python3 提交中击败了
25.16%
的用户
内存消耗：
30.8 MB
, 在所有 Python3 提交中击败了
61.26%
的用户

        :param s:
        :return:
        """
        len_s = len(s)

        def is_palindrome(tmp_s):
            i = 0
            j = len(tmp_s) - 1
            while i <= j:
                if tmp_s[i] == tmp_s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == len_s:
                ret.append(ans[:])
                return

            for j in range(i, len_s):
                if is_palindrome(s[i:j + 1]):
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret



    def partition1(self, s: str) -> List[List[str]]:
        """

        执行用时：
304 ms
, 在所有 Python3 提交中击败了
5.91%
的用户
内存消耗：
43.3 MB
, 在所有 Python3 提交中击败了
5.01%
的用户

        :param s:
        :return:
        """
        len_s = len(s)
        all = []

        def is_palindrome(tmp_s):
            i = 0
            j = len(tmp_s) - 1
            while i <= j:
                if tmp_s[i] == tmp_s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        def dfs(tmp_s, res):
            if len(tmp_s) == 1:
                res += "," + tmp_s
            for i in range(1, len(tmp_s)+1):
                if is_palindrome(tmp_s[0:i]):
                    res1 = res + "," + tmp_s[0:i]
                    dfs(tmp_s[i:], res1)
            if len(res.replace(",", "")) == len_s:
                if res[0] == ",":
                    res = res[1:]
                all.append(res.split(","))
        dfs(s, "")
        return all


if __name__ == '__main__':
    nums = "aab"
    # nums = "aa"
    solution = Solution()
    print(solution.partition(nums))
    pass
