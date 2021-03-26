#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/2/28

"""
文件说明：
    26. 删除有序数组中的重复项
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
    https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2gy9m/
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        执行用时：
48 ms
, 在所有 Python3 提交中击败了
62.43%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
32.31%
的用户
        """
        # 思路：快慢指针，慢指针只有在遇到不同的元素后才前进
        len_n = len(nums)
        if len_n <= 1:
            return len_n
        l = 0
        r = 1
        while r < len_n:
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1


    def removeDuplicates4(self, nums: List[int]) -> int:
        """
执行用时：
32 ms
, 在所有 Python3 提交中击败了
99.27%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
60.34%
的用户
        :param nums:
        :return:
        """
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        count = 0
        index = 0
        while index < len_nums:
            if nums[index] == nums[count]:
                index = index + 1
                continue
            else:
                count += 1
                nums[count] = nums[index]
                index = index + 1
        return count+1

    def removeDuplicates1(self, nums: List[int]) -> int:
        """
执行用时：
712 ms
, 在所有 Python3 提交中击败了
8.83%
的用户
内存消耗：
15.8 MB
, 在所有 Python3 提交中击败了
33.43%
的用户
        :param nums:
        :return:
        """
        index = 0
        while index < len(nums)-1:
            if nums[index+1] == nums[index]:
                nums.remove(nums[index+1])
            else:
                index = index+1
        return index+1


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    print(solution.removeDuplicates(nums))
    pass
