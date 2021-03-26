#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/1

"""
文件说明：
    3. 无重复字符的最长子串
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""
from typing import List


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        执行用时：
84 ms
, 在所有 Python3 提交中击败了
46.79%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
71.64%
的用户
        """
        # 思路，滑动窗口，队列用来做滑动窗口，遇到重复的了，判断长度，再左边前进，直到遇到当前值
        len_s = len(s)
        max_l = 0
        # 队列用来作为滑动窗口
        data = []
        i = 0
        while i < len_s:
            if s[i] not in data:
                data.append(s[i])
            else:
                max_l = max(max_l, len(data))
                # 左边前进，一直到遇到当前值
                while data and data[0] != s[i]:
                    data = data[1:]
                # 去掉原先的当前值，加的对尾
                data = data[1:]
                data.append(s[i])
            i += 1
        return max(len(data), max_l)

    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        执行用时：
324 ms
, 在所有 Python3 提交中击败了
15.19%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
54.82%
的用户
        """
        # 用一个数字记录最大子串长度
        # 用一个字典存数据记录字符+索引，依次遍历，如果遇到已存在的字符，提出这个字符的索引，去掉字典中这个索引之前的所有字符，并比较长度
        max_l = 0
        data = {}
        for i in range(len(s)):
            if s[i] not in data:
                # 如果不存在，加入索引并继续走
                data[s[i]] = i
            else:
                # 如果存在，遍历字典，去掉索引之前的所有内容
                max_l = max(max_l, len(data))
                cur = data[s[i]]
                for k,v in list(data.items()):
                    if v <= cur:
                        data.pop(k)
                # 处理完后，加上当前索引
                data[s[i]] = i
        return max(len(data), max_l)


if __name__ == '__main__':
    nums = "abcabcbb"
    nums = "pwwkew"
    # nums = "aab"
    # nums = " "
    # nums = "ynyo"
    nums = "aabaab!bb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(nums))
    print(solution.lengthOfLongestSubstring1(nums))
    pass

