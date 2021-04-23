#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
236. 二叉树的最近公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
"""
from typing import *
from base import *


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        执行用时：
108 ms
, 在所有 Python3 提交中击败了
10.33%
的用户
内存消耗：
27.5 MB
, 在所有 Python3 提交中击败了
23.66%
的用户
        """
        # 分别做dfs搜索，路径存入栈，然后依次出栈进行比较
        def dfs(tree, node, cur):
            if cur and cur[-1].val == node.val:
                return
            cur.append(tree)
            if tree.left:
                dfs(tree.left, node, cur)
            if tree.right:
                dfs(tree.right, node, cur)
            if cur and cur[-1].val == node.val:
                return
            cur.pop()
        p_list = []
        dfs(root, p, p_list)
        q_list = []
        dfs(root, q, q_list)
        res = None
        while p_list and q_list and p_list[0] == q_list[0]:
            res = p_list.pop(0)
            q_list.pop(0)
        return res

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        执行用时：
140 ms
, 在所有 Python3 提交中击败了
5.20%
的用户
内存消耗：
27.1 MB
, 在所有 Python3 提交中击败了
26.41%
的用户
        """
        def dfs(tree, node, cur):
            if cur and cur[-1] == node.val:
                return
            cur.append(tree.val)
            if tree.left:
                dfs(tree.left, node, cur)
            if tree.right:
                dfs(tree.right, node, cur)
            if cur and cur[-1] == node.val:
                return
            cur.pop()

        p_list = []
        dfs(root, p, p_list)
        q_list = []
        dfs(root, q, q_list)
        res = TreeNode()
        while p_list and q_list and p_list[0] == q_list[0]:
            res.val = p_list.pop(0)
            q_list.pop(0)
        return res


if __name__ == '__main__':
    root = [3,5,1,6,2,0,8,None,None,7,4]
    p = [5]
    q = [1]
    root = build_bfs(root)
    p = build_bfs(p)
    q = build_bfs(q)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.lowestCommonAncestor(root, p, q))
    print(solution.lowestCommonAncestor1(root, p, q))
    pass