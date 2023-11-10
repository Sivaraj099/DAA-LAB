class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def has_loop(head):
    if head is None:
        return False
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
head = ListNode(10)
n1 = ListNode(20)
head.next = n1
n2 = ListNode(20)
n1.next = n2
n3 = ListNode(40)
n2.next = n3
n3.next = n1
result = has_loop(head)
print(result)