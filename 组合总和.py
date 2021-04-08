#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
39. 组合总和

示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
]

https://leetcode-cn.com/problems/combination-sum/
"""
from typing import *
from base import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        执行用时：
56 ms
, 在所有 Python3 提交中击败了
80.63%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
90.44%
的用户
        """
        # dfs
        len_c = len(candidates)
        res = []
        # 先排序
        candidates.sort()

        # 递归做
        def dfs(stack, index):
            # 记录和，如果和超了，就不需要继续了
            sum_ = sum(stack)
            if sum_ == target:
                res.append(stack.copy())
                return False
            if sum_ > target:
                return False
            # 因为可以重复，所有从当前位置开始
            for i in range(index, len_c):
                stack.append(candidates[i])
                tmp = dfs(stack, index)
                stack.remove(candidates[i])
                # 当前位置算完后，在继续下一个位置
                index += 1
                # 如果已经超了，直接返回
                if not tmp:
                    return True
            return True

        dfs([], 0)
        return res


if __name__ == '__main__':
    nums = [2,3,6,7]
    k = 7
    nums = [2, 3, 5]
    k = 8
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.combinationSum(nums, k))
