#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
23. 合并K个升序链表
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

https://leetcode-cn.com/problems/merge-k-sorted-lists/
"""
from typing import *
from base import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
执行用时：
184 ms
, 在所有 Python3 提交中击败了
22.19%
的用户
内存消耗：
17.7 MB
, 在所有 Python3 提交中击败了
65.03%
的用户
        """
        # 哨兵+多指针队列，用一个队列来标识当前所有指针
        def quick_sort(queue, l, r):
            if l >= r:
                return
            min_i = l
            base = queue[r].val
            for i in range(l, r):
                if queue[i].val <= base:
                    queue[min_i], queue[i] = queue[i], queue[min_i]
                    min_i += 1
            queue[r], queue[min_i] = queue[min_i], queue[r]
            quick_sort(queue, l, min_i-1)
            quick_sort(queue, min_i+1, r)

        def add_one(queue, cur):
            r = len(queue)
            while r > 0 and queue[r-1].val > cur.val:
                r -= 1
            queue.insert(r, cur)
            return queue

        guard = ListNode()
        queue = []
        for tmp in lists:
            if not tmp:
                continue
            queue.append(tmp)
        quick_sort(queue, 0, len(queue)-1)
        head = guard
        while queue:
            cur = queue.pop(0)
            head.next = cur
            cur = cur.next
            head = head.next
            if cur:
                queue = add_one(queue, cur)
        return guard.next

    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        """
        执行用时：
5320 ms
, 在所有 Python3 提交中击败了
5.43%
的用户
内存消耗：
17.5 MB
, 在所有 Python3 提交中击败了
91.72%
的用户
        """
        # 哨兵+多指针队列，用一个队列来标识当前所有指针
        guard = ListNode()
        queue = []
        for tmp in lists:
            if not tmp:
                continue
            queue.append(tmp)
        head = guard
        while queue:
            index = 0
            for cur in range(len(queue)):
                if queue[index].val > queue[cur].val:
                    index = cur
            min_val = queue.pop(index)
            head.next = min_val
            min_val = min_val.next
            if min_val:
                queue.append(min_val)
            head = head.next
        return guard.next


if __name__ == '__main__':
    nums = [[1,4,5],[1,3,4],[2,6]]
    k = 3
    # nums = build_bfs(nums)
    nums = create_lists_node(nums)
    solution = Solution()
    print(solution.mergeKLists(nums))

    pass