#!/usr/bin/env python3
# coding:utf-8
# Author:Lee
# 2020/4/28 19:05

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

思路：
先判断一下哪个链表长，然后用交换的方法确保一定是l1更长
然后把l2的值加到l1上，全部加完之后遍历l1处理进位，记得处理最后一位需要进1的特殊情况
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length1, length2 = 0, 0
        p = l1
        while p:
            length1 += 1
            p = p.next
        p = l2
        while p:
            length2 += 1
            p = p.next
        if length1 < length2:
            l1, l2 = l2, l1

        p1, p2 = l1, l2
        c = 0
        while p2:
            p1.val += p2.val
            p1 = p1.next
            p2 = p2.next
        p1 = l1
        while p1:
            p1.val += c
            c = 0
            if p1.val > 9:
                p1.val -= 10
                c = 1
            if not p1.next and c:
                p1.next = ListNode(1)
                break
            p1 = p1.next
        return l1

# 这道题涉及的链表知识有欠缺，解法来自网络，先记录再学习
# runtime:64 ms
# memory:13.7 MB


