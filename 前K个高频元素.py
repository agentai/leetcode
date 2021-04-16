#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
347. 前 K 个高频元素

给定一个非空的整数数组，返回其中出现频率前k高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:

输入: nums = [1], k = 1
输出: [1]

https://leetcode-cn.com/problems/top-k-frequent-elements
"""
from typing import *
from base import *


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        """
        执行用时：
272 ms
, 在所有 Python3 提交中击败了
5.03%
的用户
内存消耗：
17.5 MB
, 在所有 Python3 提交中击败了
41.17%
的用户
        """
        # 先排序，然后依次遍历
        len_n = len(nums)
        if not nums:
            return []

        def quick_sort(l, r):
            if r - l <= 1:
                if nums[r] < nums[l]:
                    nums[l], nums[r] = nums[r], nums[l]
                return
            base_i = l
            base = nums[r]
            for i in range(l, r):
                if nums[i] < base:
                    nums[i], nums[base_i] = nums[base_i], nums[i]
                    base_i += 1
            nums[base_i], nums[r] = nums[r], nums[base_i]
            quick_sort(l, max(base_i-1, l))
            quick_sort(min(base_i+1, r), r)

        quick_sort(0, len_n-1)
        res = []
        i = 0
        while i < len_n:
            cur = nums[i]
            j = i
            while j < len_n and nums[j] == cur:
                j += 1
            size = j - i
            i = j
            if not res or len(res) < k:
                res.append([cur, size])
                res.sort(key=lambda x: x[1])
                continue
            k = 0
            while k < len(res) and res[k][1] < size:
                k += 1
            if k > 0:
                res.insert(k, [cur, size])
                res = res[1:]
        return [x[0] for x in res]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        执行用时：
188 ms
, 在所有 Python3 提交中击败了
5.03%
的用户
内存消耗：
17.6 MB
, 在所有 Python3 提交中击败了
19.35%
的用户
        """
        # 先用字典统计个数，然后在快排来选前k个
        data = {}
        for n in nums:
            data[n] = data.get(n, 0) + 1
        data = list(data.items())

        def quick_sort(l, r, res):
            if l > r or len(res) == k:
                return
            base_i = l
            base = data[r][1]
            for i in range(l, r):
                if data[i][1] < base:
                    data[i], data[base_i] = data[base_i], data[i]
                    base_i += 1
            data[base_i], data[r] = data[r], data[base_i]
            tmp = []
            for i in range(base_i, r+1):
                if data[i][0] not in tmp:
                    tmp.append(data[i][0])
            if len(tmp) <= k-len(res):
                res.extend(tmp)
                if len(res) == k:
                    return
                quick_sort(l, base_i-1, res)
            else:
                quick_sort(base_i+1, r, res)

        res = []
        quick_sort(0, len(data)-1, res)
        return res


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    # nums = [5,2,5,3,5,3,1,1,3]
    # k = 2
    nums = [3,0,1,0]
    k = 1
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.topKFrequent(nums, k))
    pass