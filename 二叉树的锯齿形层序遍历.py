#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
103. 二叉树的锯齿形层序遍历

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
"""
from typing import *
from base import *


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
43.56%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
60.98%
的用户
        """
        # 逐层遍历，用一个队列来存
        if not root:
            return []
        direction_l = True
        queue = [root]
        res = []

        while queue:
            new_queue = []
            tmp = []
            for node in queue:
                if direction_l:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            direction_l = not direction_l
            res.append(tmp)
        return res


if __name__ == '__main__':
    nums = [3,9,20,None,None,15,7]
    nums = [1,2,3,4,None,None,5]
    nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.zigzagLevelOrder(nums))
    pass