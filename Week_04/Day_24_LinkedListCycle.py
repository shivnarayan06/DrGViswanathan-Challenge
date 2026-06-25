# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = set()
        temp = head
        while temp is not None:
            temp = temp.next
            if temp not in arr:
                arr.add(temp)
            else :
                return True
        return False
        