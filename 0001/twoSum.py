#!/usr/bin/env python3
# coding:utf-8
# Author:Lee
# 2020/4/26 19:44

"""
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

思路：
1. 将nums组合为一个索引序列
2. 通过for循环取出索引和值
3. 用hashmap记录之前出现的索引和值

结果：
执行耗时:64 ms,击败了55.08% 的Python3用户
内存消耗:15 MB,击败了5.48% 的Python3用户
"""


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return hashmap[target - num], index
            hashmap[num] = index
