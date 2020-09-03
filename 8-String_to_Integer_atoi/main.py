class Solution:
    mapping = {
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
    }
    maxInt = 2**31-1
    minInt = -2**31
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        
        sign = 1
        if str == '':
            return 0
        elif str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        res = 0
        for c in str:
            if self.mapping.get(c) != None:
                res = res*10 + self.mapping[c]
            else:
                break
            if res > self.maxInt:
                break
        res = res * sign
        if res > self.maxInt:
            return self.maxInt
        elif res < self.minInt:
            return self.minInt
        return res
        

import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.myAtoi("42")
        self.assertEqual(ret, 42)
    def test_2(self):
        ret = self.obj.myAtoi("   -42")
        self.assertEqual(ret, -42)
    def test_3(self):
        ret = self.obj.myAtoi("4193 with words")
        self.assertEqual(ret, 4193)
    def test_4(self):
        ret = self.obj.myAtoi("words and 987")
        self.assertEqual(ret, 0)
    def test_5(self):
        ret = self.obj.myAtoi("-91283472332")
        self.assertEqual(ret, -2147483648)
    def test_6(self):
        ret = self.obj.myAtoi("+42")
        self.assertEqual(ret, 42)
    def test_7(self):
        ret = self.obj.myAtoi("+-42")
        self.assertEqual(ret, 0)
    def test_8(self):
        ret = self.obj.myAtoi("")
        self.assertEqual(ret, 0)
    def test_9(self):
        ret = self.obj.myAtoi("2147483648")
        self.assertEqual(ret, 2147483647)
        

if __name__ == '__main__':
    unittest.main()
    print(((Solution()).myAtoi("2147483648")))
