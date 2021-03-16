#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/7

"""
文件说明：
    
"""
import collections
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        执行用时：
64 ms
, 在所有 Python3 提交中击败了
46.63%
的用户
内存消耗：
19.7 MB
, 在所有 Python3 提交中击败了
7.26%
的用户
        :param strs:
        :return:
        """
        res = {}
        for str1 in strs:
            key_str = [0] * 26
            for tmp_str in str1:
                key_str[ord(tmp_str) - 97] += 1
            key1 = tuple(key_str)
            if key1 in res:
                res[key1].append(str1)
            else:
                res[key1] = [str1]
        return list(res.values())

    def groupAnagrams6(self, strs: List[str]) -> List[List[str]]:
        """
        执行用时：
64 ms
, 在所有 Python3 提交中击败了
46.63%
的用户
内存消耗：
19.9 MB
, 在所有 Python3 提交中击败了
5.03%
的用户
        :param strs:
        :return:
        """
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())


    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """
        执行用时：
152 ms
, 在所有 Python3 提交中击败了
8.10%
的用户
内存消耗：
18.2 MB
, 在所有 Python3 提交中击败了
23.65%
的用户
        :param strs:
        :return:
        """
        def change2str(str1):
            key_str = [0 for i in range(26)]
            for tmp_str in str1:
                index = ord(tmp_str)-97
                key_str[index] = key_str[index] + 1
            return ",".join([str(x) for x in key_str])
        if len(strs) == 0:
            return []
        res = {change2str(strs[0]): [strs[0]]}
        for str1 in strs[1:]:
            key1 = change2str(str1)
            if key1 in res:
                res[key1].append(str1)
            else:
                res[key1] = [str1]
        return list(res.values())


    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        """
        执行用时：
8524 ms
, 在所有 Python3 提交中击败了
5.01%
的用户
内存消耗：
17 MB
, 在所有 Python3 提交中击败了
95.05%
的用户

        :param strs:
        :return:
        """
        def is_match(str1, str2):
            tmp = {}
            if len(str1) != len(str2):
                return False
            else:
                for tmp_str in str1:
                    if tmp_str not in str2:
                        return False
                    tmp[tmp_str] = tmp.get(tmp_str, 0) + 1
                for tmp_str in str2:
                    if tmp_str not in tmp:
                        return False
                    if tmp.get(tmp_str, 0) < 1:
                        return False
                    tmp[tmp_str] = tmp[tmp_str] - 1
            return True

        if len(strs) == 0:
            return []
        res = {strs[0]:[strs[0]]}
        for str1 in strs[1:]:
            has_match = False
            for str2 in res.keys():
                if is_match(str1, str2):
                    tmp = res.get(str2, [])
                    tmp.append(str1)
                    res[str2] = tmp
                    has_match = True
            if not has_match:
                res[str1] = [str1]
        return list(res.values())


if __name__ == '__main__':
    nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
    nums = ["bdddddddddd","bbbbbbbbbbc"]
    # print(ord(nums[0][1])-97)
    solution = Solution()
    print(solution.groupAnagrams(nums))
    pass
