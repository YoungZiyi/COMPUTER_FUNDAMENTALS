class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中心扩散法
        cost 1572ms, 13.8MB
        """
        total = len(s)
        if total <= 1:
            return s

        ret = s[0]
        for i in range(0, total-1):
            tmp1 = self.centralCheck(s, i, i)
            tmp2 = self.centralCheck(s, i, i+1)
            tmp = tmp1 if len(tmp1) > len(tmp2) else tmp2
            ret = tmp if len(tmp) > len(ret) else ret
        return ret

    def centralCheck(self, s: str, i: int, j: int) -> str:
        ret = s[i]
        while i>=0 and j<len(s):
            if s[i] != s[j]:
                break
            ret = s[i:j+1]
            i -= 1
            j += 1
        return ret

    def longestPalindromeBruteForce(self, s: str) -> str:
        """
        Brute force
        Time Limit Exceeded...
        """
        total = len(s)
        if total == 0:
            return ''

        ret = s[0]
        for i in range(total-1):
            if total-i <= len(ret):
                break
            for j in range(i+1, total):
                if j-i+1 <= len(ret):
                    continue
                sub = s[i:j+1]
                if self.check(sub):
                    ret = sub
        return ret
    
    def check(self, s: str) -> bool:
        """
        判断子串是否是回文
        """
        left = 0
        right = len(s)-1
        if right == 0:
            return True
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        s = 'babad'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'bab')
    def test_2(self):
        s = 'cbbd'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'bb')
    def test_3(self):
        s = 'a'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'a')
    def test_4(self):
        s = 'ab'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'a')
    def test_5(self):
        s = 'ccc'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'ccc')
    def test_6(self):
        s = 'abadd'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'aba')
    def test_7(self):
        s = 'abcda'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'a')
    def test_8(self):
        s = 'bananas'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'anana')
    def test_9(self):
        s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    def test_10(self):
        s = 'abb'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'bb')
    def test_11(self):
        s = 'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
    def test_10(self):
        s = 'bb'
        ret = self.obj.longestPalindrome(s)
        self.assertEqual(ret, 'bb')

if __name__ == '__main__':
    unittest.main()
    print(((Solution()).longestPalindrome('bb')))

