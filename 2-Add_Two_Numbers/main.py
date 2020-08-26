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
    li = []
    li.append(node.val)
    if not node.next:
        return li
    node = node.next
    li.extend(toList(node))
    return li
            
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        这个很慢 140ms
        """
        head = ListNode()
        curr = head
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

            addition = a+b+carry
            curr.next = ListNode((addition)%10)
            carry = addition//10
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)
        return head.next



import unittest
class TestStringMethods(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        l1 = toObj([1,2,3])
        l2 = toObj([1,2,3])
        l3 = obj.addTwoNumbers(l1, l2)
        self.assertEqual(toList(l3), [2,4,6])
    def test_2(self):
        obj = Solution()
        l1 = toObj([5])
        l2 = toObj([5])
        l3 = obj.addTwoNumbers(l1, l2)
        self.assertEqual(toList(l3), [0,1])
    def test_3(self):
        obj = Solution()
        l1 = toObj([5,1])
        l2 = toObj([5])
        l3 = obj.addTwoNumbers(l1, l2)
        self.assertEqual(toList(l3), [0,2])

if __name__ == '__main__':
    unittest.main()
