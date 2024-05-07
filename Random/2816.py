# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        dummy.next = head
        curr,prev = head,dummy

        while curr:
            double = 2*curr.val
            if double<10:
                curr.val = double
            else:
                curr.val = double%10
                prev.val+=1
            prev = curr
            curr = curr.next

        return dummy if dummy.val else dummy.next