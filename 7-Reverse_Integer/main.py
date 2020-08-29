class Solution:
    def reverse(self, x: int) -> int:
        import sys
        i = 1
        if x < 0:
            x = -x
            i = -1
        
        ret = 0
        while x:
            n = x % 10
            ret = ret * 10 + n
            if ret > sys.maxsize:
                return 0
            x = x // 10
        return ret*i

import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.reverse(3)
        self.assertEqual(ret, 3)
    def test_2(self):
        ret = self.obj.reverse(123)
        self.assertEqual(ret, 321)
    def test_3(self):
        ret = self.obj.reverse(-123)
        self.assertEqual(ret, -321)
    def test_4(self):
        ret = self.obj.reverse(120)
        self.assertEqual(ret, 21)
    def test_5(self):
        ret = self.obj.reverse(1534236469)
        self.assertEqual(ret, 0)
    

if __name__ == '__main__':
    # unittest.main()
    print((Solution()).reverse(1534236469))