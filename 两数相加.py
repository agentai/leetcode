#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/16

"""
文件说明：
    2. 两数相加
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
    https://leetcode-cn.com/problems/add-two-numbers/
"""
from typing import List
from list import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        执行用时：
76 ms
, 在所有 Python3 提交中击败了
36.51%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
34.89%
的用户
        """
        # 思路：加一个进阶位，依次从l1和l2中取数，直到进阶位为0且l1,l2其中一个结束为止
        plus = 0
        new_l = ListNode()
        head = new_l
        while plus or l1 or l2:
            # 当 l1 和 l2 都为空了，说明有plus，则new_l尾部加1
            if not (l1 or l2):
                new_l.next = ListNode(1)
                return head.next
            # 当l1和l2都有，两个同步加，且往后走
            if l1 and l2:
                tmp = l1.val + l2.val+plus
                plus = tmp // 10
                new_l.next = ListNode(val=tmp % 10)
                new_l = new_l.next
                l1 = l1.next
                l2 = l2.next
                continue
            # 当其中一个到底了，计算另一个，直到不满足循环条件
            if not l1:
                tmp = l2.val + plus
                plus = tmp // 10
                new_l.next = ListNode(val=tmp % 10, next=l2.next)
                new_l = new_l.next
                l2 = l2.next
            else:
                tmp = l1.val + plus
                plus = tmp // 10
                new_l.next = ListNode(val=tmp % 10, next=l1.next)
                new_l = new_l.next
                l1 = l1.next
        return head.next


if __name__ == '__main__':
    nums1 = [2, 4, 6]
    nums2 = [5, 6, 4, 5, 1]
    solution = Solution()
    print(solution.addTwoNumbers(create_list_node(nums1), create_list_node(nums2)))
    pass