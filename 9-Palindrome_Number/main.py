class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        old = x
        while x:
            rev = (rev * 10) + (x % 10)
            x = x // 10
        if rev == old:
            return True
        return False



import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.isPalindrome(3)
        self.assertEqual(ret, True)
    def test_2(self):
        ret = self.obj.isPalindrome(121)
        self.assertEqual(ret, True)
    def test_3(self):
        ret = self.obj.isPalindrome(-121)
        self.assertEqual(ret, False)
    def test_4(self):
        ret = self.obj.isPalindrome(10)
        self.assertEqual(ret, False)

if __name__ == '__main__':
    unittest.main()
    print((Solution()).isPalindrome(121))