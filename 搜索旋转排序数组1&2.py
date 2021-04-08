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


81. 搜索旋转排序数组 II
示例 1：

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例 2：

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false

https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """33
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

    def search1(self, nums: List[int], target: int) -> int:
        """33
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
36.48%
的用户
内存消耗：
15.2 MB
, 在所有 Python3 提交中击败了
9.79%
的用户
        """
        # 二分查找
        def find(l, r):
            # 如果差距小于1，分别判断，如都不相等，返回-1
            if r - l <= 1:
                if nums[r] == target:
                    return r
                if nums[l] == target:
                    return l
                return -1
            # 二分查找
            m = (l + r) // 2
            if nums[m] == target:
                return m
            else:
                # 如果在左边且有序，找左边
                if nums[l] <= target < nums[m]:
                    return find(l, m - 1)
                # 如果在右边且有序，找右边
                elif nums[r] >= target > nums[m]:
                    return find(m + 1, r)
                # 如果超出左右边界，返回-1
                elif nums[r] < target and nums[l] > target:
                    return -1
                else:
                    # 先找左边，如果找到了，返回，不然找右边
                    a = find(l, m - 1)
                    if a != -1:
                        return a
                    return find(m + 1, r)

        return find(0, len(nums) - 1)

    def search4(self, nums: List[int], target: int) -> bool:
        """81
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
88.05%
的用户
内存消耗：
15.5 MB
, 在所有 Python3 提交中击败了
5.14%
的用户
        """
        # 二分类
        def find(l, r):
            # 当相近后，直接返回r和l对应的值是否是target
            if r - l <= 1:
                return nums[r] == target or nums[l] == target
            # 二分查找
            m = (l + r) // 2
            if nums[m] == target:
                return True
            else:
                # 如果左边是正常序列，且target在其中，找左边
                if nums[l] <= target < nums[m]:
                    return find(l, m - 1)
                # 如果有变是正常序列，且target在其中，找右边
                elif nums[r] >= target > nums[m]:
                    return find(m + 1, r)
                # 如果target超过了左右边界，则直接返回false
                elif nums[r] > target and nums[l] < target:
                    return False
                # 不然就两边一起找
                else:
                    return find(l, m - 1) or find(m + 1, r)

        return find(0, len(nums) - 1)


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