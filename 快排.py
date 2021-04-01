#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao

"""
文件说明：
快排
"""
from typing import *
from base import *


def quick_sort(nums, l, r):
    if l >= r:
        return
    # 基准的索引从左往右偏移
    # 先记录最小位置的索引作为基准
    min_i = l
    # 先把最右边的做基数
    base = nums[r]
    # 遍历[l,r)，如果当前数比基数小的都放到左边
    for i in range(l, r):
        # 如果当前数(queue[i])小于基数(base)，则和基准对调，并基准往右走
        if nums[i] <= base:
            # 与基准对调
            nums[i], nums[min_i] = nums[min_i], nums[i]
            # 基准往右走
            min_i += 1
    # 最后基准位置放基数
    nums[r], nums[min_i] = nums[min_i], nums[r]
    # 基准位置的左边肯定小于基准，右边肯定大于基准
    quick_sort(nums, l, min_i - 1)
    quick_sort(nums, min_i + 1, r)
    return


if __name__ == '__main__':
    nums = [5, 3, 4, 9, 6, 3, 8, 7, 1, 4]
    nums = [1, 2, 1, 1, 1]
    nums = [10, 7, 8, 9, 1, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
    pass