#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : chitao
# @Time    : 2020/6/24 2:46 下午
# @Email   : chitao@staff.weibo.com

"""
文件说明：
    基础数学表达式+-*/()和数字，
"""

# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def process_expression(self, expression: str) -> float:
        # 依次读取字符，数字串转为数字，加入到栈中，遇到+-*/ 从栈中去数字，如果有的话做对应操作，如果没有的话，返回失败
        # 如果括号没有成对出现，则返回异常
        # 遇到括号是子问题，每个括号内肯定能返回一个计算结果

        def process_nums(nums):
            # 最后处理+-
            while len(nums) > 2:
                if nums[1] == "+":
                    nums[2] += nums[0]
                    nums = nums[2:]
                elif nums[1] == "-":
                    nums[0] -= nums[2]
                    nums[2] = nums[0]
                    nums = nums[2:]
            if len(nums) != 1:
                raise Exception("err2")
            return nums

        def process_chengchu(nums, num):
            # 一有*/就处理
            if len(nums) > 1:
                if nums[-1] == "*":
                    nums[-2] *= num
                    nums.pop(-1)
                elif nums[-1] == "/":
                    nums[-2] /= num
                    nums.pop(-1)
                else:
                    nums.append(num)
            else:
                nums.append(num)
            return nums

        len_e = len(expression)

        def sub_job(index, has_kuohao):
            nums = []
            while index < len_e:
                if expression[index] == " ":
                    index += 1
                num_l = index
                # 取数字
                while index < len_e and expression[index] in "0123456789":
                    index += 1
                # 如果确实存在数字，如果已经有符号且数队列中有数，则进行计算，否则加入nums
                if index > num_l:
                    num = int(expression[num_l:index])
                    nums = process_chengchu(nums, num)
                    continue
                # 如果遇到")" 判断
                elif expression[index] == ")":
                    index += 1
                    if not has_kuohao:
                        raise Exception("err1")
                    # 到边缘了，计算nums
                    nums = process_nums(nums)
                    return nums[0], index
                elif expression[index] == "(":
                    # 递归算括号内的表达式
                    num, index = sub_job(index+1, True)
                    # 括号内表达式算完后，处理乘除
                    nums = process_chengchu(nums, num)
                elif expression[index] in "+-*/":
                    nums.append(expression[index])
                else:
                    raise Exception("err4")
                index += 1
            nums = process_nums(nums)
            if has_kuohao:
                raise Exception("err3")
            return nums[0], index
        try:
            res, index = sub_job(0, False)
            print(expression + "=" + str(res))
            return res
        except:
            print(expression+" 表达式错误")

    def calculate(self, s: str) -> int:
        # 用一个nums来存具体数值和运算符号，遇到*/先算，最后算+-
        # 遇到括号，递归算子问题
        len_s = len(s)

        def process_chengchu(nums, num):
            if len(nums) > 1:
                if nums[-1] == "*":
                    nums[-2] *= num
                    nums.pop()
                    return nums
                if nums[-1] == "/":
                    nums[-2] /= num
                    nums.pop()
                    return nums
            nums.append(num)
            return nums

        def process_nums(nums):
            while len(nums) > 2:
                if nums[1] == "+":
                    nums[2] += nums[0]
                    nums = nums[2:]
                elif nums[1] == "-":
                    nums[0] -= nums[2]
                    nums[2] = nums[0]
                    nums = nums[2:]
            return nums[0]

        def sub_job(index, has_kuohao):
            nums = []
            while index < len_s:
                if s[index] == " ":
                    index += 1
                    continue
                # 记录数字起点
                num_l = index
                while index < len_s and s[index] in "0123456789":
                    index += 1
                if index > num_l:
                    num = int(s[num_l:index])
                    nums = process_chengchu(nums, num)
                    continue
                # 遇到（ 计算子表达式
                if s[index] == "(":
                    index += 1
                    num, index = sub_job(index, True)
                    nums = process_chengchu(nums, num)
                    continue
                elif s[index] == ")":
                    index += 1
                    if not has_kuohao:
                        raise Exception("1")
                    return process_nums(nums), index
                elif s[index] in "+-*/":
                    # 如果 - 开头，需要加上0
                    if len(nums) == 0:
                        if s[index] in "+-":
                            nums.append(0)
                    nums.append(s[index])
                index += 1
            return process_nums(nums), index

        num, index = sub_job(0, False)
        print(f"{s}={num}")
        return num

    def calculate224(self, s: str) -> int:
        """
        224. 基本计算器
https://leetcode-cn.com/problems/basic-calculator/
        """
        ops = [1]
        sign = 1

        ret = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = ops[-1]
                i += 1
            elif s[i] == '-':
                sign = -ops[-1]
                i += 1
            elif s[i] == '(':
                ops.append(sign)
                i += 1
            elif s[i] == ')':
                ops.pop()
                i += 1
            else:
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                ret += num * sign
        return ret

    def calculate1(self, s: str) -> int:
        # 思路，用一个队列存计算队列，如果遇到乘除，先算，遇到括号，递归算，最后算加减
        len_s = len(s)

        def process_chengchu(stack):
            while len(stack) > 2 and stack[-2] in "*/":
                if stack:
                    if stack[-2] == "*":
                        stack[-3] *= stack[-1]
                        stack.pop()
                        stack.pop()
                    elif stack[-2] == "/":
                        stack[-3] /= stack[-1]
                        stack.pop()
                        stack.pop()
                    else:
                        break
                else:
                    break

        def process_jiajian(stack):
            while len(stack) > 2 and stack[1] in "+-":
                # 处理加减的时候，需要正序
                if stack:
                    if stack[1] == "+":
                        stack[2] += stack[0]
                        stack.pop(0)
                        stack.pop(0)
                    elif stack[1] == "-":
                        # 处理减的时候，需要左减右
                        stack[0] -= stack[2]
                        stack[2] = stack[0]
                        stack.pop(0)
                        stack.pop(0)
                    else:
                        break
                else:
                    break

        def sub_job(i, has_kuohao):
            stack = []
            while i < len_s:
                while i < len_s and s[i] == " ":
                    i += 1
                j = i
                while j < len_s and s[j] in "0123456789":
                    j += 1
                if j > i:
                    num = int(s[i:j])
                    stack.append(num)
                    process_chengchu(stack)
                    i = j
                    continue
                if i == len_s:
                    break
                if s[i] in "+-*/":
                    if s[i] in "+-" and not stack:
                        stack.append(0)
                    if s[i] in "*/" and not stack:
                        stack.append(1)
                    stack.append(s[i])
                    i += 1
                elif s[i] == "(":
                    num, index = sub_job(i+1, True)
                    stack.append(num)
                    i = index
                    process_chengchu(stack)
                elif s[i] == ")":
                    if not has_kuohao:
                        raise Exception()
                    process_jiajian(stack)
                    i += 1
                    break
            if stack:
                process_jiajian(stack)
                return stack[-1], i
            else:
                return 0, i
        num, i = sub_job(0, False)
        print(f"{s}={num}")
        return num


# Solution().process_expression(" 11+2*(14*20/2)")
# Solution().process_expression("11+ 2* (14*20/3)")
# Solution().process_expression("11+2*2*(3*20/2)")
Solution().calculate("111*10+1-(-15*20/2-10)")
Solution().calculate1("111*10+1-(-15*20/2-10)")
# Solution().process_expression("111*10+1(15*20/2-10)")
# Solution().process_expression("111*10+1-15*20/2-10)")
# Solution().process_expression("15*20-10")
# Solution().process_expression("15*2d0-10")
# Solution().process_expression("15*(20-10")
#
# print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))
# print(Solution().calculate("-2+ 1"))


