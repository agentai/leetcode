#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
    6. Z 字形变换
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

https://leetcode-cn.com/problems/zigzag-conversion/

"""
from typing import List


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        执行用时：
72 ms
, 在所有 Python3 提交中击败了
42.61%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
31.97%
的用户
        """
        # 求每个位置的相对距离，先算周期，然后不同位置处理方式不同
        # 先算周期
        between = numRows + numRows - 2
        len_s = len(s)
        # 如果numRows<2，直接返回s
        if numRows < 2:
            return s
        res = ""
        for i in range(numRows):
            # 当在首尾的时候，j=i
            if i == 0 or i == numRows-1:
                j = i
                while j < len_s:
                    res += s[j]
                    j += between
            else:
                # 其他情况，有两个索引，i, between-i
                start = [i, between-i]
                # 需一直到左边索引也到底
                while start[0] < len_s:
                    res += s[start[0]]
                    if start[1] < len_s:
                        res += s[start[1]]
                    start = [start[0]+between, start[1]+between]
        return res


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    k = 3
    solution = Solution()
    print(solution.convert(s, k))

    pass