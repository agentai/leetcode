#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
151. 翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。

说明：

无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


示例 1：

输入："the sky is blue"
输出："blue is sky the"
示例 2：

输入：" hello world! "
输出："world! hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入："a good  example"
输出："example good a"
解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例 4：

输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"
示例 5：

输入：s = "Alice does not even like bob"
输出："bob like even not does Alice"

https://leetcode-cn.com/problems/reverse-words-in-a-string
"""
from typing import *
from base import *


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        执行用时：
64 ms
, 在所有 Python3 提交中击败了
7.15%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
82.50%
的用户
        """
        len_s = len(s)
        i = 0
        data = ""
        while i < len_s:
            while i < len_s and s[i] == " ":
                i += 1
            j = i
            while j < len_s and s[j] != " ":
                j += 1
            if j > i:
                if data:
                    data = s[i:j] + " " + data
                else:
                    data = s[i:j]
                i = j
            else:
                i += 1
        return data


if __name__ == '__main__':
    nums = "  Bob    Loves  Alice   "
    nums = "  hello world!  "
    nums = "the sky is blue"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.reverseWords(nums))
    pass