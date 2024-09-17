from typing import Optional


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
    
def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    """You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
    The new list should be made up of nodes from list1 and list2."""
    # dummy = Node()
    # tail = dummy
    
    # while list1 and list2:
    #     if list1.data < list2.data:
    #         tail.next = list1
    #         list1 = list1.next
    #     else:
    #         tail.next = list2
    #         list2 = list2.next
    #     tail = tail.next
        
    # if list1:
    #     tail.next = list1 
    # elif list2:
    #     tail.next = list2 
    
    # return dummy.next
    list3 = LinkedList()
    l1 = list1.head 
    l2 = list2.head
    
    while l1 and l2:
        if l1.data < l2.data:
            list3.insert(l1)
            l1 = l1.next 
        else:
            list3.insert(l2)
            l2 = l2.next
    if l1:
        list3.insert(l1)
    elif list2:
        list3.insert(l2)
    list3.print()
    return list3
        

ll = LinkedList()
ll.insert_values([0,1,2,3])
list1 = LinkedList()
list1.insert_values([1, 2, 3])
list2 = LinkedList() 
list2.insert_values([1,2])
list1.print()
list2.print()
mergeTwoLists(list1, list2)


