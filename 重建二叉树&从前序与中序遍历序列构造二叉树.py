#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
剑指 Offer 07. 重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

前序遍历 preorder =[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof


105. 从前序与中序遍历序列构造二叉树


"""
from typing import *
from base import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        执行用时：
612 ms
, 在所有 Python3 提交中击败了
5.05%
的用户
内存消耗：
87.7 MB
, 在所有 Python3 提交中击败了
7.18%
的用户
        """
        # 前序：根 左 右 中序：左 根 右
        """
        前序遍历 preorder =[3,9,20,15,7]
        中序遍历 inorder = [9,3,15,20,7]
        """
        if not preorder:
            return None

        def sub(pre_order, in_order):
            # pre_order[0]是根
            p = i = 0
            root_val = pre_order[p]
            tmp = TreeNode(val=root_val)
            # in_order到根之前的数都是左子树
            a = i
            # in_order遍历到根
            while a < len(in_order) and in_order[a] != root_val:
                a += 1
            # 根左边的都是左子树
            if a > i:
                tmp.left = sub(pre_order[p+1:a-i+p+1], in_order[i:a])
            # 如果没到底，根右边的都是右子树
            if a < len(in_order)-1:
                tmp.right = sub(pre_order[a-i+p+1:], in_order[a+1:])
            return tmp
        return sub(preorder, inorder)


if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.buildTree(preorder, inorder))
    pass