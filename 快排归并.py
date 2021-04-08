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


def quick_sort1(nums, l, r):
    # 先确定一个基准索引(l)和基数nums[r]
    # 基准索引记录比基数小的位置，从基准索引开始遍历，遍历范围为[l,r)
    # 所有比基数小的数与基准对调，然后基准后移
    # 然后把当前基准索引换成是基数
    # 在对基准左边和基准右边做递归分治排序
    if l >= r:
        return
    base_index = l
    base_num = nums[r]
    for i in range(l, r):
        if nums[i] <= base_num:
            nums[i], nums[base_index] = nums[base_index], nums[i]
            base_index += 1
    nums[base_index], nums[r] = nums[r], nums[base_index]
    quick_sort1(nums, l, base_index-1)
    quick_sort1(nums, base_index+1, r)


def merge_sort(nums, l, r):
    """空间复杂度为 O(1)的归并排序
    参考： https://blog.csdn.net/kexuanxiu1163/article/details/107398372
    技巧，在一个数中同时保留原始数和排序后的数，通过取余的方式来保留原始数，通过取模的方式来保留排序后的数
    """
    if r - l <= 1:
        if nums[l] > nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        return
    m = (l+r)//2
    # 先处理好左右
    merge_sort(nums, l, m)
    merge_sort(nums, min(m+1, r), r)
    # 对于数组中两个元素 arr[i] 和 arr[j]，要将这两个元素保存到数组下标为 i 的数当中，我们可以通过取模和求余运算来实现。
    ## 相当于用余来记录当前的数，用模来记录当前排序后的值，所以需要有个当前情况下的最大值+1来作为分界线
    # 合并左右，空间复杂度为O(1)的方式
    min_index, i, j = l, l, min(m+1, r)
    # 取当前范围内最大的值+1作为分界线
    max_num = max(nums[m], nums[r])+1
    # 左右一起遍历
    while i <= m and j <= r:
        # 取余来获取当前位置的值
        if nums[i] % max_num <= nums[j] % max_num:
            # 比较后大的数 * 分界线 来保留排序后的数
            nums[min_index] += (nums[i] % max_num) * max_num
            i += 1
        else:
            nums[min_index] += (nums[j] % max_num) * max_num
            j += 1
        min_index += 1
    while i <= m:
        nums[min_index] += (nums[i] % max_num) * max_num
        min_index += 1
        i += 1
    while j <= r:
        nums[min_index] += (nums[j] % max_num) * max_num
        min_index += 1
        j += 1
    # 最后取模来获取排序后的数
    for i in range(l, r+1):
        nums[i] //= max_num


def merge_sort1(nums, l, r):
    """空间复杂度O(nlogn)"""
    if r - l <= 1:
        if nums[l] > nums[r]:
            nums[r], nums[l] = nums[l], nums[r]
        return
    m = (l+r)//2
    merge_sort1(nums, l, m)
    merge_sort1(nums, min(m+1, r), r)
    new_nums = []
    i, j = l, min(m+1, r)
    while i <= m and j <= r:
        if nums[i] < nums[j]:
            new_nums.append(nums[i])
            i += 1
        else:
            new_nums.append(nums[j])
            j += 1
    while i <= m:
        new_nums.append(nums[i])
        i += 1
    while j <= r:
        new_nums.append(nums[j])
        j += 1
    for i in range(l, r+1):
        nums[i] = new_nums.pop(0)


if __name__ == '__main__':
    nums = [5, 3, 4, 9, 6, 3, 8, 7, 1, 4]
    # nums = [1, 2, 1, 1, 1]
    # nums = [10, 7, 8, 9, 1, 5]
    # quick_sort(nums, 0, len(nums) - 1)
    merge_sort1(nums, 0, len(nums) - 1)
    print(nums)
    pass