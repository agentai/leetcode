#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/16

"""
文件说明：
    82. 删除排序链表中的重复元素 II
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
"""
from base import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
84.85%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
90.74%
的用户
        """
        # 思路：先建立一个哨兵指向head，然后head指向哨兵，因为第一个元素就有可能重复
        # 然后做个快慢指针，慢指针的next是快指针，判断快的指针的值和其next是否一致，
        # 一致的话记录这个值，并且快指针一直往后走，直到快指针的next与这个值不一致为止，然后慢指针指向快指针的next

        # 先创建哨兵
        slow = ListNode()
        slow.next = head
        head = slow
        # 慢指针从哨兵出发，快指针是慢指针的next（关键）
        fast = slow.next
        # 因为循环里需要判断fast.val和fast.next.val，所以需要fast和fast.next都有值
        while fast and fast.next:
            # 如果fast.val和fast.next.val一致，取当前值，并把fast往后走，一致到fast.next为空或者fast.next.val不等于当前值
            if fast.val == fast.next.val:
                cur_val = fast.val
                while fast.next and fast.next.val == cur_val:
                    fast = fast.next
                slow.next = fast.next
            else:
                # 不同了以后，慢指针才走一步
                slow = slow.next
            # 快指针是慢指针的next
            fast = slow.next
        return head.next


if __name__ == '__main__':
    # nums = [1,2,3,3,4,4,5, 5, 5,6]
    nums = [1,1,1,2,3]
    solution = Solution()
    print(solution.deleteDuplicates(create_list_node(nums)))
    pass