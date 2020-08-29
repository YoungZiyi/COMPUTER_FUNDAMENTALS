class Solution:
    symbols = {
        1:'I',
        5:'V',
        10:'X',
        50:'L',
        100:'C',
        500:'D',
        1000:'M',
    }
    def intToRoman(self, num: int) -> str:
        roman = ''
        p = 1
        while num:
            n = (num % 10)
            if p == 1000:
                roman = self.symbols[p] * n + roman
                break
            p *= 10
            if n == 9:
                roman = self.symbols[p/10] + self.symbols[p] + roman
            elif n == 4:
                roman = self.symbols[p/10] + self.symbols[p/2] + roman
            else:
                if n < 5:
                    roman = (self.symbols[p/10] * n) + roman
                else:
                    roman = self.symbols[p/2] + (self.symbols[p/10] * (n-5)) + roman
            num = num // 10
        return roman



        

import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.intToRoman(1994)
        self.assertEqual(ret, 'MCMXCIV')
    def test_2(self):
        ret = self.obj.intToRoman(58)
        self.assertEqual(ret, 'LVIII')
    def test_3(self):
        ret = self.obj.intToRoman(3)
        self.assertEqual(ret, 'III')
    def test_4(self):
        ret = self.obj.intToRoman(4)
        self.assertEqual(ret, 'IV')
    def test_5(self):
        ret = self.obj.intToRoman(9)
        self.assertEqual(ret, 'IX')
    def test_6(self):
        ret = self.obj.intToRoman(0)
        self.assertEqual(ret, '')

if __name__ == '__main__':
    unittest.main()
    print((Solution()).intToRoman(0))