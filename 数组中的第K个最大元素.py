#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    215. 数组中的第K个最大元素

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

"""
from typing import List


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
81.03%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
22.48%
的用户
        """
        # 快排查找
        def quick_find(items, aim):
            len_n = len(items)
            if len_n == 1:
                return items[-aim]
            if len_n == 2:
                if items[0] > items[1]:
                    items[1], items[0] = items[0], items[1]
                return items[-aim]
            l, r = 0, len_n-2
            small, big = [], []
            # 每次必出一个数字，来避免因猜中最小值或最大值而死循环
            base = items.pop(0)
            while l <= r:
                if items[l] >= base:
                    big.append(items[l])
                else:
                    small.append(items[l])
                if l < r:
                    if items[r] >= base:
                        big.append(items[r])
                    else:
                        small.append(items[r])
                l += 1
                r -= 1
            len_b = len(big)
            if len_b >= aim:
                return quick_find(big, aim)
            elif len_b == aim-1:
                return base
            else:
                return quick_find(small, aim-len_b-1)
        return quick_find(nums, k)


    def findKthLargest1(self, nums: List[int], k: int) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
68.71%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
33.42%
的用户
        """
        # 快排思路找

        def quick_find(items, aim):
            # 左右同时找
            l, r = 0, len(items)-1
            if r - l < 1:
                return items[0]
            if r - l == 1:
                if items[0] > items[1]:
                    items[0], items[1] = items[1], items[0]
                return items[-aim]
            m = (l+r+1)//2
            # 先定基准
            base = items[m]
            small, big = [], []
            while l<=r:
                if items[l] >= base:
                    big.append(items[l])
                else:
                    small.append(items[l])
                # 左右不等时，右边也加
                if l < r:
                    if items[r] >= base:
                        big.append(items[r])
                    else:
                        small.append(items[r])
                l += 1
                r -= 1
            # 如果一次排序后没分开大小
            if not big:
                small.sort()
                return small[-aim]
            if not small:
                big.sort()
                return big[-aim]
            len_b = len(big)
            # 如果大的个数正好是目标个数，直接返回base
            if len_b == aim:
                return base
            # 如果大于目标个数，从大集合里找
            elif len_b > aim:
                return quick_find(big, aim)
            else:
                # 如果小于目标个数，从小集合里找
                return quick_find(small, aim-len_b)

        return quick_find(nums, k)


if __name__ == '__main__':
    nums = [3,2,1,5,6,4]
    k = 2
    # nums = [3,2,3,1,2,4,5,5,6]
    # k = 4
    # nums = [2,1]
    # k = 1
    solution = Solution()
    print(solution.findKthLargest(nums, k))

    pass