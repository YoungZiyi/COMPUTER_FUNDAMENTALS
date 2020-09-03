class Solution:
    from typing import List
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        a = 0
        d = None
        l = len(nums)
        for i in range(l-2):
            j = i+1
            k = l-1
            while j < k:
                addition = nums[i] + nums[j] + nums[k]
                diff = target - addition
                if diff > 0:
                    j += 1
                elif diff < 0:
                    k -= 1
                else:
                    return target

                if d == None or abs(diff) < d:
                    d = abs(diff)
                    a = addition
        return a


import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.threeSumClosest([-1,2,1,-4], 1)
        self.assertEqual(ret, 2)
    def test_2(self):
        ret = self.obj.threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0)
        self.assertEqual(ret, 0)
        

if __name__ == '__main__':
    unittest.main()
    print(((Solution()).threeSumClosest([-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33], 0)))
