#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
378. 有序矩阵中第 K 小的元素

输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

"""
from typing import *
from base import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        执行用时：
56 ms
, 在所有 Python3 提交中击败了
80.55%
的用户
内存消耗：
18.6 MB
, 在所有 Python3 提交中击败了
89.40%
的用
        """
        # 思路，二分法查找，先计算当前首尾的中间数，再定位这个中间数所在的位置
        # 如果中间数所在的位置==k了，则返回，否则，二分查找
        # rows记录行数
        rows = len(matrix)
        cols = len(matrix[0])

        def check(mid):
            # 定位中间数所在的位置
            # i 从下往上，j 从左往右
            i, j = rows - 1, 0
            # 记录小于当前数的个数
            num = 0
            while i >= 0 and j < cols:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def kthSmallest3(self, matrix: List[List[int]], k: int) -> int:
        """
        """
        # 思路，每次只走
        rows = len(matrix)
        cols = len(matrix[0])

        def add_node(queue, r, c, v, kind):
            if (r, c, v) not in queue:
                i = len(queue)
                if kind == "u":
                    while i > 0 and v < queue[i - 1][2]:
                        i -= 1
                else:
                    while i > 0 and v > queue[i - 1][2]:
                        i -= 1
                queue.insert(i, (r, c, v))
            return queue

        count_u = 0
        count_d = rows*cols
        v_u = matrix[0][0]
        queue_u = [(0, 0, v_u)]
        v_d = matrix[rows-1][cols-1]
        queue_d = [(rows-1, cols-1, v_d)]
        while queue_u or queue_d:
            count_u += 1
            count_d -= 1
            (r_u, c_u, v_u) = queue_u.pop(0)
            if k <= count_u:
                return v_u
            (r_d, c_d, v_d) = queue_d.pop(0)
            if k > count_d:
                return v_d
            if r_u < rows - 1:
                queue_u = add_node(queue_u, r_u + 1, c_u, matrix[r_u + 1][c_u], "u")
            if c_u < cols - 1:
                queue_u = add_node(queue_u, r_u, c_u + 1, matrix[r_u][c_u + 1], "u")
            if r_d > 0:
                queue_d = add_node(queue_d, r_d - 1, c_d, matrix[r_d - 1][c_d], "d")
            if c_d < 0:
                queue_d = add_node(queue_d, r_d, c_d - 1, matrix[r_d][c_d - 1], "d")
        return v_d

    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        """
        执行用时：
968 ms
, 在所有 Python3 提交中击败了
5.03%
的用户
内存消耗：
18.7 MB
, 在所有 Python3 提交中击败了
53.93%
的用户
        """
        # 思路，每次只走一步，为当前步的最小值，走一步后，加这一步的下一步入队列
        rows = len(matrix)
        cols = len(matrix[0])

        def add_node(queue, r, c, v):
            if (r, c, v) not in queue:
                i = len(queue)
                while i > 0 and v < queue[i-1][2]:
                    i -= 1
                queue.insert(i, (r, c, v))
            return queue

        count = 0
        v = matrix[0][0]
        queue = [(0, 0, v)]
        while queue:
            count += 1
            (r, c, v) = queue.pop(0)
            if k <= count:
                return v
            if r < rows - 1:
                queue = add_node(queue, r+1, c, matrix[r+1][c])
            if c < cols - 1:
                queue = add_node(queue, r, c+1, matrix[r][c+1])
        return v


if __name__ == '__main__':
    nums = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    nums = [[-5]]
    k = 1
    nums = [[1,2],[1,3]]
    k = 1
    nums = [[1,3,5],[6,7,12],[11,14,14]]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.kthSmallest(nums, k))
    pass