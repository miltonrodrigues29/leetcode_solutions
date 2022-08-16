class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l ,  r = 0 , 0
        for i in nums:
            r = r + i
        for i in range(len(nums)):
            r = r - nums[i]
            if l == r:
                return i
            else:
                l = l + nums[i]
        return -1
