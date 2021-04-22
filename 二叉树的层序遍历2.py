#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
107. 二叉树的层序遍历 II

给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]

https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii

"""
from typing import *
from base import *


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
91.11%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
72.49%
的用户
        """
        if not root:
            return []
        res = deque()
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.appendleft(tmp)
        return list(res)


if __name__ == '__main__':
    nums = [3,9,20,None,None,15,7]
    nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.levelOrderBottom(nums))
    pass