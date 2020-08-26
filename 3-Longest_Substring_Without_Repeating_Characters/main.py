class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window
        60ms
        """
        index = {}
        maxLength = left = right = 0
        for i, c in enumerate(s):
            right = i
            if None != index.get(c):
                if left <= index.get(c):
                    left = index.get(c)+1
            index[c] = i
            curr = right-left+1
            maxLength = curr if curr>maxLength else maxLength
        return maxLength



import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.lengthOfLongestSubstring('abcabcbb')
        self.assertEqual(ret, 3)
    def test_2(self):
        ret = self.obj.lengthOfLongestSubstring('asdfa')
        self.assertEqual(ret, 4)
    def test_3(self):
        ret = self.obj.lengthOfLongestSubstring('dvdf')
        self.assertEqual(ret, 3)
    def test_4(self):
        ret = self.obj.lengthOfLongestSubstring('aab')
        self.assertEqual(ret, 2)
    def test_5(self):
        ret = self.obj.lengthOfLongestSubstring('abba')
        self.assertEqual(ret, 2)
    def test_6(self):
        ret = self.obj.lengthOfLongestSubstring('tmmzuxt')
        self.assertEqual(ret, 5)

if __name__ == '__main__':
    unittest.main()
