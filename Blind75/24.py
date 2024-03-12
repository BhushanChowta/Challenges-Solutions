#53 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        cs=ms=nums[0]

        for num in nums[1:]:
            cs=max(num,cs+num)
            ms=max(cs,ms)
        
        return ms