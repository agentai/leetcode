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
304 ms
, 在所有 Python3 提交中击败了
13.95%
的用户
内存消耗：
16.1 MB
, 在所有 Python3 提交中击败了
5.21%
的用户
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        def quick_sort(nums, l, r):
            if l >= r:
                return
            base = nums[r]
            base_index = l
            for i in range(l, r):
                if nums[i] <= base:
                    nums[i], nums[base_index] = nums[base_index], nums[i]
                    base_index += 1
            nums[base_index], nums[r] = nums[r], nums[base_index]
            quick_sort(nums, l, base_index - 1)
            quick_sort(nums, base_index + 1, r)

        quick_sort(nums, 0, len(nums) - 1)
        res = -10000
        i = 0
        while i < len(nums) - 2:
            l = i + 1
            r = len(nums) - 1
            aim = target - nums[i]
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == aim:
                    return target
                if abs(res - target) > abs(aim - tmp):
                    res = tmp + nums[i]
                if tmp < aim:
                    l += 1
                else:
                    r -= 1
            i += 1
        return res


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    k = 1
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.threeSumClosest(nums, k))
    pass