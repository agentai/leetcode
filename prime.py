#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2021/3/2

"""
文件说明：
    质数判断
    https://blog.csdn.net/weixin_42196908/article/details/81130061?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control
"""
from typing import List


class Calculator(object):
    def prime(self, n):
        if n <= 2:
            return 0
        is_right = [True] * n
        is_right[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_right[i]:
                for j in range(i * i, n, i):
                    is_right[j] = False
        m = 0
        for x in range(2, n):
            if is_right[x]:
                m += 1
        return m


if __name__ == '__main__':
    solution = Calculator()
    print(solution.prime(120))
    pass
