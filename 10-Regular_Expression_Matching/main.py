class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        sLength = len(s)
        pLength = len(p)

        sp = ''
        cur = 0
        for i in range(pLength):

            if (i+1) >= pLength or p[i+1] != '*' or p[i+1] != '.':
                sp += p[i]
                continue
            # compare
            if sp and sp == s[cur : len(sp)]:
                cur += len(sp)
                sp = ''
            else:
                return False

            if p[i+1] == '*':
                pass

            if p[i+1] == '.':
                pass
        
        if sp and sp != s[cur : len(sp)]:
            return False
        return True


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.isMatch('asd', 'asd')
        self.assertEqual(ret, True)

if __name__ == '__main__':
    # unittest.main()
    print((Solution()).isMatch('asd', 'asdd'))