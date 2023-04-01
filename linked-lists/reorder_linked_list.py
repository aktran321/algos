def reorderList(head):


        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        newHead = slow.next
        slow.next = None 
        while newHead:
            temp = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = temp
        while prev:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            head = tmp1
            prev.next = head
            prev = tmp2
