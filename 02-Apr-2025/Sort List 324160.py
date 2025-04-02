# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def merge(left,right):
            dummy=ListNode()
            current=dummy
            while left and right:
                if left.val<=right.val:
                    current.next=left
                    left=left.next
                else:
                    current.next=right
                    right=right.next


                current=current.next

            current.next=left if left else right
            return dummy.next

          
        def mergesort(head):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next

            mid=slow.next
            slow.next=None
            return head, mid

        left,right=mergesort(head)
        left_sorted=self.sortList(left)
        right_sorted=self.sortList(right)
        return merge(left_sorted,right_sorted)