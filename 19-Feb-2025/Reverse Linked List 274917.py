# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        newlist=None
        while current:
            next_node=current.next
            current.next=newlist
            newlist=current
            current=next_node
        return newlist
        