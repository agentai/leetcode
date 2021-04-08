#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/15

"""
文件说明：
76. 最小覆盖子串

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"

https://leetcode-cn.com/problems/minimum-window-substring/
    
"""
from typing import List
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        执行用时：
68 ms
, 在所有 Python3 提交中击败了
99.48%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
98.89%
的用户
        """
        # 滑动窗口来求解
        need = collections.defaultdict(int)
        # 先统计需要多少字符
        for c in t:
            need[c] += 1
        # 用needCnt记录需要的字符个数
        need_length = len(t)
        l = 0 # 窗口的左边
        res = (0, len(s) + 1) # 记录需要的区间长度
        for r, c in enumerate(s):
            # 如果当前字符是需要的，需要的字符数减1，需要的长度减1
            if need[c] > 0:
                need_length -= 1
            need[c] -= 1
            # 如果包含了所有元素，走左边，去掉左边可能的多余元素
            if need_length == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加l，排除多余元素
                    c = s[l]
                    # 如果没有多余，退出
                    if need[c] == 0:
                        break
                    need[c] += 1
                    l += 1
                # 如果有比当前结果小的，记录结果
                if r - l < res[1] - res[0]:
                    res = (l, r)
                # 如果左边右移了，对应的需要的字符串也要加回去
                need[s[l]] += 1  # 步骤三：l增加一个位置，寻找新的满足条件滑动窗口
                need_length += 1
                l += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果



if __name__ == '__main__':
    nums = "ADOBECODEBANC"
    b = "ABC"
    nums = "a"
    b = "a"
    solution = Solution()
    print(solution.minWindow(nums, b))
    pass
