#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/15

"""
文件说明：
    基本的一些数据结构
"""
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_bfs(self):
        """广度优先遍历"""
        def _print(queue, nums):
            new_queue = []
            for tree in queue:
                if tree:
                    nums.append(tree.val)
                    new_queue.append(tree.left)
                    new_queue.append(tree.right)
                else:
                    nums.append(None)
            if new_queue and list(filter(lambda x: x, new_queue)):
                _print(new_queue, nums)
        nums = []
        _print([self], nums)
        print("bfs", nums)
        return nums

    def print_dfs(self):
        def _print(tree, nums):
            nums.append(tree.val)
            if not tree.left and not tree.right:
                return
            if tree.left:
                _print(tree.left, nums)
            else:
                nums.append(None)
            if tree.right:
                _print(tree.right, nums)
            else:
                nums.append(None)
        nums = []
        _print(self, nums)
        print("dfs", nums)
        return nums


def build_bfs(nums):
    """按照广度优先建树"""
    def _build(queue, nums):
        new_queue = []
        for tree in queue:
            if not nums:
                return
            num = nums.pop(0)
            if num:
                tree.left = TreeNode(num)
                new_queue.append(tree.left)
            if not nums:
                return
            num = nums.pop(0)
            if num:
                tree.right = TreeNode(num)
                new_queue.append(tree.right)
        if new_queue and nums:
            _build(new_queue, nums)
    if not nums:
        return None
    num = nums.pop(0)
    tree = TreeNode(num)
    _build([tree], nums)
    tree.print_bfs()
    return tree


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


def create_lists_node(lists):
    """
    example:
    lists = [[1,4,5],[1,3,4],[2,6]]
    [print(i) for i in create_lists_node(lists)]
    """
    res = []
    for nums in lists:
        res.append(create_list_node(nums))
    return res


if __name__ == '__main__':
    # nums = [3, 2, 3, None, 3, None, 1]
    # tree = build_bfs(nums)
    # tree.print_dfs()
    #
    # print(create_list_node([1, 5, 7, 2]))
    # lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # [print(i) for i in create_lists_node(lists)]
    pass
