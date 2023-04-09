
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# need to make sure, that I am paying closer attention to while loop conditions
def copyRandomList(head):
        cur = head
        ogToCopy = {None:None}
        while cur:
            newNode = Node(cur.val)
            ogToCopy[cur] = newNode
            cur = cur.next
        cur = head
        while cur:
            copy = ogToCopy[cur]
            copy.next = ogToCopy[cur.next]
            copy.random = ogToCopy[cur.random]
            cur = cur.next
        return ogToCopy[head]