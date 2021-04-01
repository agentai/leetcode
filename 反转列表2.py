#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
92. 反转链表 II
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

输入：head = [5], left = 1, right = 1
输出：[5]

https://leetcode-cn.com/problems/reverse-linked-list-ii/
"""
from typing import *
from base import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
84.94%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
72.72%
的用户
        """
        # 思路：哨兵+提取数值，然后赋值回去
        # 哨兵
        guard = ListNode(next=head)
        # 确定左边位置
        pro_l = guard
        l = 0
        while l < left:
            l += 1
            pro_l = pro_l.next
        # 确定右边位置，需要到右边的后面
        r = l
        pro_r = pro_l
        nums = []
        while r <= right:
            r += 1
            nums.append(pro_r.val)
            pro_r = pro_r.next
        # 出栈的方式写回数据
        while nums:
            pro_l.val = nums.pop()
            pro_l = pro_l.next
        return head


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    l = 2
    r = 4
    nums = [5]
    l = 1
    r = 1
    # nums = build_bfs(nums)
    nums = create_list_node(nums)
    solution = Solution()
    print(solution.reverseBetween(nums, l, r))
    pass