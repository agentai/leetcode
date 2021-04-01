#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/16

"""
文件说明：
    206. 反转链表
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
    https://leetcode-cn.com/problems/reverse-linked-list/
"""
from base import *


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
62.68%
的用户
内存消耗：
15.4 MB
, 在所有 Python3 提交中击败了
85.69%
的用户
        """
        # 思路：加一个哨兵，遍历head，每次令哨兵的next指向head
        guard = ListNode()
        while head:
            tmp = head.next
            head.next = guard.next
            guard.next = head
            head = tmp
            # print(head, guard)
        return guard.next


if __name__ == '__main__':
    # nums = [1,2,3,3,4,4,5, 5, 5,6]
    nums = [1,4,1,2,3]
    solution = Solution()
    print(solution.reverseList(create_list_node(nums)))
    pass
