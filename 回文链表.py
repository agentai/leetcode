#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
234. 回文链表

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

https://leetcode-cn.com/problems/palindrome-linked-list/
"""
from typing import *
from base import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """执行用时：
788 ms
, 在所有 Python3 提交中击败了
26.46%
的用户
内存消耗：
40.2 MB
, 在所有 Python3 提交中击败了
38.96%
的用户"""
        # 思路，快慢指针，快指针先到尾部，慢指针不动，确定列表长度，然后找到中间点，反转右边的列表

        # fast走两步slow走一步，也可以达到一半的距离
        gourd = ListNode(next=head)
        fast = gourd
        slow = gourd
        count = 0
        # 先确定列表长度
        while fast.next:
            count += 1
            fast = fast.next
        # 慢指针到中间
        m = count//2
        while m > 0:
            slow = slow.next
            m -= 1
        # 去掉中间孤立点
        if count%2 and slow.next:
            slow.next = slow.next.next
        # 左边尾部
        left_tail = slow
        slow = slow.next
        left_tail.next = None
        while slow:
            # 反转右边
            tmp = slow
            slow = slow.next
            tmp.next = left_tail.next
            left_tail.next = tmp
        gourd = gourd.next
        right = left_tail.next
        left_tail.next = None
        while gourd and right:
            if gourd.val != right.val:
                return False
            gourd = gourd.next
            right = right.next
        return not gourd and not right


if __name__ == '__main__':
    nums = [1,2,4,2,2,1]
    k = 3
    # nums = build_bfs(nums)
    nums = create_list_node(nums)
    solution = Solution()
    print(solution.isPalindrome(nums))
    pass