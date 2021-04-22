#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1 。



示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：true
示例 2：


输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
示例 3：

输入：root = []
输出：true

https://leetcode-cn.com/problems/balanced-binary-tree
"""
from typing import *
from base import *


class Solution:
    def isBalanced1(self, root: TreeNode) -> bool:
        """
        执行用时：
76 ms
, 在所有 Python3 提交中击败了
31.32%
的用户
内存消耗：
19.9 MB
, 在所有 Python3 提交中击败了
6.97%
的用户
        """
        # dfs
        def dfs(node, depth):
            left = depth
            if node.left:
                left = dfs(node.left, depth+1)
            if left < 0:
                return left
            right = depth
            if node.right:
                right = dfs(node.right, depth+1)
            if right < 0:
                return right
            if left - right > 1 or right - left > 1:
                return -1
            return max(left, right)

        if not root:
            return True
        res = dfs(root, 0)
        return res >= 0

    def isBalanced(self, root: TreeNode) -> bool:
        """
        执行用时：
60 ms
, 在所有 Python3 提交中击败了
72.75%
的用户
内存消耗：
19.6 MB
, 在所有 Python3 提交中击败了
36.65%
的用
        """
        # dfs
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 3, None, None, 4, 4]
    nums = [1, None, 2, None, 3]
    nums = [1, 2, 3, 4, 5, 6, None, 8]
    nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.isBalanced(nums))
    pass