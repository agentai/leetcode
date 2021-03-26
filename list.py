#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/15

"""
文件说明：
    列表的数据结构
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nums = []
        head = self
        while head:
            nums.append(str(head.val))
            head = head.next
        return "->".join(nums)


def create_list_node(nums):
    head = ListNode()
    cur = head
    for num in nums:
        cur.next = ListNode(val=num)
        cur = cur.next
    return head.next


# print(create_list_node([1, 5, 7, 2]))