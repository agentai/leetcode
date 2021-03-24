#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/21

"""
文件说明：
    986. 区间列表的交集
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
