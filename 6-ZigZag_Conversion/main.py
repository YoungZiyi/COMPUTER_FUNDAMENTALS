class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 0:
            return ''
        elif numRows == 1:
            return s
        m = {}
        for i in range(numRows):
            m[i] = ''
        i = 0
        n = -1
        for c in s:
            m[i] += c
            if i == 0 or i == numRows-1:
                n = -n
            i += n
        ret = ''
        for i in m:
            ret += m[i]
        return ret


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.convert('PAYPALISHIRING', 3)
        self.assertEqual(ret, 'PAHNAPLSIIGYIR')
    def test_2(self):
        ret = self.obj.convert('PAYPALISHIRING', 0)
        self.assertEqual(ret, '')
    def test_3(self):
        ret = self.obj.convert('PAYPALISHIRING', 4)
        self.assertEqual(ret, 'PINALSIGYAHRPI')
    def test_4(self):
        ret = self.obj.convert('PAYPALISHIRING', 1)
        self.assertEqual(ret, 'PAYPALISHIRING')

if __name__ == '__main__':
    unittest.main()
    print((Solution()).convert('asdfghj', 5))