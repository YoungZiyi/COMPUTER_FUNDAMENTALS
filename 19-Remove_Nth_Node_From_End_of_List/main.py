# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toObj(li: list) -> ListNode:
    head_node = None
    prev_node = None
    for i in li:
        new_node = ListNode(i)
        if prev_node:
            prev_node.next = new_node
        else:
            head_node = new_node
        prev_node = new_node
    return head_node

def toList(node: ListNode) -> list:
    if not node:
        return []
    li = []
    li.append(node.val)
    if not node.next:
        return li
    node = node.next
    li.extend(toList(node))
    return li


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n):
            if first.next:
                first = first.next
            else:
                break
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        li = []
        li.append(head)
        cur = head
        while cur.next:
            if len(li) == n+1:
                li.pop(0)
            li.append(cur.next)
            cur = cur.next
        
        if n>1 and len(li) < n+1:
            return li[1]

        if len(li) == 1:
            return None
        elif len(li) == 2:
            li[0].next = None
        else:
            li[0].next = li[2]
        return head
        


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.removeNthFromEnd()
        self.assertEqual()

if __name__ == '__main__':
    # unittest.main()
    head = toObj({1})
    head = (Solution()).removeNthFromEnd(head, 1)
    print(toList(head))