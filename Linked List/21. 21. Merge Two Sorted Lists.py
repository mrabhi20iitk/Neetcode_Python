# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None: return list2
        if list2 == None: return list1
        
        curr1 , curr2 = list1, list2
        dummy = ListNode()
        tail = dummy
        while curr1!=None and curr2!=None:
            if curr1.val <  curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            
            tail = tail.next
            
        if curr1!=None: tail.next = curr1
        if curr2!=None: tail.next = curr2
            
            
        return dummy.next
                
                
                
                
        