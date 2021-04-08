#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
781. 森林中的兔子

示例:
输入: answers = [1, 1, 2]
输出: 5
解释:
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。

输入: answers = [10, 10, 10]
输出: 11

输入: answers = []
输出: 0

https://leetcode-cn.com/problems/rabbits-in-forest/

"""
from typing import *
from base import *


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        执行用时：
56 ms
, 在所有 Python3 提交中击败了
48.62%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
43.09%
的用户
        """
        # 看题解，如果有13(y)个兔子都回答了5(x)个，那么假设有6(x+1)个是红色且都在13个兔子里，那么至少有ceil(13/(5+1))*(5+1)个兔子，ceil(y/(x+1))*(x+1)，其中y/(x+1)需要向上取整。
        # ceil(y/(x+1)) = (y+x)//(x+1) ，向上取整的算法 ceil(A/B)=(A+B+1)//B
        # 最终公式，count = ((y+x)//(x+1))*(x+1)
        # 只需要统计回答值(x)一致的兔子的个数(y)，然后依次套用公式，结果求和就是最终结果
        data = {}
        for i in answers:
            data[i] = 1 + data.get(i, 0)
        res = 0
        for x, y in data.items():
            res += ((x+y)//(x+1))*(x+1)
        return res


if __name__ == '__main__':
    nums = [1,0,1,0,0]
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.numRabbits(nums))
    pass