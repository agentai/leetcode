#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    8. 字符串转换整数 (atoi)
输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。

https://leetcode-cn.com/problems/string-to-integer-atoi/

"""
from typing import List


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
86.33%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
65.84%
的用户
        """
        # 暴力遍历，要注意各种特例
        len_s = len(s)
        i = 0
        res = ""
        while i < len_s:
            # 当是空格且res还没有值时，一直往前走
            while i < len_s and s[i] == " " and res == "":
                i += 1
            if i == len_s:
                return 0
            # 如果是加减，且存在字符了，则跳出
            if s[i] in "+-" and len(res) > 0:
                break
            elif s[i] not in "1234567890+-":
                break
            else:
                res += s[i]
            i += 1
        if res == "" or res == "-" or res == "+":
            return 0
        tmp = int(res)
        if res.startswith("-"):
            a = -2 ** 31
            if tmp < a:
                return a
        else:
            b = 2 ** 31 - 1
            if tmp > b:
                return b
        return tmp


if __name__ == '__main__':
    nums = "+1"
    nums = "00000-42a1234"
    solution = Solution()
    print(solution.myAtoi(nums))

    pass
