#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
394. 字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
示例 2：

输入：s = "3[a2[c]]"
输出："accaccacc"
示例 3：

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"
示例 4：

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

https://leetcode-cn.com/problems/decode-string

"""
from typing import *
from base import *


class Solution:
    def decodeString(self, s: str) -> str:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
81.14%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
31.84%
的用
        """
        # 递归生成字符串
        len_s = len(s)

        def sub(cur):
            # cur 为当前索引
            num = 0 # 记录是否有数字
            tmp = ""
            while cur < len_s:
                # 读取数字
                i = cur
                while i < len_s and s[i] in "0123456789":
                    i += 1
                if i > cur:
                    # 有数字的话，记录数字，并跳过
                    num = int(s[cur:i])
                    cur = i
                    continue
                # 如果遇到 [ 递归处理
                if cur < len_s and s[cur] == "[":
                    # 递归返回 处理后的串 + 索引
                    tmp_res, cur = sub(cur + 1)
                    # 加上返回的串，如果有num，乘上
                    if num > 0:
                        tmp += tmp_res * num
                        num = 0
                    else:
                        tmp += tmp_res
                    continue
                # 如果遇到 ] 处理当前串，并返回
                if cur == len_s or s[cur] == "]":
                    if num > 0:
                        tmp = tmp * num
                    return tmp, min(len_s, cur+1)
                # 如果都不是，则加上当前字符
                tmp += s[cur]
                cur += 1
            return tmp, cur
        res, cur = sub(0)
        return res


if __name__ == '__main__':
    # nums = "3[a2[c]]"
    # nums = "2[abc]3[cd]ef"
    # nums = "abc3[cd]xyz"
    nums = "3[a]2[bc]"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.decodeString(nums))
    pass