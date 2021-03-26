#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    189. 旋转数组
    https://leetcode-cn.com/problems/rotate-array/
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
"""
from typing import List


class Solution:

    def reverse(self, x: int) -> int:
        """
        执行用时：
60 ms
, 在所有 Python3 提交中击败了
6.07%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
42.30%
的用户
        """
        # 思路：先转成字符串，然后保留负号，去掉末尾多余0，然后反转字符串，然后转int
        if x < 0:
            s = str(-x)
        else:
            s = str(x)
        l = 0
        r = len(s) - 1
        tmp = [""] * (r + 1)
        while l <= r:
            tmp[l], tmp[r] = s[r], s[l]
            l += 1
            r -= 1
        if x < 0:
            res = -int("".join(tmp))
            if res < -2**31:
                return 0
        else:
            res = int("".join(tmp))
            if res > 2**31 - 1:
                return 0
        return res


if __name__ == '__main__':
    nums = 1563847412
    solution = Solution()
    print(solution.reverse(nums))
    pass
