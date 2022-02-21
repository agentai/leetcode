#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

"""
from typing import *
from base import *


class Solution:
    """
    执行用时：
144 ms
, 在所有 Python3 提交中击败了
35.35%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
40.91%
的用户
    """
    def multiply(self, num1: str, num2: str) -> str:
        # 对位相乘，并存储结果
        # 最长位数为m+n
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                tmp = int(num1[i]) * int(num2[j]) + res[i + j + 1]
                res[i + j + 1] = tmp % 10
                res[i + j] += tmp // 10
        print(res)
        while res and res[0] == 0:
            res = res[1:]
        if len(res) == 0:
            return "0"
        return "".join([str(x) for x in res])


if __name__ == '__main__':
    nums = "123"
    k = "456"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.multiply(nums, k))
    pass