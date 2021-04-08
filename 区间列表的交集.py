#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/21

"""
文件说明：
    986. 区间列表的交集
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中a <= b）表示实数x的集合，而a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。


示例 1：


输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
示例 2：

输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]
示例 3：

输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]
示例 4：

输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]

    https://leetcode-cn.com/problems/interval-list-intersections
    
"""
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        执行用时：
80 ms
, 在所有 Python3 提交中击败了
6.33%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
5.27%
的用户
        :param firstList:
        :param secondList:
        :return:
        """
        res = []
        f = s = 0
        while f < len(firstList) and s < len(secondList):
            # f 右边小于s左边，f走下一个
            if firstList[f][1] < secondList[s][0]:
                f += 1
            elif secondList[s][1] < firstList[f][0]:
                s += 1
            elif firstList[f][0] < secondList[s][0]:
                if firstList[f][1] > secondList[s][1]:
                    res.append(secondList[s])
                    s += 1
                else:
                    res.append([secondList[s][0], firstList[f][1]])
                    f += 1
            else:
                if firstList[f][1] < secondList[s][1]:
                    res.append(firstList[f])
                    f += 1
                else:
                    res.append([firstList[f][0], secondList[s][1]])
                    s += 1
        return res


if __name__ == '__main__':
    nums1 = [[0,2],[5,10],[13,23],[24,25]]
    nums2 = [[1,5],[8,12],[15,24],[25,26]]
    solution = Solution()
    print(solution.intervalIntersection(nums1, nums2))
    pass
