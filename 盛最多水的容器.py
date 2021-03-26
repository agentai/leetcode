#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    11. 盛最多水的容器
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
    https://leetcode-cn.com/problems/container-with-most-water/
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
执行用时：
264 ms
, 在所有 Python3 提交中击败了
10.15%
的用户
内存消耗：
24.5 MB
, 在所有 Python3 提交中击败了
19.19%
的用户
        """
        # 双指针，哪边小走哪边，因为小的那边不可能在作为边界了
        l, r = 0, len(height)
        max_area = 0
        while l < r:
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == '__main__':
    s = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(s))
    pass