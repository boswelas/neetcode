# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
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
                    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """You are given the beginning of a linked list head, and an integer n.
        Remove the nth node from the end of the list and return the beginning of the list."""
        dummy = ListNode()
        dummy.next = head
        
        l, r = head, dummy
        
        while True:
            while n > 0:
                r = r.next
                n -= 1
            while r:
                r = r.next
                prev = l
                l = l.next
            prev.next = l.next
            return dummy.next.val

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None:None}
        
        curr = head
        while curr:
            new_node = Node(curr.val)
            nodes[curr] = new_node
            curr = curr.next
            
        curr = head
        while curr:
            temp = nodes[curr]
            temp.next = nodes[curr.next]
            temp.random = nodes[curr.random]
            curr = curr.next
        return nodes[head]
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        plusOne = 0
        while l1 or l2 or plusOne:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1 + val2 + plusOne
            plusOne = 0
            if temp > 9:
                plusOne = 1
                temp = temp % 10           
            curr.next = ListNode(temp)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return dummy.next       
             
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        
        while fast and fast.next:
            if fast.next == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        
        return False
   
    def findDuplicate(self, nums: List[int]) -> int:
        """You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
        Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears 
        more than once."""
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.keys = []
        self.store = {}
        
    def get(self, key: int) -> int:
        if key in self.keys:
            self.keys.append(self.keys.pop(self.keys.index(key)))
        return self.store.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.store[key] = value
        else:
            if len(self.keys) == self.size:
                del self.store[self.keys[0]]
                self.keys.pop(0)
            self.store[key] = value
            self.keys.append(key)
                
        

lRUCache = LRUCache(2)
print(lRUCache.put(1, 1));  # cache: {1=10}
print(lRUCache.put(2, 2));  # cache: {1=10}
print(lRUCache.get(1));      # return 10
print(lRUCache.put(3, 3));  # cache: {1=10}
print(lRUCache.put(2, 20));  # cache: {1=10, 2=20}
print(lRUCache.put(3, 30));  # cache: {2=20, 3=30}, key=1 was evicted
print(lRUCache.get(2));      # returns 20 
print(lRUCache.get(1));      # return -1 (not found)

# solution = Solution()
# nums = [1,2,3,2,2]
# list1 = ListNode(l1[0])
# current = list1
# for val in l1[1:]:
#     current.next = ListNode(val)
#     current = current.next
    
# list2 = ListNode(l2[0])
# current = list2
# for val in l2[1:]:
#     current.next = ListNode(val)
#     current = current.next

# print(solution.findDuplicate(nums))


