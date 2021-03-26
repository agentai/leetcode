#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    4. 寻找两个正序数组的中位数
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
    https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 思路先确定中位数的两个或一个索引，在用两个指针分别从两个数值的左边开始，一直走到中位数索引为止
        len_1 = len(nums1)
        len_2 = len(nums2)
        between = True
        mid = int((len_1 + len_2) / 2)
        if (len_1 + len_2) % 2 != 0:
            mid += 1
            between = False
        m = n = 0
        passed = False
        while mid > 0:
            if nums1[m] < nums2[n]:
                if m < len_1:
                    m += 1
                else:
                    n += 1
                    passed = True
            elif n < len_2:
                n += 1
            else:
                m += 1
                passed = True
            mid -= 1
        if m == len_1:
            if passed:
                if between:
                    return (nums2[n] + nums2[n + 1]) / 2
                else:
                    return nums2[n]
            else:
                if between:
                    return (nums1[m] + nums2[n]) / 2
                else:
                    return nums1[m]
        else:
            if passed:
                if between:
                    return (nums1[m] + nums1[m + 1]) / 2
                else:
                    return nums1[n]
            else:
                if between:
                    return (nums1[m] + nums2[n]) / 2
                else:
                    return nums2[m]


if __name__ == '__main__':
    nums1 = [1,3]
    nums2 = [2]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
    pass
