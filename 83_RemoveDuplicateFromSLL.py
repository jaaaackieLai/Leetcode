class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        current = head
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

# main
# set test data
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(1)

# solution
sol = Solution()
res = sol.deleteDuplicates(ll.head)  # Pass the head of the linked list

# print
arr = []
while res:
    arr.append(res.val)
    res = res.next

print(arr)  # This should now print [1, 2] correctly

