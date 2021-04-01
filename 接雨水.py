#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    42. 接雨水
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

https://leetcode-cn.com/problems/trapping-rain-water/

"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
44.42%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
5.07%
的用户
        """
        # 求每个i 存左边最大值和右边最大值，算完后，求每个i的最小高度-其本身高度的和
        # 左右一起算
        # dp[i][0] = max(dp[i-1][0], height[i])
        # dp[n-i-1][1] = max(dp[n-i][1], height[n-i-1])
        n = len(height)
        # 初始化dp
        dp = [[-1, -1] for i in range(n)]
        # 左右一起算每个i的左边最大值和右边最大值
        for i in range(n):
            # 当=0时，左右最大值就是其本身
            if i == 0:
                dp[i][0] = height[i]
                dp[n-1-i][1] = height[n-1-i]
            else:
                # 当!=0时，左边为max其左边和自身，右边为max其右边和自身
                dp[i][0] = max(dp[i-1][0], height[i])
                dp[n-1-i][1] = max(dp[n-i][1], height[n-i-1])
        # 最后算一下每个i的面积
        res = 0
        for i in range(n):
            res += min(dp[i][0], dp[i][1]) - height[i]
        return res


if __name__ == '__main__':
    k = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(k))

    pass