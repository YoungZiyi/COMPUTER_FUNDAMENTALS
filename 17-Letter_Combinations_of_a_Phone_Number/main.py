from typing import List
import itertools
class Solution:
    phoneNumbers = {
        '0': [],
        '1': [],
        '2': ['a','b','c'],
        '3': ['d','e','f'],
        '4': ['g','h','i'],
        '5': ["j","k","l"],
        '6': ['m','n','o'],
        '7': ['p','q','r','s'],
        '8': ['t','u','v'],
        '9': ['w','x','y','z'],
        '*': ['d','o','w','n','c','a','s','t',' ','o','f'],
        '#': ["v","p","t","r","_","c","h","e","c","k"],
    }
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        l = len(digits)
        if 0 == l:
            return []
        elif 1 == l:
            return [] if None == self.phoneNumbers.get(digits[0]) else self.phoneNumbers[digits[0]]
        res = [] if None == self.phoneNumbers.get(digits[0]) else self.phoneNumbers[digits[0]]
        for i in range(1, l):
            s = [] if None == self.phoneNumbers.get(digits[i]) else self.phoneNumbers[digits[i]]
            res = list(itertools.product(res, s))
            res = list(map(lambda x: ''.join(x), res))
        return res
        

import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.letterCombinations("23")
        self.assertEqual(ret, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    def test_2(self):
        ret = self.obj.letterCombinations("12")
        self.assertEqual(ret, [])
    def test_3(self):
        ret = self.obj.letterCombinations("2")
        self.assertEqual(ret, ["a","b","c"])
    def test_4(self):
        ret = self.obj.letterCombinations("20")
        self.assertEqual(ret, [])
    def test_5(self):
        ret = self.obj.letterCombinations("2*")
        self.assertEqual(ret, ["ad","ao","aw","an","ac","aa","as","at","a ","ao","af","bd","bo","bw","bn","bc","ba","bs","bt","b ","bo","bf","cd","co","cw","cn","cc","ca","cs","ct","c ","co","cf"])
    def test_6(self):
        ret = self.obj.letterCombinations("*")
        self.assertEqual(ret, ["d","o","w","n","c","a","s","t"," ","o","f"])
        

if __name__ == '__main__':
    unittest.main()
    print(((Solution()).letterCombinations("2*")))
