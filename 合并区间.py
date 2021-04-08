#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/21

"""
文件说明：
    56. 合并区间

以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

    https://leetcode-cn.com/problems/merge-intervals/
    思路先排序后覆盖
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
45.54%
的用户
内存消耗：
16.5 MB
, 在所有 Python3 提交中击败了
5.03%
的用户
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        merged = []
        cur = intervals[0]
        for i in intervals[1:]:
            # 断开了，右边界小于左边界
            if cur[1] < i[0]:
                merged.append(cur)
                cur = i
            elif cur[1] <= i[1]:
                # 有重叠，合并两个组成新边界
                cur[1] = i[1]
        if not merged or cur[0] != merged[-1][0] or cur[1] != merged[-1][0]:
            merged.append(cur)
        return merged



    def merge1(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        执行用时：
80 ms
, 在所有 Python3 提交中击败了
5.31%
的用户
内存消耗：
16.5 MB
, 在所有 Python3 提交中击败了
5.03%
的用户
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        index = 0
        cur = intervals[index]
        del_index = []
        for i, item in enumerate(intervals):
            if i == 0:
                continue
            # 断开了，右边界小于左边界
            if cur[1] < item[0]:
                index = i
                cur = item
            elif cur[1] <= item[1]:
                # 有重叠，合并两个组成新边界
                intervals[index][1] = item[1]
                cur[1] = item[1]
                del_index.insert(0, i)
            else:
                # 全覆盖，
                del_index.insert(0, i)
        for i in del_index:
            intervals.pop(i)
        return intervals


if __name__ == '__main__':
    nums = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]
    nums = [[1,4],[4,5]]
    solution = Solution()
    print(solution.merge(nums))
    pass
