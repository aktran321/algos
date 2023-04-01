
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
            
def copyRandomList(head):
        cur = head
        # ok, what i want to do is loop through the input list, and create new nodes. The new nodes need to be entered into a hashmap. we will use a dictionary.
        ogToCopy = {None:None}
        while cur:
            newNode = ListNode(cur.val)
            ogToCopy[cur] = newNode
            cur = cur.next
        cur = head
        # now that we have the newNodes, and a way to access them and change their values
        # we can loop through the original list again, and then create the links for the newNodes. 
        while cur:
            copy = ogToCopy[cur]
            copy.next = ogToCopy[cur.next]
            copy.random = ogToCopy[cur.random]
            cur = cur.next
        return ogToCopy[head]