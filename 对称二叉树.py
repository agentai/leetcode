#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    101. 对称二叉树
例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3


但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

https://leetcode-cn.com/problems/symmetric-tree/

"""
from typing import List
from base import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
30.68%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
33.79%
的用户
        """
        # bfs，队列，每层队列进行二分判断
        queue = [root]
        while queue:
            new_queue = []
            for tmp in queue:
                # 不管是否为空，都先加上所有子节点
                if tmp:
                    new_queue.append(tmp.left)
                    new_queue.append(tmp.right)
                else:
                    new_queue.append(None)
                    new_queue.append(None)
            # 二分查找
            l,r = 0, len(new_queue)-1
            while l < r:
                # 左右对应的都为空或者数值相等，才对称
                if (not new_queue[l] and not new_queue[r]) or (new_queue[l] and new_queue[r] and new_queue[l].val == new_queue[r].val):
                    l += 1
                    r -= 1
                else:
                    return False
            # 过滤掉空的
            queue = list(filter(lambda x: x is not None, new_queue))
        return True


if __name__ == '__main__':
    nums = [1,2,2,3,4,4,3]
    nums = [1,2,2,None,3,None,3]
    tree = build_bfs(nums)
    solution = Solution()
    print(solution.isSymmetric(tree))

    pass