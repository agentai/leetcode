#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
61. 旋转链表
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

输入：head = [0,1,2], k = 4
输出：[2,0,1]

https://leetcode-cn.com/problems/rotate-list/
"""
from typing import *
from base import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        执行用时：
60 ms
, 在所有 Python3 提交中击败了
5.44%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
67.75%
的用户
        """
        # 思路：先遍历到底求长度，然后将底指向头，指针停留在底，然后算需要走的长度，在返回
        if not head or not head.next:
            return head
        # 遍历到底求长度
        count = 1
        cur = head
        # 指针停留在底
        while cur.next:
            cur = cur.next
            count += 1
        # 求需要走的次数
        k = count-k%count
        # 底指向头，并走对应次数
        cur.next = head
        while k > 0:
            cur = cur.next
            k -= 1
        # 当前位置下一个作为头，然后截断返回
        head = cur.next
        cur.next = None
        return head



    def rotateRight1(self, head: ListNode, k: int) -> ListNode:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
63.50%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
41.16%
的用户
        """
        # 思路，先取数值做旋转，然后在赋值回去
        nums = []
        # 哨兵
        guard = ListNode(next=head)
        # 取数值
        while head:
            nums.append(head.val)
            head = head.next
        # 为空的话直接返回
        if not nums:
            return guard.next
        # 去掉循环周期
        k = k%len(nums)
        # 旋转
        nums = nums[::-1]
        nums = nums[0:k][::-1] + nums[k:][::-1]
        # 重新赋值
        head = guard.next
        for num in nums:
            head.val = num
            head = head.next
        return guard.next


if __name__ == '__main__':
    s = [1,2,3,4,5]
    k = 2
    # s = [1, 2]
    # k = 0
    solution = Solution()
    nums = create_list_node(s)
    print(solution.rotateRight(nums, k))
    pass