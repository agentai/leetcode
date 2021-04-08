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
        """
        执行用时：
64 ms
, 在所有 Python3 提交中击败了
22.18%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
97.50%
的用户
        """
        # 思路，中位数可以转化成找第k个大的数
        # k = (len1 + len2)//2，如果是奇数，k+=1
        len1 = len(nums1)
        len2 = len(nums2)
        k = (len1 + len2)//2
        # 判断是否是奇数个，如果是，k += 1
        is_mid = (len1+len2) != k * 2
        if is_mid:
            k += 1
        # i和j从-1开始，比较下一个哪个大，大的走下一步
        i, j = -1, -1
        base = 0 # 随时记录当前最小的值
        while k > 0:
            # 这里判断条件很关键
            if len2 == 0 or (i < len1-1 and j < len2-1 and nums1[i+1] < nums2[j+1]) or (j >= len2-1):
                i += 1
                base = nums1[i]
            else:
                j += 1
                base = nums2[j]
            k -= 1
        # 如果是奇数个，直接返回当前最小值
        if is_mid:
            return base
        if len2 == 0 or (i < len1-1 and j < len2-1 and nums1[i+1] < nums2[j+1]) or (j >= len2-1):
            return (base + nums1[i+1])/2
        else:
            return (base + nums2[j+1])/2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        # 中位数可以转化成第k小的数，k=(len(nums1)+len(nums2))//2
        # 如果两个数组长度和为奇数，直接返回第k个数即可，如果是偶数，需要返回(k,k+1)的均值
        # 如何定位第k小的数，两个数组都从左往右数第k/2位置的数，哪个大就缩小哪个
        len1 = len(nums1)
        len2 = len(nums2)
        k = (len1 + len2) // 2
        # 是否是中间数，如果是中间数，需要找到k+1位置的数
        is_mid = (len1 + len2) != k * 2
        if len1 == 0:
            if is_mid:
                return nums2[k]
            return (nums2[k]+nums2[k-1])/2
        if len2 == 0:
            if is_mid:
                return nums1[k]
            return (nums1[k]+nums1[k-1])/2
        # if is_mid:
        #     k = k+1
        # 如果k==1，直接比较nums1[0]和nums2[0]就行
        if k == 1:
            if is_mid:
                if nums1[0] > nums2[0]:
                    return nums1[0]
                else:
                    return nums2[0]
            else:
                return (nums1[0] + nums2[0]) / 2
        # l1 l2 为对应的索引
        l1 = k//2 - 1
        l2 = k - l1 - 2
        # 如果nums1小了，往左走
        while l2 > 0 and l1 < len1-1 and nums1[l1] < nums2[l2]:
            l1 += 1
            l2 -= 1
        # 如果nums2小了，往右走
        while l1 > 0 and l2 < len2-1 and nums1[l1] > nums2[l2]:
            l1 -= 1
            l2 += 1
        # 取当前位置的4个数，这里保证了<l1的数都得去掉，<l2的数也得去掉，即 (l1+l2+2)=k-1
        tmp = [nums1[l1], nums2[l2]]
        if l1 < len1-1:
            tmp.append(nums1[l1+1])
        if l2 < len2-1:
            tmp.append(nums2[l2+1])
        tmp.sort()
        tmp.pop(0)
        if is_mid:
            return tmp[1]
        return (tmp[0] + tmp[1])/2

        # if l1 == 0:
        #     # l1到底了（即最小的l1都大于等于l2），且l2右边小于等于l1，说明中位数在l2或l2+1中
        #     if l2 < len2-1 and nums2[l2+1] <= nums1[l1]:
        #         if is_mid:
        #             return nums2[l2]
        #         else:
        #             return (nums2[l2] + nums2[l2+1]) / 2
        #     # l1到底了（即最小的l1都大于等于l2），且l2右边大于l1，说明中位数在l2或l1中
        #     else:
        #         if is_mid:
        #             if nums1[l1] > nums2[l2]:
        #                 return nums1[l1]
        #             else:
        #                 return nums2[l2]
        #         else:
        #             return (nums2[l2] + nums1[l1]) / 2
        # elif l2 == 0:
        #     # l2到底了（即最小的l2都大于等于l1），且l1右边小于等于l2，说明中位数在l1或l1+1中
        #     if l1 < len1-1 and nums1[l1 + 1] <= nums2[l2]:
        #         if is_mid:
        #             return nums1[l1]
        #         else:
        #             return (nums1[l1] + nums1[l1 + 1]) / 2
        #     # l2到底了（即最小的l2都大于等于l1），且l1右边大于l2，说明中位数在l1或l2中
        #     else:
        #         if is_mid:
        #             if nums1[l1] > nums2[l2]:
        #                 return nums1[l1]
        #             else:
        #                 return nums2[l2]
        #         else:
        #             return (nums2[l2] + nums1[l1]) / 2
        # else:
        #     # 都没到底的情况下，中位数可能在l1,l2,l1+1,l2+1中
        #     if is_mid:
        #         if nums1[l1] > nums2[l2]:
        #             return nums1[l1]
        #         else:
        #             return nums2[l2]
        #     else:
        #         tmp = [nums1[l1], nums2[l2]]
        #         if l1 < len1-1:
        #             tmp.append(nums1[l1+1])
        #         if l2 < len2-1:
        #             tmp.append(nums2[l2+1])
        #         tmp.sort()
        #         return (tmp[0] + tmp[1]) / 2

    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
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
    nums1 = [1,3,4]
    nums2 = [2,3]
    # nums1 = [1, 3, 4, 9]
    # nums2 = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
    nums1 = []
    nums2 = [1, 2, 4, 4]
    # nums1 = [1]
    # nums2 = [2,3]
    nums1 = [0, 0]
    nums2 = [0, 0]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))
    pass
