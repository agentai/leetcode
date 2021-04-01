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

"""
from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
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


if __name__ == '__main__':
    k = [1,2,2]
    solution = Solution()
    print(solution.subsetsWithDup(k))

    pass