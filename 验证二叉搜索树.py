#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
98. 验证二叉搜索树

示例1:

输入:
    2
   / \
  1   3
输出: true
示例2:

输入:
    5
   / \
  1   4
    / \
   3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
    根节点的值为 5 ，但是其右子节点值为 4 。


https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
from typing import *
from base import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST1(self, root: TreeNode) -> bool:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
75.68%
的用户
内存消耗：
17.8 MB
, 在所有 Python3 提交中击败了
13.91%
的用户
        """
        # dfs，每次返回节点的最大值和最小值

        def get_mix_max(node):
            l_min_v = r_max_v = node.val
            if node.left:
                # 如果存在左树，返回左树的最大最小值
                is_bst, l_min_v, l_max_v = get_mix_max(node.left)
                # 如果左树的最大值大于当前节点，返回失败
                if not is_bst or l_max_v >= node.val:
                    return False, 0, 0
            if node.right:
                # 如果存在右树，返回右树的最大最小值
                is_bst, r_min_v, r_max_v = get_mix_max(node.right)
                # 如果右树的最小值小于当前节点，返回失败
                if not is_bst or r_min_v <= node.val:
                    return False, 0, 0
            # 最终返回左树的最小值 l_min_v 和右树的最大值 r_max_v 作为当前节点的最小最大值
            return True, l_min_v, r_max_v

        is_bst, _, _ = get_mix_max(root)
        return is_bst

    def isValidBST(self, root: TreeNode) -> bool:
        """
        执行用时：
56 ms
, 在所有 Python3 提交中击败了
54.71%
的用户
内存消耗：
17.8 MB
, 在所有 Python3 提交中击败了
18.29%
的用户
        """
        # 中序遍历
        if not root:
            return True
        # res = []
        cur_min = [float('-inf')]

        def dfs(node):
            if node.left:
                if not dfs(node.left):
                    return False
            if cur_min[0] >= node.val:
                return False
            # res.append(node.val)
            cur_min[0] = node.val
            if node.right:
                if not dfs(node.right):
                    return False
            return True
        # dfs(root)
        # print(res)
        return dfs(root)



if __name__ == '__main__':
    nums = [5,1,4,None,None,3,6]
    nums = [5,4,6,None,None,3,7]
    nums = [2, 1, 4]
    # nums = [1,1]
    k = 3
    nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.isValidBST(nums))
    pass