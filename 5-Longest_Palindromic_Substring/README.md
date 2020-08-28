# 5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```
Example 2:
```
Input: "cbbd"
Output: "bb"
```


回文特性指的是一个串从前往后和从后往前读是一样的
例如 'abcba', '1234321'

1 暴力破解法
    遍历所有子串, 判断子串是否符合回文特性
    判断方法:双指针指向子串首尾, 判断指针位字符是否相同, 并向中心聚拢
    O(n^3)

2 中心扩展法
    遍历字符串中每一个字符, 以该字符为中心向两边扩散, 判断对应位置字符是否相等
    需要注意奇偶数两种情况, eg: 'aba', 'abbc'

3 Manacher's Algorithm (马拉车算法)
    TODO: