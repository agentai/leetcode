#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/1

"""
文件说明：
    225. 用队列实现栈
输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False

    https://leetcode-cn.com/problems/implement-stack-using-queues/
"""
from typing import List


class MyStack:
    """
    执行用时：
40 ms
, 在所有 Python3 提交中击败了
58.96%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
39.03%
的用户
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.cache.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.cache.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.cache[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.cache) == 0

    def __str__(self):
        return str(self.cache)



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class Solution:

    def job(self, l1, l2):
        res = []
        tmp = None
        for x,y in zip(l1,l2):
            # print(x,y, tmp)
            if x == "MyStack":
                tmp = MyStack()
                res.append(None)
            elif x == "push":
                res.append(tmp.push(y[0]))
            elif x == "top":
                res.append(tmp.top())
            elif x == "pop":
                res.append(tmp.pop())
            elif x == "empty":
                res.append(tmp.empty())
        return res



if __name__ == '__main__':
    l1 = ["MyStack", "push", "push", "top", "pop", "empty"]
    l2 = [[], [1], [2], [], [], []]
    solution = Solution()
    print(solution.job(l1, l2))
    pass
