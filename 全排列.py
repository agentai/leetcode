#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    46. 全排列
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

https://leetcode-cn.com/problems/permutations/

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
27.80%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
66.70%
的用户
        """
        # 递归 + 栈
        res = [] # 存最终结果
        # 递归函数
        def sub_problem(item, remain):
            if not remain:
                # 如果没有可分配的了，copy item，加到结果中
                res.append(item.copy())
                return
            # 循环取remain里的数
            for i in range(len(remain)):
                # 用tmp记录这个数，在remian里去掉对应的数加到item里
                tmp = remain.pop(i)
                item.append(tmp)
                # 递归求解
                sub_problem(item, remain)
                # item去掉最好一个数
                item.pop(-1)
                # remain加回来tmp
                remain.insert(i, tmp)
        sub_problem([], nums)
        return res


if __name__ == '__main__':
    k = [1,2,3]
    solution = Solution()
    print(solution.permute(k))

    pass