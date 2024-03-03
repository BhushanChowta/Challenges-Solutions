#169
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=Counter(nums)
        return max(counts,key=counts.get)
            
