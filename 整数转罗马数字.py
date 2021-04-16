#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
12. 整数转罗马数字

罗马数字包含以下七种字符：I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给定一个整数，将其转为罗马数字。输入确保在 1到 3999 的范围内。


示例1:

输入:3
输出: "III"
示例2:

输入:4
输出: "IV"
示例3:

输入:9
输出: "IX"

示例4:

输入:58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
示例5:

输入:1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

https://leetcode-cn.com/problems/integer-to-roman

"""
from typing import *
from base import *


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
96.37%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
38.54%
的用户
        """
        res = ""
        # 算超1000部分
        for i in range(num // 1000):
            res += "M"
        num %= 1000
        # 算超900部分
        if num >= 900:
            num -= 900
            res += "CM"
        # 算超500部分
        for i in range(num // 500):
            res += "D"
        num %= 500
        # 算超400部分
        if num >= 400:
            num -= 400
            res += "CD"
        # 算超100部分
        for i in range(num // 100):
            res += "C"
        num %= 100
        # 算超90部分
        if num >= 90:
            num -= 90
            res += "XC"
        # 算超50部分
        for i in range(num // 50):
            res += "L"
        num %= 50
        # 算超40部分
        if num >= 40:
            num -= 40
            res += "XL"
        # 算超10部分
        for i in range(num // 10):
            res += "X"
        num %= 10
        # 算超9部分
        if num >= 9:
            num -= 9
            res += "IX"
        # 算超5部分
        for i in range(num // 5):
            res += "V"
        num %= 5
        # 算超4部分
        if num >= 4:
            num -= 4
            res += "IV"
        for i in range(num):
            res += "I"

        return res


if __name__ == '__main__':
    nums = 40
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.intToRoman(nums))
    pass