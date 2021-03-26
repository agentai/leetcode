#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    189. 旋转数组
    https://leetcode-cn.com/problems/rotate-array/
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        """
        # 思路：先用k对len_n取余（关键），因为会有多轮旋转的情况
        # 在 0,len_n-1 旋转，在 0,k-1 旋转，在 k,len_n-1 旋转
        def reverse(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        len_n = len(nums)
        k = k % len_n
        reverse(0, len_n-1)
        reverse(0, k-1)
        reverse(k, len_n-1)

        # reverse(len_n-k, len_n-1)
        # reverse(0, len_n-k-1)
        # reverse(0, len_n-1)


if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    print(solution.rotate(nums, k))
    pass
