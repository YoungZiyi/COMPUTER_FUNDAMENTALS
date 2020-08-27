class Solution(object):
    # 512 ms
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            try:
                i1 = nums.index(i)
                i2 = nums.index(target-i, i1+1)
                return [i1, i2]
            except IndexError:
                continue
            except ValueError:
                continue
        return []
    # 368 ms
    def twoSum2(self, nums, target):
        tnums = list(enumerate(nums))
        for i in tnums:
            try:
                i1 = i[0]
                i2 = nums.index(target-i[1], i1+1)
                return [i1, i2]
            except IndexError:
                continue
            except ValueError:
                continue
        return []
    # hash 32ms
    def twoSum3(self, nums, target):
        m = {}
        for i in range(len(nums)):
            if m.get(target-nums[i]) is not None:
                return [m.get(target-nums[i]), i]
            m[nums[i]] = i

        
if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum3([3,2,4], 6))
