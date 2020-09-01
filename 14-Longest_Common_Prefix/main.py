class Solution:
    from typing import List
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        '''
        Horizontal scanning
        48ms
        '''
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix2 = self.findPrefix(prefix, strs[i])
            prefix = prefix2 if len(prefix2) < len(prefix) else prefix
        return prefix

    def findPrefix(self, str1, str2):
        if str1 == '' or str2 == '':
            return ''
        mLength = min(len(str1), len(str2))
        for i in range(mLength):
            if str1[i] != str2[i]:
                return str1[0:i]
        return str1[0:i+1]
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Vertical scanning
        40ms
        '''
        prefix = ''
        if not strs:
            return prefix
        for i in range(0, len(strs[0])):
            for j in range(0, len(strs)-1):
                if i >= len(strs[j]) or i >= len(strs[j+1]) or strs[j][i] != strs[j+1][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        '''
        Binary search
        '''
        if not strs:
            return ''
        mid = len(strs[0]) // 2
        cur = strs[0][0:mid]
        prefix = ''
        while True:
            if mid < 0:
                return ''
            for s in strs:
                if mid > len(s):
                    mid = len(s) // 2
                    break
                if cur != s[0:mid]:
                    if prefix:
                        return prefix
                    mid -= 1
                    break
                mid += 1
                cur = s[0:mid]
            prefix = cur
        
        return prefix

import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.longestCommonPrefix(["flower","flow","flight"])
        self.assertEqual(ret, 'fl')
    def test_2(self):
        ret = self.obj.longestCommonPrefix(["dog","racecar","car"])
        self.assertEqual(ret, '')
    def test_3(self):
        ret = self.obj.longestCommonPrefix(["b","cb","cab"])
        self.assertEqual(ret, '')
    def test_4(self):
        ret = self.obj.longestCommonPrefix(["a"])
        self.assertEqual(ret, 'a')
    def test_5(self):
        ret = self.obj.longestCommonPrefix([])
        self.assertEqual(ret, '')

        

if __name__ == '__main__':
    # unittest.main()
    # print(((Solution()).longestCommonPrefix([])))
    print(((Solution()).longestCommonPrefix2(['aaaa', 'aaa'])))
    # print(((Solution()).findPrefix('asdf','a')))
