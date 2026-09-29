# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Linked List Solution with Two Pointers
        prev = None # Pointer One - initialize prev as None
        curr = head # Pointer Two - start with curr at the head of the list

        while curr: # while the head exists
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
