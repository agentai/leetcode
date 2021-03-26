#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    19. 删除链表的倒数第 N 个结点
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
    https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""
from typing import List
from list import *


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
90.50%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
        """
        # 加哨兵，加快慢指针，快慢指针间距为n
        if n <= 0 or head.next is None:
            return head.next
        guard = ListNode(next=head)
        # 慢指针先指向哨兵，快指针指向头
        l = guard
        r = guard.next
        # 快指针往后走，到空或者长度为n为止
        while r and n > 0:
            n -= 1
            r = r.next
        # 接着快慢指针一起走，到快指针到底为止
        while r:
            r = r.next
            l = l.next
        # 当前慢指针的next指向next.next
        l.next = l.next.next
        return guard.next


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 2
    solution = Solution()
    print(solution.removeNthFromEnd(create_list_node(nums), k))