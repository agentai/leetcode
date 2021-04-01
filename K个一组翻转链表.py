#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
25. K 个一组翻转链表

输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

"""
from typing import *
from base import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
88.49%
的用户
内存消耗：
15.5 MB
, 在所有 Python3 提交中击败了
69.74%
的用户
        """
        # 双指针
        r = l = head
        while l:
            count = 0
            nums = []
            while count < k and r:
                count += 1
                nums.append(r.val)
                r = r.next
            if count == k:
                r = l
                while nums:
                    r.val = nums.pop()
                    r = r.next
            l = r
        return head


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 2
    # nums = build_bfs(nums)
    nums = create_list_node(nums)
    solution = Solution()
    print(solution.reverseKGroup(nums, k))
    pass