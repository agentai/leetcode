#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

"""
from typing import *
from base import *


class Solution:
    """
    执行用时：
1068 ms
, 在所有 Python3 提交中击败了
5.64%
的用户
内存消耗：
21.4 MB
, 在所有 Python3 提交中击败了
22.58%
的用户
    """
    def pushDominoes(self, dominoes: str) -> str:
        # 表示从左往右推的序列
        dp0 = [0] * len(dominoes)
        # 表示从右往左推的序列
        dp1 = [0] * len(dominoes)
        res = ""
        l = 0
        while l < len(dominoes):
            if l > 0 and dp0[l-1] > 0 and dominoes[l] == ".":
                # 数字从大到小排列
                dp0[l] = dp0[l-1] - 1
            elif dominoes[l] == "R":
                dp0[l] = len(dominoes)
            r = len(dominoes) - 1 - l
            if r < len(dominoes) - 1 and dp1[r+1] > 0 and dominoes[r] == ".":
                dp1[r] = dp1[r+1] - 1
            elif dominoes[r] == "L":
                dp1[r] = len(dominoes)
            print(dominoes[l], dominoes[r])
            l += 1
        i = 0
        while i < len(dominoes):
            if dp0[i] > dp1[i]:
                res += "R"
            elif dp0[i] < dp1[i]:
                res += "L"
            else:
                res += "."
            i += 1
        return res


if __name__ == '__main__':
    nums = "RR.L"
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.pushDominoes(nums))
    pass