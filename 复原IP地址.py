#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
93. 复原 IP 地址

给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

https://leetcode-cn.com/problems/restore-ip-addresses
"""
from typing import *
from base import *


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        执行用时：
36 ms
, 在所有 Python3 提交中击败了
94.37%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
49.69%
的用户
        """
        # 字符分四段，每段数在0-255之间
        len_s = len(s)
        if len_s < 4:
            return []
        res = []
        a = 1
        while a <= 3:
            if a >= len_s - 2 or (a > 1 and s[0] == "0"):
                break
            if int(s[0:a]) <= 255:
                b = 1
                while b <= 3:
                    if a + b >= len_s - 1 or (b > 1 and s[a] == "0"):
                        break
                    if int(s[a:a+b]) <= 255:
                        c = 1
                        while c <= 3:
                            index = a + b + c
                            if index >= len_s:
                                break
                            if len_s - index > 3 or (c > 1 and s[a+b] == "0") or (len_s - index > 1 and s[index] == "0"):
                                c += 1
                                continue
                            if int(s[a+b:index]) <= 255 and int(s[index:]) <= 255:
                                tmp = f"{int(s[0:a])}.{int(s[a:a+b])}.{int(s[a+b:index])}.{int(s[index:])}"
                                if tmp not in res:
                                    res.append(tmp)
                            c += 1
                    b += 1
            a += 1
        return res


if __name__ == '__main__':
    nums = "101023"
    nums = "010010"
    k = 3
    # nums = build_bfs(nums)
    # nums = create_list_node(nums)
    solution = Solution()
    print(solution.restoreIpAddresses(nums))
    pass