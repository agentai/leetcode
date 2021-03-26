#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    84. 柱状图中最大的矩形
输入: [2,1,5,6,2,3]
输出: 10
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""
from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        执行用时：
304 ms
, 在所有 Python3 提交中击败了
39.89%
的用户
内存消耗：
25.1 MB
, 在所有 Python3 提交中击败了
39.67%
的用户
        """
        # 主要思路，单调栈 + 哨兵
        # 哨兵就是给栈先加一个位置，因为计算面积的时候，需要根据当前栈顶确定起点位置（关键）
        # 栈里存的是索引，索引对应的数字是单调增的
        # 通过索引相减确定宽度，在通过单调性来确定高度
        # 分两步，第一步先构建单调栈，第二步处理单调栈
        # 第一步 构建单调栈的时候，如果遇到当前索引对应的数小于栈顶，循环出栈，
        # 一直到对应的数大于栈顶，同时计算最大面积
        # 构建完栈后，取栈顶的索引作为起点，先用起点算一次最大面积，然后循环出栈，一直到哨兵前，
        # 每一轮出栈的索引对应的值是高，出栈完后的栈顶是左边，右边是之前提取的起点。用来算面积。
        max_area = 0
        # 先加一个-1做哨兵，因为计算面积的时候，需要根据当前栈顶确定起点位置
        stack = [-1]
        # 第一步，构建栈
        for i in range(len(heights)):
            if stack[-1] == -1 or heights[stack[-1]] < heights[i]:
                # 如果栈是空的或者当前值大于栈顶索引对应的值，当前索引入栈
                stack.append(i)
            else:
                # 如果当前值小于栈顶对应的值，取出栈顶元素，
                # 一直到栈顶对应的值小于当前值或者到哨兵位置，同时计算最大面积
                while stack[-1] >= 0 and heights[stack[-1]] > heights[i]:
                    start = stack.pop()
                    # 右边是当前索引，左边是栈顶的索引的右边，就是i-stack[-1]-1，高是当前值
                    max_area = max((i - stack[-1] - 1) * heights[start], max_area)
                stack.append(i)
        print(stack, max_area)
        # 第二步，处理栈
        # 先取起点，也就是最右边的索引，同时比较一次面积
        start = stack.pop()
        # 右边是start，左边是当前栈顶的索引，高是start对应的高
        max_area = max((start-stack[-1])*heights[start], max_area)
        # 循环出栈
        while len(stack) > 1:
            cur = stack.pop()
            # 右边是起点，左边是当前栈顶的索引，高是当前值
            max_area = max((start - stack[-1]) * heights[cur], max_area)
        return max_area

    def largest_area(self, nums: List[int]) -> int:
        # 单调栈 + 哨兵
        max_area = 0
        # 栈里放的是索引，索引对应的值是单调增的
        stack = [-1]
        for i in range(len(nums)):
            # 当栈顶是哨兵或者栈顶小于当前值时，入栈
            if stack[-1] == -1 or nums[stack[-1]] < nums[i]:
                stack.append(i)
            else:
                # 如果不是，则依次出栈顶元素，直到栈顶元素小于当前值，同时计算面积
                while stack[-1] >= 0 and nums[stack[-1]] > nums[i]:
                    cur = stack.pop()
                    # r = i-1
                    # l = stack[-1]
                    # high = nums[cur]
                    max_area = max(max_area, (i-stack[-1]-1) * nums[cur])
                # 处理完后，当前元素入栈
                stack.append(i)
        print(stack, max_area)
        # 处理栈
        start = stack.pop()
        max_area = max(max_area, (start-stack[-1]) * nums[start])
        # 直到遇到哨兵位置
        while stack[-1] >= 0:
            cur = stack.pop()
            # r = start
            # l = stack[-1]
            # high = nums[cur]
            max_area = max(max_area, (start-stack[-1]) * nums[cur])
        return max_area



if __name__ == '__main__':
    nums = [2,4]
    nums = [2, 1,5,6,2,3]
    # nums = [2,1,2]
    nums = [5, 4, 1, 2]
    solution = Solution()
    print(solution.largestRectangleArea(nums))
    print(solution.largest_area(nums))
    pass