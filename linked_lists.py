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
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """You are given the head of a singly linked-list.
        The positions of a linked list of length = 7 for example, can intially be represented as: [0, 1, 2, 3, 4, 5, 6]
        Reorder the nodes of the linked list to be in the following order: [0, 6, 1, 5, 2, 4, 3]
        Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
        [0, n-1, 1, n-2, 2, n-3, ...]
        You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves."""
        if not head:
            return
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        right = slow.next
        prev = slow.next = None
        while right:
            next = right.next
            right.next = prev
            prev = right
            right = next
        left = head
        right = prev
        while right:
            temp1, temp2 = left.next, right.next 
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2
        
            
         
            
        
            
        
                
                            
        
        

         

solution = Solution()
head = [2,4,6,8]
list1 = ListNode(head[0])
current = list1
for val in head[1:]:
    current.next = ListNode(val)
    current = current.next

print(solution.reorderList(list1))


