class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        more readable version, cost 90ms
        """
        total = len(nums1) + len(nums2)
        mid = total//2
        first, second = 0, 0
        for _ in range(mid+1):
            second = first
            if not nums1:
                first = nums2.pop()
            elif not nums2:
                first = nums1.pop()
            else:
                first = nums1.pop() if nums1[-1] > nums2[-1] else nums2.pop()
        return first if total%2 else round((first+second)/2, 5)

    def findMedianSortedArrays_2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float

        cost 96ms
        """
        # nums1.reverse()
        # nums2.reverse()

        total = len(nums1) + len(nums2)
        mid = total//2
        a = b = num = None
        i = 0
        while i < mid:
            i += 1
            # pop a number from each list
            a = nums1.pop() if a == None and nums1 else a
            b = nums2.pop() if b == None and nums2 else b

            if a == None and b == None:
                continue
            if a == None:
                num = b
                b = None
                continue
            if b == None:
                num = a
                a = None
                continue
            
            if a > b:
                num = a
                a = None
            else:
                num = b
                b = None

        if a == None and nums1:
            a = nums1.pop()
        if b == None and nums2:
            b = nums2.pop()

        if total%2:
            if a == None:
                return b
            if b == None:
                return a
            return a if a > b else b
        else:
            if a == None:
                return round((num+b)/2, 5)
            if b == None:
                return round((num+a)/2, 5)
            return round((num+a)/2, 5) if a > b else round((num+b)/2, 5)



import unittest
class TestStringMethods(unittest.TestCase):
    obj = Solution()
    def test_1(self):
        nums1 = [1,3]
        nums2 = [2]
        ret = self.obj.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(ret, 2.00000)
    def test_2(self):
        nums1 = [1,2]
        nums2 = [3,4]
        ret = self.obj.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(ret, 2.50000)
    def test_3(self):
        nums1 = [0,0]
        nums2 = [0,0]
        ret = self.obj.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(ret, 0.00000)
    def test_4(self):
        nums1 = []
        nums2 = [1]
        ret = self.obj.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(ret, 1.00000)
    def test_5(self):
        nums1 = [2]
        nums2 = []
        ret = self.obj.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(ret, 2.00000)

if __name__ == '__main__':
    unittest.main()
    nums1, nums2 = [1,3], [2]
    # print((Solution()).findMedianSortedArrays(nums1, nums2))
