from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
              
    def insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_values(self, data_list):
        if self.head is None:
            self.head = None       
        for data in data_list:
            self.insert(data)
            
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at_index(self, index):
        if index < 0 or index > self.get_length():
            return None
        
        if index == 0:
            self.head = self.head.next
            return
               
        count = 0
        curr = self.head
        
        while curr:
            if count == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            count += 1
      
            
    def print(self):
        if self.head == None:
            return print("Empty LL")
        
        listr = ''
        itr = self.head
        while itr:
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)
        
    def reverseList(self):
        """Given the beginning of a singly linked list head, reverse the list, 
        and return the new beginning of the list."""
        if not self.head:
            return None
        
        prev = None
        curr = self.head
        while curr:
            if not curr.next:
                self.head = curr
            next = curr.next 
            curr.next = prev 
            prev = curr
            curr = next          
            
        return prev
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[Node]:
        """You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
        The new list should be made up of nodes from list1 and list2."""
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1 
        elif list2:
            tail.next = list2 
        return dummy.next
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """You are given the head of a singly linked-list. The positions of a linked list of length = 7 for example, can intially be represented as:
        [0, 1, 2, 3, 4, 5, 6]
        Reorder the nodes of the linked list to be in the following order: [0, 6, 1, 5, 2, 4, 3]
        Notice that in the general case for a list of length = n the nodes are reordered to be in the following order: [0, n-1, 1, n-2, 2, n-3, ...]
        You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves."""
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next 
            second.next = prev
            prev = second
            second = temp
            
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next 
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2 
            
        return
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """"You are given the beginning of a linked list head, and an integer n.
        Remove the nth node from the end of the list and return the beginning of the list."""
        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        while n > 0:
            r = r.next
            n -= 1
            
        while r:
            l = l.next
            r = r.next
            
        l.next = l.next.next 
        return dummy.next 
            
        



def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()       

solution = Solution()
values = [1, 2, 3, 4, 5]
list1 = ListNode(values[0])
current = list1
for val in values[1:]:
    current.next = ListNode(val)
    current = current.next

print_linked_list(list1)
n = 2
result = solution.removeNthFromEnd(list1, n)
print_linked_list(list1)


