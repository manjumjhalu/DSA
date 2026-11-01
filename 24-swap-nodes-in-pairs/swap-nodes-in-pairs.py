
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next

            # Swap nodes
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to next pair
            prev = first

        return dummy.next
