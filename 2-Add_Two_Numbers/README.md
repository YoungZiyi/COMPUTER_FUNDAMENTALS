# 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
```

解题思路:
同时遍历两个链表的节点, 两个节点的值再加上上一个节点的carry值, 如果大于10则取余并用一个变量carry保存进位, 以该值创建一个新节点,  
遍历结束后记得检查carry, 如果carry>0 则还需创建一个节点
