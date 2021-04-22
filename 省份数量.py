#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
547. 省份数量

有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。

省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

示例 1：


输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

示例 2：


输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3

https://leetcode-cn.com/problems/number-of-provinces
"""
from typing import *
from base import *


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
93.28%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
86.21%
的用户
        """
        # bfs,用一个队列来存储当前相同的点,从一个点出发，找到所有和这个点相关的点
        # 点相关有两个规则，一个是固定行，一个是固定列
        len_n = len(isConnected)
        # key是行，value是列
        data = {}
        # 先统计所有有连接的点
        for i in range(len_n):
            for j in range(i, len_n):
                if isConnected[i][j] == 1:
                    tmp = data.get(i, set())
                    tmp.add(j)
                    data[i] = tmp
        # 再合并行，如果两个行的列有交集，则合并两个行
        # 需要递归去合并
        def merge():
            # 用来记录是否有改动
            has_change = False
            rows = list(data.keys())
            for i in rows:
                if i in data:
                    for k in rows:
                        if k == i or k not in data:
                            continue
                        v = data[k]
                        # 合并两行
                        if v & data[i]:
                            data[i].update(v)
                            data.pop(k)
                            has_change = True
            return has_change
        while merge():
            pass
        return len(data)


if __name__ == '__main__':
    nums = [[1,1,0],[1,1,0],[0,0,1]]
    nums = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.findCircleNum(nums))
    pass