#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/16

"""
文件说明：
    337. 打家劫舍 III
"""
from typing import List
from tree import *


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        执行用时：
52 ms
, 在所有 Python3 提交中击败了
90.82%
的用户
内存消耗：
16.8 MB
, 在所有 Python3 提交中击败了
31.56%
的用户
        :param root:
        :return:
        """
        def max(a, b):
            if a > b:
                return a
            return b

        def helper(root: TreeNode):
            if not root:
                return [0, 0]
            dpl = helper(root.left)
            dpr = helper(root.right)
            dp = [dpl[1] + dpr[1] + root.val, max(dpl[0], dpl[1]) + max(dpr[0], dpr[1])]
            # dp = [max(dpl[0], dpl[1]) + max(dpr[0], dpr[1]), dpl[1] + dpr[1] + root.val]
            return dp

        dp = helper(root)
        return max(dp[0], dp[1])
        pass


if __name__ == '__main__':
    nums = [3, 2, 3, None, 3, None, 1]
    tree = build_bfs(nums)
    solution = Solution()
    print(solution.rob(tree))
    pass
