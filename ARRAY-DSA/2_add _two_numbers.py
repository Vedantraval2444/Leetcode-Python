# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list_head = ListNode(0)
        curr = list_head 
        carry = 0 # Store the carry value

        while l1 or l2 or carry: 
            val1 = l1.val if l1 else 0 # Get value from l1 or 0 if l1 is None
            val2 = l2.val if l2 else 0 # Get value from l2 or 0 if l2 is None

            carry, sum_val = divmod(val1 + val2 + carry, 10) # Calculate carry and sum value

            curr.next = ListNode(sum_val) # Create a new node with the sum value
            curr = curr.next

            l1 = l1.next if l1 else None # Move to the next node in l1 if it exists
            l2 = l2.next if l2 else None

        return list_head.next 