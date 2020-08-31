class Solution:
    symbols = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }
    def romanToInt(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            n = i+1
            if n >= len(s):
                ret += self.symbols[s[i]]
                break
            if self.symbols[s[n]] > self.symbols[s[i]]:
                ret -= self.symbols[s[i]]
            else:
                ret += self.symbols[s[i]]
        return ret


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.romanToInt('M')
        self.assertEqual(ret, 1000)
    def test_2(self):
        ret = self.obj.romanToInt('III')
        self.assertEqual(ret, 3)

    def test_3(self):
        ret = self.obj.romanToInt('IV')
        self.assertEqual(ret, 4)
    def test_4(self):
        ret = self.obj.romanToInt('IX')
        self.assertEqual(ret, 9)
    def test_5(self):
        ret = self.obj.romanToInt('LVIII')
        self.assertEqual(ret, 58)
    def test_6(self):
        ret = self.obj.romanToInt('MCMXCIV')
        self.assertEqual(ret, 1994)

if __name__ == '__main__':
    unittest.main()
    print(((Solution()).romanToInt('MCMXCIV')))
