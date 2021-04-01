#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    22. 括号生成
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

https://leetcode-cn.com/problems/generate-parentheses/

"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
30.71%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
84.80%
的用户
        """
        # 递归 + 字典判断，字典里存当前字符串的括号数
        res = []
        def generate(item, cur):
            if len(item) == n*2:
                res.append(item)
                return
            # 还有左括号的话，继续加左括号，并且递归
            if cur[0] > 0:
                item1 = item + "("
                generate(item1, [cur[0]-1, cur[1]])
            if cur[0] < cur[1]:
                item1 = item + ")"
                generate(item1, [cur[0], cur[1]-1])
        generate("", [n, n])
        return res


if __name__ == '__main__':
    k = 3
    solution = Solution()
    print(solution.generateParenthesis(k))

    pass