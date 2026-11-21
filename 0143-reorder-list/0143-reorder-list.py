# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find the middle
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #divide first and second half
        curr = slow.next
        slow.next = None
        prev = None
        #reverse the second half
        while curr:
            nn = curr.next
            curr.next = prev
            prev = curr
            curr = nn
        #merge two halfs
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        
        