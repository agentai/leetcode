#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
363. 矩形区域不超过 K 的最大数值和

给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。

题目数据保证总会存在一个数值和不超过 k 的矩形区域。

示例 1：

输入：matrix = [[1,0,1],[0,-2,3]], k = 2
输出：2
解释：蓝色边框圈出来的矩形区域[[0, 1], [-2, 3]]的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。

示例 2：

输入：matrix = [[2,2,-1]], k = 3
输出：3

https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
"""
from typing import *
from base import *
from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix1(self, matrix: List[List[int]], k: int) -> int:
        # 动态规划+滑动窗口
        # a,b c,d 表示从 m[a][b] 到 m[c][d] 之间的和
        # abcd只能往右走或往下走，先走cd，如果加入cd后值变小了，ab=cd
        max_sum = [-float('inf')]
        rows = len(matrix)
        cols = len(matrix[0])

        def sub(a, b, c, d, src_sum):
            if max_sum[0] == k:
                return
            if c < rows - 1:
                add = 0 # 记录加上 c+1 行后增加的量
                minus = 0 # 记录减去 a 行后减少的量
                for i in range(b, d+1):
                    add += matrix[c+1][i]
                    minus += matrix[a][i]
                # 加上后小于k，a行保留，加入c+1行
                tmp = src_sum + add
                if tmp <= k:
                    max_sum[0] = max(tmp, max_sum[0])
                    if tmp == k:
                        return
                sub(a, b, c+1, d, tmp)
                if a < rows-1:
                    # 加上且减去后小于k，去除a行，加入c+1行
                    tmp = src_sum + add - minus
                    if tmp <= k:
                        max_sum[0] = max(tmp, max_sum[0])
                        if tmp == k:
                            return
                    sub(a+1, b, c+1, d, tmp)

            if a < rows - 1 and a < c:
                minus = 0  # 记录减去 a 行后减少的量
                for i in range(b, d + 1):
                    minus += matrix[a][i]
                # 减去a行后小于k，去除a行
                tmp = src_sum - minus
                if tmp <= k:
                    max_sum[0] = max(tmp, max_sum[0])
                    if tmp == k:
                        return
                sub(a + 1, b, c, d, tmp)

            if d < cols - 1:
                add = 0  # 记录加上 d+1 列后增加的量
                minus = 0  # 记录减去 b 列后减少的量
                for i in range(a, c+1):
                    add += matrix[i][d+1]
                    minus += matrix[i][b]
                # 加上后小于k，b保留，加入d+1列
                tmp = src_sum + add
                if tmp <= k:
                    max_sum[0] = max(tmp, max_sum[0])
                    if tmp == k:
                        return
                sub(a, b, c, d+1, tmp)
                if b < cols-1:
                    # 加上且减去后小于k，去除b，加入d+1行
                    tmp = src_sum + add - minus
                    if tmp <= k:
                        max_sum[0] = max(tmp, max_sum[0])
                        if tmp == k:
                            return
                    sub(a, b+1, c, d+1, tmp)

            if b < cols-1 and b < d:
                minus = 0  # 记录减去 b 列后减少的量
                for i in range(a, c + 1):
                    minus += matrix[i][b]
                # 减去b后小于k，去除b
                tmp = src_sum - minus
                if tmp <= k:
                    max_sum[0] = max(tmp, max_sum[0])
                    if tmp == k:
                        return
                sub(a, b + 1, c, d, tmp)

        sub(0, 0, 0, 0, matrix[0][0])
        return int(max_sum[0])

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """
        执行用时：
2900 ms
, 在所有 Python3 提交中击败了
14.90%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
68.63%
的用户
        """
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):  # 枚举上边界
            total = [0] * n
            for j in range(i, m):  # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]  # 更新每列的元素和

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans


if __name__ == '__main__':
    nums = [[1,0,1],[0,-2,3]]
    k = 5
    nums = [[2, 2, -1]]
    k = 0
    nums = [[7,7,4,-6,-10],[-7,-3,-9,-1,-7],[9,6,-3,-7,7],[-4,1,4,-3,-8],[-7,-4,-4,6,-10],[1,3,-2,3,-10],[8,-2,1,1,-8]]
    k = 12
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.maxSumSubmatrix(nums, k))
    pass