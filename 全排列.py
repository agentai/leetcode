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
    def permute1(self, nums: List[int]) -> List[List[int]]:
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
                # item去掉最后一个数
                item.pop(-1)
                # remain加回来tmp
                remain.insert(i, tmp)
        sub_problem([], nums)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
77.42%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
39.36%
的用户
        """
        res = []

        def dfs(stack):
            if len(nums) == 0:
                res.append(stack.copy())
                return
            for i in range(len(nums)):
                tmp = nums.pop(i)
                stack.append(tmp)
                dfs(stack)
                nums.insert(i, tmp)
                stack.pop(-1)

        dfs([])
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """执行用时：
64 ms
, 在所有 Python3 提交中击败了
38.45%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
22.41%
的用户
"""
        res = []
        nums.sort()
        def dfs(stack):
            if len(nums) == 0:
                if stack not in res:
                    res.append(stack.copy())
                return
            for i in range(len(nums)):
                # 加速
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                tmp = nums.pop(i)
                stack.append(tmp)
                dfs(stack)
                stack.pop()
                nums.insert(i, tmp)
        dfs([])
        return res


if __name__ == '__main__':
    k = [1,2,3]
    solution = Solution()
    print(solution.permute(k))
    print(solution.permute1(k))
    print(solution.permuteUnique([1,2,3]))
    print(solution.permuteUnique([1,1,3]))

    pass