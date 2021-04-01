#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    33. 搜索旋转排序数组
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
36.20%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
91.10%
的用户
        """
        # 二分查找
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # k不在l,m之间,l,m之间单调
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # k 不在m,r之间，m,r单调
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    k = 0
    nums = [5,1,3]
    k = 5
    nums = [1, 3]
    k = 3
    nums = [3, 1]
    k = 1
    solution = Solution()
    print(solution.search(nums, k))
    list(filter(lambda x:x>2, [1,2,3,5]))

    pass