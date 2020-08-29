class Solution:
    from typing import List
    def maxArea(self, height: List[int]) -> int:
        '''
        168 ms
        '''
        total = len(height)
        maxSize = 0
        left = 0
        right = total - 1
        
        while left < right:
            currWidth = right - left
            currHeight = height[left] if height[left] <= height[right] else height[right]
            
            size = currWidth * currHeight
            if size > maxSize:
                maxSize = size
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxSize

import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        ret = self.obj.maxArea([1,8,6,2,5,4,8,3,7])
        self.assertEqual(ret, 49)

if __name__ == '__main__':
    unittest.main()
    print((Solution()).maxArea([1,8,6,2,5,4,8,3,7]))