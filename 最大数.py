#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
179. 最大数

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"

https://leetcode-cn.com/problems/largest-number

"""
from typing import *
from base import *


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
89.05%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
18.96%
的用户
        """
        # 思路，排序
        stack = []
        for n in nums:
            stack.append(str(n))

        def compare(num1, num2):
            # 先按照i位置比较，
            # 如果i位置相同的话，比较i+1的位置，
            # 如果i+1的位置超过其中一个数字的长度，则没有超过i+1的数的i+1位置值超过k的话，排前面
            len1 = len(num1)
            len2 = len(num2)
            for i in range(min(len1, len2)):
                if num1[i] > num2[i]:
                    return True
                if num2[i] > num1[i]:
                    return False
            if len1 > len2:
                return compare(num1[len2:], num2)
            elif len2 > len1:
                return compare(num1, num2[len1:])
            return True

        def quick_sort(l, r):
            # 快排
            if l >= r:
                return
            base_i = l
            base = stack[r]
            for i in range(l, r):
                if compare(base, stack[i]):
                    stack[base_i], stack[i] = stack[i], stack[base_i]
                    base_i += 1
            stack[base_i], stack[r] = stack[r], stack[base_i]
            quick_sort(l, base_i-1)
            quick_sort(base_i+1, r)
        quick_sort(0, len(nums)-1)
        return str(int("".join(stack[::-1])))


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    # nums = [34323,3432]
    # nums = [0,0]
    # nums = [432, 43243]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.largestNumber(nums))
    # print("343234323")
    pass