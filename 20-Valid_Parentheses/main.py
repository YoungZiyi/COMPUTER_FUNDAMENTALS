class Solution:
    mapping = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if None == self.mapping.get(c):
                stack.append(c)
            else:
                if not stack or stack.pop() != self.mapping.get(c):
                    return False
        # l = list(s)
        # while l:
        #     c = l.pop(0)
        #     if None == self.mapping.get(c):
        #         stack.append(c)
        #     else:
        #         if not stack or stack.pop() != self.mapping.get(c):
        #             return False
        if stack:
            return False
        return True


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.isValid('()')
        self.assertEqual(ret, True)
    def test_2(self):
        ret = self.obj.isValid("()[]{}")
        self.assertEqual(ret, True)
    def test_3(self):
        ret = self.obj.isValid('(]')
        self.assertEqual(ret, False)
    def test_4(self):
        ret = self.obj.isValid('([)]')
        self.assertEqual(ret, False)
    def test_5(self):
        ret = self.obj.isValid('{[]}')
        self.assertEqual(ret, True)
    def test_6(self):
        ret = self.obj.isValid(')')
        self.assertEqual(ret, False)
        

if __name__ == '__main__':
    unittest.main()
    print(((Solution()).isValid(')')))
