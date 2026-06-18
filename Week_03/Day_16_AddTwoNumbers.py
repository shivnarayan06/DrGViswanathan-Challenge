# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        check = ListNode(-1)
        tail = check
        carry = 0
        currSum = 0
        while l1 is not None or l2 is not None or carry>0:
            if l1 is not None:
                val1 = l1.val
                l1=l1.next
            else:
                val1 = 0
            if l2 is not None:
                val2 = l2.val
                l2=l2.next
            else:
                val2 = 0
            currSum= val1 + val2 + carry
            carry = currSum//10
            digit = currSum%10
            tail.next = ListNode(digit)
            tail = tail.next    
        return check.next

