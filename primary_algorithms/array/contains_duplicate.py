#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    
"""
from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
71.86%
的用户
内存消耗：
19.7 MB
, 在所有 Python3 提交中击败了
80.80%
的用户
        :param nums:
        :return:
        """
        data = set()
        start = 0
        end = len(nums) - 1
        while start < end:
            if nums[start] in data or nums[end] in data or nums[start] == nums[end]:
                return True
            else:
                data.add(nums[start])
                data.add(nums[end])
                start += 1
                end -= 1
        return False

    def containsDuplicate3(self, nums: List[int]) -> bool:
        """
        执行用时：
220 ms
, 在所有 Python3 提交中击败了
5.31%
的用户
内存消耗：
19.2 MB
, 在所有 Python3 提交中击败了
80.83%
的用户
        :param nums:
        :return:
        """
        def resort_in(l_list, r_list):
            l = r = 0
            d = []
            while l<len(l_list) and r < len(r_list):
                if l_list[l] == r_list[r]:
                    return d, True
                if l_list[l] < r_list[r]:
                    d.append(l_list[l])
                    l += 1
                else:
                    d.append(r_list[r])
                    r += 1
            d.extend(l_list[l:])
            d.extend(r_list[r:])
            return d, False

        def resort(nums, tmp):
            if len(nums) == 1 or tmp:
                return nums, tmp
            index = int(len(nums)/2)
            left,tmp = resort(nums[0:index], tmp)
            if tmp:
                return nums, tmp
            right, tmp = resort(nums[index:], tmp)
            if tmp:
                return nums, tmp
            nums, tmp = resort_in(left, right)
            return nums, tmp
        _, tmp = resort(nums, False)
        return tmp


    def containsDuplicate2(self, nums: List[int]) -> bool:
        """
        执行用时：
40 ms
, 在所有 Python3 提交中击败了
87.32%
的用户
内存消耗：
20 MB
, 在所有 Python3 提交中击败了
65.98%
的用户
        :param nums:
        :return:
        """
        data = set()
        for num in nums:
            if num in data:
                return True
            else:
                data.add(num)
        return False

    def containsDuplicate1(self, nums: List[int]) -> bool:
        """
        执行用时：
44 ms
, 在所有 Python3 提交中击败了
71.86%
的用户
内存消耗：
20.1 MB
, 在所有 Python3 提交中击败了
55.48%
的用户
        :param nums:
        :return:
        """
        return not len(nums) == len(set(nums))


if __name__ == '__main__':
    nums = [1, 2, 2]
    solution = Solution()
    print(solution.containsDuplicate2(nums))
    pass
