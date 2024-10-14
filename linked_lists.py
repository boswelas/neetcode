# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list."""
        if not head:
            return None
        
        prev = None
        curr = head
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev   
            
            
        
        

         

solution = Solution()
head = [0,1,2,3]
list1 = ListNode(head[0])
current = list1
for val in head[1:]:
    current.next = ListNode(val)
    current = current.next
print(solution.reverseList(list1))


