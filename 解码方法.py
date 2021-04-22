#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
91. 解码方法

一条包含字母A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：

"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)
注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。

示例 1：

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

示例 2：

输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

示例 3：

输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。

示例 4：

输入：s = "06"
输出：0
解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。

https://leetcode-cn.com/problems/decode-ways
"""
from typing import *
from base import *


class Solution:
    def numDecodings1(self, s: str) -> int:
        # 递归求解，注意边界即可
        res = []
        len_s = len(s)

        def sub(k, cur):
            # k是当前的索引，cur是
            if k >= len_s:
                tmp = ",".join(cur)
                if tmp not in res:
                    res.append(tmp)
                return
            if s[k] == "0":
                return
            cur.append(s[k])
            sub(k+1, cur)
            cur.pop()
            if k+1 < len_s and int(s[k:k+2]) <= 26:
                cur.append(s[k:k+2])
                sub(k+2, cur)
                cur.pop()
        sub(0, [])
        return len(res)

    def numDecodings(self, s: str) -> int:
        """
        执行用时：
28 ms
, 在所有 Python3 提交中击败了
99.37%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
67.58%
的用户
        """
        # 动态规划，dp[i]表示s[i:]内所有编码的次数
        # 从后往前遍历
        # if s[i] == "0" continue
        # if s[i:i+2] < '26' dp[1] = dp[i+1] + dp[i+2]
        len_s = len(s)
        dp = [0] * len_s
        for i in range(len_s-1, -1, -1):
            if s[i] != "0":
                if i == len_s-1:
                    dp[i] = 1
                else:
                    dp[i] = dp[i + 1]
                    if int(s[i:i+2]) <= 26:
                        if i == len_s-2:
                            dp[i] += 1
                        else:
                            dp[i] += dp[i+2]
        return dp[0]


if __name__ == '__main__':
    nums = "226"
    # nums = "06"
    # nums = "11106"
    # nums = "27"
    nums = "111111111111111111111111111111111111111111111"
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    # print(solution.numDecodings1(nums))
    print(solution.numDecodings(nums))
    pass