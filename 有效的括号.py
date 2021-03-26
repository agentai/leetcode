#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/16

"""
文件说明：
    20. 有效的括号
输入：s = "()"
输出：true

输入：s = "(]"
输出：false

    https://leetcode-cn.com/problems/valid-parentheses/
"""
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """执行用时：
60 ms
, 在所有 Python3 提交中击败了
7.05%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
54.90%
的用户"""
        # 思路：栈 + 字典
        # 用栈存左括号，字典存右括号对应的左括号，遇到右括号，判断栈顶是否是对应的左括号
        stark = []
        data = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in ")]}":
                if not stark or stark[-1] != data[i]:
                    return False
                else:
                    stark.pop()
            else:
                stark.append(i)
        return not stark


if __name__ == '__main__':
    s = "()]"
    solution = Solution()
    print(solution.isValid(s))
    pass