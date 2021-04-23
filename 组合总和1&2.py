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


40. 组合总和 II
给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例1:

输入: candidates =[10,1,2,7,6,1,5], target =8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例2:

输入: candidates =[2,5,2,1,2], target =5,
所求解集为:
[
 [1,2,2],
 [5]
]

https://leetcode-cn.com/problems/combination-sum-ii
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

    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
89.71%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
53.31%
的用户
        """
        candidates.sort()
        len_c = len(candidates)
        res = []

        def dfs(k, cur, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            if remain < 0:
                return
            for i in range(k, len_c):
                # 如果 剩余的小于当前值，直接跳出
                if remain < candidates[i]:
                    break
                if cur and candidates[i] < cur[-1]:
                    continue
                cur.append(candidates[i])
                dfs(k, cur, remain-candidates[i])
                cur.pop()

        dfs(0, [], target)
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
90.74%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
36.49%
的用户
        """
        candidates.sort()
        res = []
        len_c = len(candidates)

        def dfs(k, cur, remain):
            if remain == 0:
                res.append(cur.copy())
                return
            if remain < 0:
                return
            i = k
            while i < len_c:
                while k < i < len_c and candidates[i] == candidates[i - 1]:
                    i += 1
                if i == len_c:
                    break
                if candidates[i] > remain:
                    break
                cur.append(candidates[i])
                dfs(i+1, cur, remain - candidates[i])
                cur.pop()
                i += 1
        dfs(0, [], target)
        return res


if __name__ == '__main__':
    nums = [2,3,6,7]
    k = 7
    # nums = [2, 3, 5]
    # k = 8
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.combinationSum(nums, k))
    print(solution.combinationSum1(nums, k))
    nums = [10, 1, 2, 7, 6, 1, 5]
    k = 8
    print(solution.combinationSum2(nums, k))
