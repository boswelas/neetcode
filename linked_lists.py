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
            
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
        The new list should be made up of nodes from list1 and list2."""
        dummy = ListNode()
        curr = dummy
        
        l1_curr = list1
        l2_curr = list2
        
        while l1_curr and l2_curr:
            if l1_curr.val < l2_curr.val:
                curr.next = l1_curr
                l1_curr = l1_curr.next
                curr = curr.next
            else:
                curr.next = l2_curr
                l2_curr = l2_curr.next
                curr = curr.next
                
        if not l1_curr:
            curr.next = l2_curr
        else:
            curr.next = l1_curr
        return dummy.next
                
                            
        
        

         

solution = Solution()
head1 = [1,2,4] 
head2 = [1,3,5]
list1 = ListNode(head1[0])
current = list1
for val in head1[1:]:
    current.next = ListNode(val)
    current = current.next
    
list2 = ListNode(head2[0])
current = list2
for val in head2[1:]:
    current.next = ListNode(val)
    current = current.next
print(solution.mergeTwoLists(list1, list2).val)


