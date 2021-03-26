#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
34. 在排序数组中查找元素的第一个和最后一个位置
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
执行用时：
32 ms
, 在所有 Python3 提交中击败了
96.93%
的用户
内存消耗：
15.6 MB
, 在所有 Python3 提交中击败了
44.33%
的用户
        """
        # 思路 二分查找，最后在往左右走
        def find(l, r):
            # 当两者差距小于等于1时，细致判断，因为可能存在没有target的情况
            if r - l <= 1:
                if nums[r] != target and nums[l] != target:
                    return -1
                elif nums[r] == target:
                    return r
                return l
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return find(l, m)
            else:
                return find(m, r)
        i = find(0, len(nums)-1)
        # 判断是否有target
        if i < 0 or nums[i] != target:
            return [-1, -1]
        else:
            # 有target的话，找最左和最右的
            l = i
            while l > 0 and nums[l-1] == target:
                l -= 1
            r = i
            while r < len(nums)-1 and nums[r+1] == target:
                r += 1
            return [l, r]


if __name__ == '__main__':
    nums = [1, 4]
    k = 4
    solution = Solution()
    print(solution.searchRange(nums, k))
    pass