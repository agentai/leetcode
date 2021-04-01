#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    17. 电话号码的字母组合
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
    https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
31.10%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
77.80%
的用户
        """
        # 字典+递归，每次递归，传入到目前为止所有组合+当前的数字
        data = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        def get_str(src_list, cur):
            tmp = []
            for src in src_list:
                for i in data[cur]:
                    tmp.append(src+i)
            return tmp
        res = [""]
        for i in digits:
            res = get_str(res, i)
        return res


if __name__ == '__main__':
    nums = "23"
    solution = Solution()
    print(solution.letterCombinations(nums))
    pass
