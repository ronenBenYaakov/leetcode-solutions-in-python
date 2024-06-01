# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s, t, p1, p2 = "", "", l1, l2

        while p1 is not None:
            s += str(p1.val)
            p1 = p1.next

        while p2 is not None:
            t += str(p2.val)
            p2 = p2.next

        x = int(s) + int(t)
        s = str(x)
        
        l = ListNode()
        res = l
        for i in range(len(s)):
            l.val = int(s[i])
            if i != len(s) - 1:
                l.next = ListNode()
                l = l.next

        return res
