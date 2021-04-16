#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：

199. 二叉树的右视图

给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入:[1,2,3,null,5,null,4]
输出:[1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

https://leetcode-cn.com/problems/binary-tree-right-side-view

"""
from typing import *
from base import *


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        执行用时：
28 ms
, 在所有 Python3 提交中击败了
99.43%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
85.65%
的用户
        """
        # bfs，每次取最右的节点加入到结果中
        if not root:
            return []
        # res = []
        # queue = [root]
        # while queue:
        #     size = len(queue)
        #     node = None
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(node.val)
        # return res
        res = []
        # 用deque可用加速，因为是双向队列，访问对尾可用达到o(1)的复杂度
        queue = deque([root])
        while queue:
            size = len(queue)
            node = None
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)
        return res


if __name__ == '__main__':
    nums = [1,2,3,None,5,None,4]
    nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.rightSideView(nums))
    pass