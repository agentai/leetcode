#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/21

"""
文件说明：
    1288. 删除被覆盖区间
    https://leetcode-cn.com/problems/remove-covered-intervals/
    思路：先按照左边+右边排序
    在依次挑选覆盖
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        执行用时：
68 ms
, 在所有 Python3 提交中击败了
14.45%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
98.46%
的用户
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        l = intervals[0][0]
        r = intervals[0][1]
        for i in intervals[1:]:
            if r >= i[1]:
                intervals.remove(i)
            else:
                l = i[0]
                r = i[1]
        return len(intervals)


if __name__ == '__main__':
    intervals = [[1,4],[3,6],[2,8],[2,6]]
    solution = Solution()
    print(solution.removeCoveredIntervals(intervals))
    pass
