# 记录其他解法

```python
# source leetcode.com
# runtime:84 ms
# memory:13.6 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur =ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //=10
        return dummy.next
```

```python
# source leetcode.com
# runtime:86 ms
# memory:13.7 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_string = ""
        while l1:
            l1_string = str(l1.val) + l1_string
            l1 = l1.next

        l2_string = ""
        while l2:
            l2_string = str(l2.val) + l2_string
            l2 = l2.next

        l_sum = str(int(l1_string) + int(l2_string))

        l3 = ListNode(int(l_sum[-1]))
        itr = l3

        for numIdx in range(-2, -len(l_sum) - 1, -1):
            itr.next = ListNode(int(l_sum[numIdx]))
            itr = itr.next

        return l3
```

```python
# source leetcode.com
# runtime:84 ms
# memory:13.9 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _ = l1.val + l2.val
        digit, tenth = _ % 10, _ // 10
        answer = ListNode(digit)
        if any((l1.next, l2.next, tenth)):
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)
            l1.val += tenth
            answer.next = self.addTwoNumbers(l1, l2)
        return answer
```

```python
# source leetcode.com
# runtime:76 ms
# memory:13.7 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumval = 0
        root = curr = ListNode(0)
        while l1 or l2 or sumval:
            if l1: sumval += l1.val; l1 = l1.next
            if l2: sumval += l2.val; l2 = l2.next
            curr.next = curr = ListNode(sumval % 10)
            sumval //= 10
        return root.next

```

```python
# source leetcode-cn.com
# runtime:104 ms
# memory:13.6 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if self.getLength(l1) < self.getLength(l2):  # 保证l1永远比l2更长
            l1, l2 = l2, l1

        head = l1
        while (l2):  # 执行加法
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next

        p = head
        while (p):  # 处理进位
            if p.val > 9:
                p.val -= 10
                if p.next:
                    p.next.val += 1
                else:
                    p.next = ListNode(1)
            p = p.next

        return head

    def getLength(self, l):  # 计算链表长度
        length = 0
        while (l):
            length += 1
            l = l.next
        return length
```