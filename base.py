#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/15

"""
文件说明：
    基本的一些数据结构
"""
from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_bfs(self, to_string=False):
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
        if to_string:
            return f"bfs： {nums}"
        print("bfs：", nums)
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

    def print_in_order(self, is_print=False):
        """中序遍历 -> 左 根 右"""
        def _print(tree, nums):
            if tree.left:
                _print(tree.left, nums)
            nums.append(tree.val)
            if tree.right:
                _print(tree.right, nums)
        nums = []
        _print(self, nums)
        if is_print:
            print("中序：", nums)
        return nums

    def print_first_order(self, is_print=False):
        """前序遍历 -> 根 左 右"""
        def _print(tree, nums):
            nums.append(tree.val)
            if tree.left:
                _print(tree.left, nums)
            if tree.right:
                _print(tree.right, nums)
        nums = []
        _print(self, nums)
        if is_print:
            print("前序：", nums)
        return nums

    def print_last_order(self, is_print=False):
        """后序遍历 -> 左 右 根"""
        def _print(tree, nums):
            if tree.left:
                _print(tree.left, nums)
            if tree.right:
                _print(tree.right, nums)
            nums.append(tree.val)
        nums = []
        _print(self, nums)
        if is_print:
            print("后序：", nums)
        return nums

    def __str__(self):
        print()
        self.print_first_order(True)
        self.print_in_order(True)
        self.print_last_order(True)
        return self.print_bfs(True)


def build_tree_by_first_in_order(first_orders, in_orders):
    """已知前序中序，建树
    注：如果树的节点存在重复，建立的树会有问题
    example:
    first_orders = [5, 1, 4, 3, 6]
    in_orders = [1, 5, 3, 4, 6]
    tree = build_tree_by_first_in_order(first_orders, in_orders)
    """
    if not first_orders or not in_orders:
        return None
    # 前序的第一个值就是根
    tree = TreeNode(first_orders[0])
    for i in range(len(in_orders)):
        # 从中序找出根的索引，索引左边就是根的左边，右边就是根的右边
        if first_orders[0] == in_orders[i]:
            # 前序的 [1, i+1) 是所有根的左边，0位置是根；
            # 中序的 [0, i) 是所有根的左边，提取出来建立左边，i位置是根
            tree.left = build_tree_by_first_in_order(
                first_orders[1:i+1].copy(), in_orders[0:i].copy())
            # 排除左边，剩下的就是右边，
            # 前序的 [i+1, len(first_orders))是所有根的右边；
            # 中序的 [i+1, len(in_orders))是所有根的右边
            tree.right = build_tree_by_first_in_order(
                first_orders[i+1:].copy(), in_orders[i+1:].copy())
    return tree


def build_tree_by_last_in_order(last_orders, in_orders):
    """已知后序中序，建树
    注：如果树的节点存在重复，建立的树会有问题
    example:
    in_orders = [1, 5, 3, 4, 6]
    last_orders = [1, 3, 6, 4, 5]
    tree = build_tree_by_in_last_order(last_orders, in_orders)
    """
    if not last_orders or not in_orders:
        return None
    # 后序的最后一个值就是根
    tree = TreeNode(last_orders[-1])
    for i in range(len(in_orders)):
        # 从中序找出根的索引，索引左边就是根的左边，右边就是根的右边
        if last_orders[-1] == in_orders[i]:
            # 后序的 [0, i) 是所有根的左边，len(last_orders)-1位置是根；
            # 中序的 [0, i) 是所有根的左边，提取出来建立左边，i位置是根
            tree.left = build_tree_by_last_in_order(
                last_orders[0:i].copy(), in_orders[0:i].copy())
            # 排除左边，剩下的就是右边，
            # 后序的 [i, len(last_orders)-1)是所有根的右边，len(last_orders)-1位置是根；
            # 中序的 [i+1, len(in_orders))是所有根的右边
            tree.right = build_tree_by_last_in_order(
                last_orders[i:-1].copy(), in_orders[i+1:].copy())
    return tree


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
    print("build_by_bfs", tree)
    # tree.print_bfs()
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
    """
    example:
    nums = [2, 4, 7, 1, 4, 3, 1]
    print(create_list_node(nums))
    """
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
    # nums = [5, 1, 4, None, None, 3, 6]
    # tree = build_bfs(nums)
    # # print(tree)
    # # tree.print_dfs()
    # tree1 = build_tree_by_first_in_order(tree.print_first_order(), tree.print_in_order())
    # print("build_tree_by_first_in_order", tree1)
    # tree2 = build_tree_by_last_in_order(tree.print_last_order(), tree.print_in_order())
    # print("build_tree_by_last_in_order", tree2)
    #
    # print(create_list_node([1, 5, 7, 2]))
    # lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # [print(i) for i in create_lists_node(lists)]
    pass
