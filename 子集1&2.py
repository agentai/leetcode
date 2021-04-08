#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    90. 子集 II

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

https://leetcode-cn.com/problems/subsets-ii/


78. 子集
示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

https://leetcode-cn.com/problems/subsets/

"""
from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
20.11%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
77.75%
的用户
        """
        # 排序后回溯
        len_n = len(nums)
        if len_n == 0:
            return [[]]
        # 排序
        nums.sort()
        res = []

        # 回溯算
        def dfs(cur, i):
            if i < len_n:
                # 加一个数
                cur.append(nums[i])
                # 递归算
                dfs(cur, i + 1)
                # 减去当前加的数，在递归算
                cur.pop()
                dfs(cur, i + 1)
            else:
                if cur not in res:
                    res.append(cur.copy())

        dfs([], 0)
        return res

    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        """90
        执行用时：
56 ms
, 在所有 Python3 提交中击败了
10.18%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
5.98%
的用户
        """
        # 排序后回溯
        len_n = len(nums)
        if len_n == 0:
            return [[]]
        # 排序
        nums.sort()
        # 回溯算
        def sub_problem(i):
            cur = nums[i-1]
            # 到1的时候，返回特定组合
            if i == 1:
                return [[cur], []]
            items = sub_problem(i-1)
            # 构建新的组合
            new_items = [[cur]]
            for item in items:
                if item not in new_items:
                    new_items.append(item.copy())
                item.append(cur)
                if item not in new_items:
                    new_items.append(item)
            return new_items
        return sub_problem(len_n)

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
7.88%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
15.14%
的用户
        """
        # 递归加
        def sub_job(i):
            if i == 0:
                return [[], [nums[0]]]
            items = sub_job(i - 1)
            new_items = [[nums[i]]]
            for item in items:
                if item not in new_items:
                    new_items.append(item.copy())
                item.append(nums[i])
                if item not in new_items:
                    new_items.append(item.copy())
            return new_items

        return sub_job(len(nums) - 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
35.61%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
96.07%
的用户
        """
        # 递归加
        len_n = len(nums)
        res = []

        def dfs(cur, index):
            if index < len_n:
                cur.append(nums[index])
                dfs(cur, index + 1)
                cur.pop()
                dfs(cur, index + 1)
            else:
                res.append(cur.copy())

        dfs([], 0)
        return res


if __name__ == '__main__':
    k = [1,2,3]
    solution = Solution()
    # print(solution.subsetsWithDup(k))
    print(solution.subsets(k))

    pass