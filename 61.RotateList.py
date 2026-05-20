# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        # get length

        length, tail = 1, head
        while tail.next:
            tail =tail.next
            length += 1
        
        k = k % length
        if k ==0:
            return head
        
        # move to pivot point and rotate

        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        newHead = curr.next
        curr.next = None
        tail.next = head

        return newHead