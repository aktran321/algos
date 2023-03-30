def removeNthFromEnd(head):
        dummy = ListNode(0, head)
        left=right =dummy
        while n > 0:
            right = right.next
            n -= 1
        while right:
            right = right.next
            prev = left
            left = left.next
        prev.next = left.next
        return dummy.next